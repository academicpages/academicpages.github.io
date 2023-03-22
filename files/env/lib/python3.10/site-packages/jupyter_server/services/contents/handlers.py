"""Tornado handlers for the contents web service.

Preliminary documentation at https://github.com/ipython/ipython/wiki/IPEP-27%3A-Contents-Service
"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import json

try:
    from jupyter_client.jsonutil import json_default
except ImportError:
    from jupyter_client.jsonutil import date_default as json_default

from tornado import web

from jupyter_server.auth import authorized
from jupyter_server.base.handlers import APIHandler, JupyterHandler, path_regex
from jupyter_server.utils import ensure_async, url_escape, url_path_join

AUTH_RESOURCE = "contents"


def validate_model(model, expect_content):
    """
    Validate a model returned by a ContentsManager method.

    If expect_content is True, then we expect non-null entries for 'content'
    and 'format'.
    """
    required_keys = {
        "name",
        "path",
        "type",
        "writable",
        "created",
        "last_modified",
        "mimetype",
        "content",
        "format",
    }
    missing = required_keys - set(model.keys())
    if missing:
        raise web.HTTPError(
            500,
            f"Missing Model Keys: {missing}",
        )

    maybe_none_keys = ["content", "format"]
    if expect_content:
        errors = [key for key in maybe_none_keys if model[key] is None]
        if errors:
            raise web.HTTPError(
                500,
                f"Keys unexpectedly None: {errors}",
            )
    else:
        errors = {key: model[key] for key in maybe_none_keys if model[key] is not None}  # type: ignore[assignment]
        if errors:
            raise web.HTTPError(
                500,
                f"Keys unexpectedly not None: {errors}",
            )


class ContentsAPIHandler(APIHandler):
    auth_resource = AUTH_RESOURCE


class ContentsHandler(ContentsAPIHandler):
    def location_url(self, path):
        """Return the full URL location of a file.

        Parameters
        ----------
        path : unicode
            The API path of the file, such as "foo/bar.txt".
        """
        return url_path_join(self.base_url, "api", "contents", url_escape(path))

    def _finish_model(self, model, location=True):
        """Finish a JSON request with a model, setting relevant headers, etc."""
        if location:
            location = self.location_url(model["path"])
            self.set_header("Location", location)
        self.set_header("Last-Modified", model["last_modified"])
        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(model, default=json_default))

    @web.authenticated
    @authorized
    async def get(self, path=""):
        """Return a model for a file or directory.

        A directory model contains a list of models (without content)
        of the files and directories it contains.
        """
        path = path or ""
        cm = self.contents_manager

        type = self.get_query_argument("type", default=None)
        if type not in {None, "directory", "file", "notebook"}:
            raise web.HTTPError(400, "Type %r is invalid" % type)

        format = self.get_query_argument("format", default=None)
        if format not in {None, "text", "base64"}:
            raise web.HTTPError(400, "Format %r is invalid" % format)
        content_str = self.get_query_argument("content", default="1")
        if content_str not in {"0", "1"}:
            raise web.HTTPError(400, "Content %r is invalid" % content_str)
        content = int(content_str or "")

        if await ensure_async(cm.is_hidden(path)) and not cm.allow_hidden:
            raise web.HTTPError(404, f"file or directory {path!r} does not exist")

        model = await ensure_async(
            self.contents_manager.get(
                path=path,
                type=type,
                format=format,
                content=content,
            )
        )
        validate_model(model, expect_content=content)
        self._finish_model(model, location=False)

    @web.authenticated
    @authorized
    async def patch(self, path=""):
        """PATCH renames a file or directory without re-uploading content."""
        cm = self.contents_manager
        model = self.get_json_body()
        if model is None:
            raise web.HTTPError(400, "JSON body missing")

        old_path = model.get("path")
        if (
            old_path
            and (
                await ensure_async(cm.is_hidden(path)) or await ensure_async(cm.is_hidden(old_path))
            )
            and not cm.allow_hidden
        ):
            raise web.HTTPError(400, f"Cannot rename file or directory {path!r}")

        model = await ensure_async(cm.update(model, path))
        validate_model(model, expect_content=False)
        self._finish_model(model)

    async def _copy(self, copy_from, copy_to=None):
        """Copy a file, optionally specifying a target directory."""
        self.log.info(
            "Copying {copy_from} to {copy_to}".format(
                copy_from=copy_from,
                copy_to=copy_to or "",
            )
        )
        model = await ensure_async(self.contents_manager.copy(copy_from, copy_to))
        self.set_status(201)
        validate_model(model, expect_content=False)
        self._finish_model(model)

    async def _upload(self, model, path):
        """Handle upload of a new file to path"""
        self.log.info("Uploading file to %s", path)
        model = await ensure_async(self.contents_manager.new(model, path))
        self.set_status(201)
        validate_model(model, expect_content=False)
        self._finish_model(model)

    async def _new_untitled(self, path, type="", ext=""):
        """Create a new, empty untitled entity"""
        self.log.info("Creating new %s in %s", type or "file", path)
        model = await ensure_async(
            self.contents_manager.new_untitled(path=path, type=type, ext=ext)
        )
        self.set_status(201)
        validate_model(model, expect_content=False)
        self._finish_model(model)

    async def _save(self, model, path):
        """Save an existing file."""
        chunk = model.get("chunk", None)
        if not chunk or chunk == -1:  # Avoid tedious log information
            self.log.info("Saving file at %s", path)
        model = await ensure_async(self.contents_manager.save(model, path))
        validate_model(model, expect_content=False)
        self._finish_model(model)

    @web.authenticated
    @authorized
    async def post(self, path=""):
        """Create a new file in the specified path.

        POST creates new files. The server always decides on the name.

        POST /api/contents/path
          New untitled, empty file or directory.
        POST /api/contents/path
          with body {"copy_from" : "/path/to/OtherNotebook.ipynb"}
          New copy of OtherNotebook in path
        """

        cm = self.contents_manager

        file_exists = await ensure_async(cm.file_exists(path))
        if file_exists:
            raise web.HTTPError(400, "Cannot POST to files, use PUT instead.")

        model = self.get_json_body()
        copy_from = model.get("copy_from")
        if (
            copy_from
            and (
                await ensure_async(cm.is_hidden(path))
                or await ensure_async(cm.is_hidden(copy_from))
            )
            and not cm.allow_hidden
        ):
            raise web.HTTPError(400, f"Cannot copy file or directory {path!r}")

        if model is not None:
            copy_from = model.get("copy_from")
            ext = model.get("ext", "")
            type = model.get("type", "")
            if copy_from:
                await self._copy(copy_from, path)
            else:
                await self._new_untitled(path, type=type, ext=ext)
        else:
            await self._new_untitled(path)

    @web.authenticated
    @authorized
    async def put(self, path=""):
        """Saves the file in the location specified by name and path.

        PUT is very similar to POST, but the requester specifies the name,
        whereas with POST, the server picks the name.

        PUT /api/contents/path/Name.ipynb
          Save notebook at ``path/Name.ipynb``. Notebook structure is specified
          in `content` key of JSON request body. If content is not specified,
          create a new empty notebook.
        """
        model = self.get_json_body()
        cm = self.contents_manager

        if model:
            if model.get("copy_from"):
                raise web.HTTPError(400, "Cannot copy with PUT, only POST")
            if (
                (model.get("path") and await ensure_async(cm.is_hidden(model.get("path"))))
                or await ensure_async(cm.is_hidden(path))
            ) and not cm.allow_hidden:
                raise web.HTTPError(400, f"Cannot create file or directory {path!r}")

            exists = await ensure_async(self.contents_manager.file_exists(path))
            if exists:
                await self._save(model, path)
            else:
                await self._upload(model, path)
        else:
            await self._new_untitled(path)

    @web.authenticated
    @authorized
    async def delete(self, path=""):
        """delete a file in the given path"""
        cm = self.contents_manager

        if await ensure_async(cm.is_hidden(path)) and not cm.allow_hidden:
            raise web.HTTPError(400, f"Cannot delete file or directory {path!r}")

        self.log.warning("delete %s", path)
        await ensure_async(cm.delete(path))
        self.set_status(204)
        self.finish()


class CheckpointsHandler(ContentsAPIHandler):
    @web.authenticated
    @authorized
    async def get(self, path=""):
        """get lists checkpoints for a file"""
        cm = self.contents_manager
        checkpoints = await ensure_async(cm.list_checkpoints(path))
        data = json.dumps(checkpoints, default=json_default)
        self.finish(data)

    @web.authenticated
    @authorized
    async def post(self, path=""):
        """post creates a new checkpoint"""
        cm = self.contents_manager
        checkpoint = await ensure_async(cm.create_checkpoint(path))
        data = json.dumps(checkpoint, default=json_default)
        location = url_path_join(
            self.base_url,
            "api/contents",
            url_escape(path),
            "checkpoints",
            url_escape(checkpoint["id"]),
        )
        self.set_header("Location", location)
        self.set_status(201)
        self.finish(data)


class ModifyCheckpointsHandler(ContentsAPIHandler):
    @web.authenticated
    @authorized
    async def post(self, path, checkpoint_id):
        """post restores a file from a checkpoint"""
        cm = self.contents_manager
        await ensure_async(cm.restore_checkpoint(checkpoint_id, path))
        self.set_status(204)
        self.finish()

    @web.authenticated
    @authorized
    async def delete(self, path, checkpoint_id):
        """delete clears a checkpoint for a given file"""
        cm = self.contents_manager
        await ensure_async(cm.delete_checkpoint(checkpoint_id, path))
        self.set_status(204)
        self.finish()


class NotebooksRedirectHandler(JupyterHandler):
    """Redirect /api/notebooks to /api/contents"""

    SUPPORTED_METHODS = ("GET", "PUT", "PATCH", "POST", "DELETE")

    def get(self, path):
        self.log.warning("/api/notebooks is deprecated, use /api/contents")
        self.redirect(url_path_join(self.base_url, "api/contents", url_escape(path)))

    put = patch = post = delete = get


class TrustNotebooksHandler(JupyterHandler):
    """Handles trust/signing of notebooks"""

    @web.authenticated
    @authorized(resource=AUTH_RESOURCE)
    async def post(self, path=""):
        cm = self.contents_manager
        await ensure_async(cm.trust_notebook(path))
        self.set_status(201)
        self.finish()


# -----------------------------------------------------------------------------
# URL to handler mappings
# -----------------------------------------------------------------------------


_checkpoint_id_regex = r"(?P<checkpoint_id>[\w-]+)"


default_handlers = [
    (r"/api/contents%s/checkpoints" % path_regex, CheckpointsHandler),
    (
        rf"/api/contents{path_regex}/checkpoints/{_checkpoint_id_regex}",
        ModifyCheckpointsHandler,
    ),
    (r"/api/contents%s/trust" % path_regex, TrustNotebooksHandler),
    (r"/api/contents%s" % path_regex, ContentsHandler),
    (r"/api/notebooks/?(.*)", NotebooksRedirectHandler),
]

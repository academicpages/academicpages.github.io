"""A contents manager that uses the local file system for storage."""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import errno
import mimetypes
import os
import shutil
import stat
import sys
from datetime import datetime

import nbformat
from anyio.to_thread import run_sync
from jupyter_core.paths import exists, is_file_hidden, is_hidden
from send2trash import send2trash
from tornado import web
from traitlets import Bool, TraitError, Unicode, default, validate

from jupyter_server import _tz as tz
from jupyter_server.base.handlers import AuthenticatedFileHandler
from jupyter_server.transutils import _i18n

from .filecheckpoints import AsyncFileCheckpoints, FileCheckpoints
from .fileio import AsyncFileManagerMixin, FileManagerMixin
from .manager import AsyncContentsManager, ContentsManager

try:
    from os.path import samefile
except ImportError:
    # windows + py2
    from jupyter_server.utils import samefile_simple as samefile

_script_exporter = None


class FileContentsManager(FileManagerMixin, ContentsManager):

    root_dir = Unicode(config=True)

    @default("root_dir")
    def _default_root_dir(self):
        try:
            return self.parent.root_dir
        except AttributeError:
            return os.getcwd()

    @validate("root_dir")
    def _validate_root_dir(self, proposal):
        """Do a bit of validation of the root_dir."""
        value = proposal["value"]
        if not os.path.isabs(value):
            # If we receive a non-absolute path, make it absolute.
            value = os.path.abspath(value)
        if not os.path.isdir(value):
            raise TraitError("%r is not a directory" % value)
        return value

    @default("checkpoints_class")
    def _checkpoints_class_default(self):
        return FileCheckpoints

    delete_to_trash = Bool(
        True,
        config=True,
        help="""If True (default), deleting files will send them to the
        platform's trash/recycle bin, where they can be recovered. If False,
        deleting files really deletes them.""",
    )

    always_delete_dir = Bool(
        False,
        config=True,
        help="""If True, deleting a non-empty directory will always be allowed.
        WARNING this may result in files being permanently removed; e.g. on Windows,
        if the data size is too big for the trash/recycle bin the directory will be permanently
        deleted. If False (default), the non-empty directory will be sent to the trash only
        if safe. And if ``delete_to_trash`` is True, the directory won't be deleted.""",
    )

    @default("files_handler_class")
    def _files_handler_class_default(self):
        return AuthenticatedFileHandler

    @default("files_handler_params")
    def _files_handler_params_default(self):
        return {"path": self.root_dir}

    def is_hidden(self, path):
        """Does the API style path correspond to a hidden directory or file?

        Parameters
        ----------
        path : string
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        hidden : bool
            Whether the path exists and is hidden.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        return is_hidden(os_path, self.root_dir)

    def is_writable(self, path):
        """Does the API style path correspond to a writable directory or file?

        Parameters
        ----------
        path : string
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        hidden : bool
            Whether the path exists and is writable.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        try:
            return os.access(os_path, os.W_OK)
        except OSError:
            self.log.error("Failed to check write permissions on %s", os_path)
            return False

    def file_exists(self, path):
        """Returns True if the file exists, else returns False.

        API-style wrapper for os.path.isfile

        Parameters
        ----------
        path : string
            The relative path to the file (with '/' as separator)

        Returns
        -------
        exists : bool
            Whether the file exists.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path)
        return os.path.isfile(os_path)

    def dir_exists(self, path):
        """Does the API-style path refer to an extant directory?

        API-style wrapper for os.path.isdir

        Parameters
        ----------
        path : string
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        exists : bool
            Whether the path is indeed a directory.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        return os.path.isdir(os_path)

    def exists(self, path):
        """Returns True if the path exists, else returns False.

        API-style wrapper for os.path.exists

        Parameters
        ----------
        path : string
            The API path to the file (with '/' as separator)

        Returns
        -------
        exists : bool
            Whether the target exists.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        return exists(os_path)

    def _base_model(self, path):
        """Build the common base of a contents model"""
        os_path = self._get_os_path(path)
        info = os.lstat(os_path)

        four_o_four = "file or directory does not exist: %r" % path

        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            self.log.info("Refusing to serve hidden file or directory %r, via 404 Error", os_path)
            raise web.HTTPError(404, four_o_four)

        try:
            # size of file
            size = info.st_size
        except (ValueError, OSError):
            self.log.warning("Unable to get size.")
            size = None

        try:
            last_modified = tz.utcfromtimestamp(info.st_mtime)
        except (ValueError, OSError):
            # Files can rarely have an invalid timestamp
            # https://github.com/jupyter/notebook/issues/2539
            # https://github.com/jupyter/notebook/issues/2757
            # Use the Unix epoch as a fallback so we don't crash.
            self.log.warning("Invalid mtime %s for %s", info.st_mtime, os_path)
            last_modified = datetime(1970, 1, 1, 0, 0, tzinfo=tz.UTC)

        try:
            created = tz.utcfromtimestamp(info.st_ctime)
        except (ValueError, OSError):  # See above
            self.log.warning("Invalid ctime %s for %s", info.st_ctime, os_path)
            created = datetime(1970, 1, 1, 0, 0, tzinfo=tz.UTC)

        # Create the base model.
        model = {}
        model["name"] = path.rsplit("/", 1)[-1]
        model["path"] = path
        model["last_modified"] = last_modified
        model["created"] = created
        model["content"] = None
        model["format"] = None
        model["mimetype"] = None
        model["size"] = size
        model["writable"] = self.is_writable(path)

        return model

    def _dir_model(self, path, content=True):
        """Build a model for a directory

        if content is requested, will include a listing of the directory
        """
        os_path = self._get_os_path(path)

        four_o_four = "directory does not exist: %r" % path

        if not os.path.isdir(os_path):
            raise web.HTTPError(404, four_o_four)
        elif is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            self.log.info("Refusing to serve hidden directory %r, via 404 Error", os_path)
            raise web.HTTPError(404, four_o_four)

        model = self._base_model(path)
        model["type"] = "directory"
        model["size"] = None
        if content:
            model["content"] = contents = []
            os_dir = self._get_os_path(path)
            for name in os.listdir(os_dir):
                try:
                    os_path = os.path.join(os_dir, name)
                except UnicodeDecodeError as e:
                    self.log.warning("failed to decode filename '%s': %s", name, e)
                    continue

                try:
                    st = os.lstat(os_path)
                except OSError as e:
                    # skip over broken symlinks in listing
                    if e.errno == errno.ENOENT:
                        self.log.warning("%s doesn't exist", os_path)
                    elif e.errno != errno.EACCES:  # Don't provide clues about protected files
                        self.log.warning("Error stat-ing %s: %s", os_path, e)
                    continue

                if (
                    not stat.S_ISLNK(st.st_mode)
                    and not stat.S_ISREG(st.st_mode)
                    and not stat.S_ISDIR(st.st_mode)
                ):
                    self.log.debug("%s not a regular file", os_path)
                    continue

                try:
                    if self.should_list(name):
                        if self.allow_hidden or not is_file_hidden(os_path, stat_res=st):
                            contents.append(self.get(path=f"{path}/{name}", content=False))
                except OSError as e:
                    # ELOOP: recursive symlink, also don't show failure due to permissions
                    if e.errno not in [errno.ELOOP, errno.EACCES]:
                        self.log.warning(
                            "Unknown error checking if file %r is hidden",
                            os_path,
                            exc_info=True,
                        )

            model["format"] = "json"

        return model

    def _file_model(self, path, content=True, format=None):
        """Build a model for a file

        if content is requested, include the file contents.

        format:
          If 'text', the contents will be decoded as UTF-8.
          If 'base64', the raw bytes contents will be encoded as base64.
          If not specified, try to decode as UTF-8, and fall back to base64
        """
        model = self._base_model(path)
        model["type"] = "file"

        os_path = self._get_os_path(path)
        model["mimetype"] = mimetypes.guess_type(os_path)[0]

        if content:
            content, format = self._read_file(os_path, format)
            if model["mimetype"] is None:
                default_mime = {
                    "text": "text/plain",
                    "base64": "application/octet-stream",
                }[format]
                model["mimetype"] = default_mime

            model.update(
                content=content,
                format=format,
            )

        return model

    def _notebook_model(self, path, content=True):
        """Build a notebook model

        if content is requested, the notebook content will be populated
        as a JSON structure (not double-serialized)
        """
        model = self._base_model(path)
        model["type"] = "notebook"
        os_path = self._get_os_path(path)

        if content:
            validation_error: dict = {}
            nb = self._read_notebook(
                os_path, as_version=4, capture_validation_error=validation_error
            )
            self.mark_trusted_cells(nb, path)
            model["content"] = nb
            model["format"] = "json"
            self.validate_notebook_model(model, validation_error)

        return model

    def get(self, path, content=True, type=None, format=None):
        """Takes a path for an entity and returns its model

        Parameters
        ----------
        path : str
            the API path that describes the relative path for the target
        content : bool
            Whether to include the contents in the reply
        type : str, optional
            The requested type - 'file', 'notebook', or 'directory'.
            Will raise HTTPError 400 if the content doesn't match.
        format : str, optional
            The requested format for file contents. 'text' or 'base64'.
            Ignored if this returns a notebook or directory model.

        Returns
        -------
        model : dict
            the contents model. If content=True, returns the contents
            of the file or directory as well.
        """
        path = path.strip("/")
        os_path = self._get_os_path(path)
        four_o_four = "file or directory does not exist: %r" % path

        if not self.exists(path):
            raise web.HTTPError(404, four_o_four)

        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            self.log.info("Refusing to serve hidden file or directory %r, via 404 Error", os_path)
            raise web.HTTPError(404, four_o_four)

        if os.path.isdir(os_path):
            if type not in (None, "directory"):
                raise web.HTTPError(
                    400,
                    f"{path} is a directory, not a {type}",
                    reason="bad type",
                )
            model = self._dir_model(path, content=content)
        elif type == "notebook" or (type is None and path.endswith(".ipynb")):
            model = self._notebook_model(path, content=content)
        else:
            if type == "directory":
                raise web.HTTPError(400, "%s is not a directory" % path, reason="bad type")
            model = self._file_model(path, content=content, format=format)
        return model

    def _save_directory(self, os_path, model, path=""):
        """create a directory"""
        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            raise web.HTTPError(400, "Cannot create directory %r" % os_path)
        if not os.path.exists(os_path):
            with self.perm_to_403():
                os.mkdir(os_path)
        elif not os.path.isdir(os_path):
            raise web.HTTPError(400, "Not a directory: %s" % (os_path))
        else:
            self.log.debug("Directory %r already exists", os_path)

    def save(self, model, path=""):
        """Save the file model and return the model with no content."""
        path = path.strip("/")

        self.run_pre_save_hooks(model=model, path=path)

        if "type" not in model:
            raise web.HTTPError(400, "No file type provided")
        if "content" not in model and model["type"] != "directory":
            raise web.HTTPError(400, "No file content provided")

        os_path = self._get_os_path(path)

        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            raise web.HTTPError(400, f"Cannot create file or directory {os_path!r}")

        self.log.debug("Saving %s", os_path)

        validation_error: dict = {}
        try:
            if model["type"] == "notebook":
                nb = nbformat.from_dict(model["content"])
                self.check_and_sign(nb, path)
                self._save_notebook(os_path, nb, capture_validation_error=validation_error)
                # One checkpoint should always exist for notebooks.
                if not self.checkpoints.list_checkpoints(path):
                    self.create_checkpoint(path)
            elif model["type"] == "file":
                # Missing format will be handled internally by _save_file.
                self._save_file(os_path, model["content"], model.get("format"))
            elif model["type"] == "directory":
                self._save_directory(os_path, model, path)
            else:
                raise web.HTTPError(400, "Unhandled contents type: %s" % model["type"])
        except web.HTTPError:
            raise
        except Exception as e:
            self.log.error("Error while saving file: %s %s", path, e, exc_info=True)
            raise web.HTTPError(500, f"Unexpected error while saving file: {path} {e}") from e

        validation_message = None
        if model["type"] == "notebook":
            self.validate_notebook_model(model, validation_error=validation_error)
            validation_message = model.get("message", None)

        model = self.get(path, content=False)
        if validation_message:
            model["message"] = validation_message

        self.run_post_save_hooks(model=model, os_path=os_path)

        return model

    def delete_file(self, path):
        """Delete file at path."""
        path = path.strip("/")
        os_path = self._get_os_path(path)
        rm = os.unlink

        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            raise web.HTTPError(400, f"Cannot delete file or directory {os_path!r}")

        four_o_four = "file or directory does not exist: %r" % path
        if not self.exists(path):
            raise web.HTTPError(404, four_o_four)

        def _check_trash(os_path):
            if sys.platform in {"win32", "darwin"}:
                return True

            # It's a bit more nuanced than this, but until we can better
            # distinguish errors from send2trash, assume that we can only trash
            # files on the same partition as the home directory.
            file_dev = os.stat(os_path).st_dev
            home_dev = os.stat(os.path.expanduser("~")).st_dev
            return file_dev == home_dev

        def is_non_empty_dir(os_path):
            if os.path.isdir(os_path):
                # A directory containing only leftover checkpoints is
                # considered empty.
                cp_dir = getattr(self.checkpoints, "checkpoint_dir", None)
                if set(os.listdir(os_path)) - {cp_dir}:
                    return True

            return False

        if self.delete_to_trash:
            if not self.always_delete_dir and sys.platform == "win32" and is_non_empty_dir(os_path):
                # send2trash can really delete files on Windows, so disallow
                # deleting non-empty files. See Github issue 3631.
                raise web.HTTPError(400, "Directory %s not empty" % os_path)
            if _check_trash(os_path):
                # Looking at the code in send2trash, I don't think the errors it
                # raises let us distinguish permission errors from other errors in
                # code. So for now, the "look before you leap" approach is used.
                if not self.is_writable(path):
                    raise web.HTTPError(403, "Permission denied: %s" % path)
                self.log.debug("Sending %s to trash", os_path)
                send2trash(os_path)
                return
            else:
                self.log.warning(
                    "Skipping trash for %s, on different device to home directory",
                    os_path,
                )

        if os.path.isdir(os_path):
            # Don't permanently delete non-empty directories.
            if not self.always_delete_dir and is_non_empty_dir(os_path):
                raise web.HTTPError(400, "Directory %s not empty" % os_path)
            self.log.debug("Removing directory %s", os_path)
            with self.perm_to_403():
                shutil.rmtree(os_path)
        else:
            self.log.debug("Unlinking file %s", os_path)
            with self.perm_to_403():
                rm(os_path)

    def rename_file(self, old_path, new_path):
        """Rename a file."""
        old_path = old_path.strip("/")
        new_path = new_path.strip("/")
        if new_path == old_path:
            return

        new_os_path = self._get_os_path(new_path)
        old_os_path = self._get_os_path(old_path)

        if (
            is_hidden(old_os_path, self.root_dir) or is_hidden(new_os_path, self.root_dir)
        ) and not self.allow_hidden:
            raise web.HTTPError(400, f"Cannot rename file or directory {old_os_path!r}")

        # Should we proceed with the move?
        if os.path.exists(new_os_path) and not samefile(old_os_path, new_os_path):
            raise web.HTTPError(409, "File already exists: %s" % new_path)

        # Move the file
        try:
            with self.perm_to_403():
                shutil.move(old_os_path, new_os_path)
        except web.HTTPError:
            raise
        except Exception as e:
            raise web.HTTPError(500, f"Unknown error renaming file: {old_path} {e}") from e

    def info_string(self):
        return _i18n("Serving notebooks from local directory: %s") % self.root_dir

    def get_kernel_path(self, path, model=None):
        """Return the initial API path of  a kernel associated with a given notebook"""
        if self.dir_exists(path):
            return path
        if "/" in path:
            parent_dir = path.rsplit("/", 1)[0]
        else:
            parent_dir = ""
        return parent_dir


class AsyncFileContentsManager(FileContentsManager, AsyncFileManagerMixin, AsyncContentsManager):
    @default("checkpoints_class")
    def _checkpoints_class_default(self):
        return AsyncFileCheckpoints

    async def _dir_model(self, path, content=True):
        """Build a model for a directory

        if content is requested, will include a listing of the directory
        """
        os_path = self._get_os_path(path)

        four_o_four = "directory does not exist: %r" % path

        if not os.path.isdir(os_path):
            raise web.HTTPError(404, four_o_four)
        elif is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            self.log.info("Refusing to serve hidden directory %r, via 404 Error", os_path)
            raise web.HTTPError(404, four_o_four)

        model = self._base_model(path)
        model["type"] = "directory"
        model["size"] = None
        if content:
            model["content"] = contents = []
            os_dir = self._get_os_path(path)
            dir_contents = await run_sync(os.listdir, os_dir)
            for name in dir_contents:
                try:
                    os_path = os.path.join(os_dir, name)
                except UnicodeDecodeError as e:
                    self.log.warning("failed to decode filename '%s': %s", name, e)
                    continue

                try:
                    st = await run_sync(os.lstat, os_path)
                except OSError as e:
                    # skip over broken symlinks in listing
                    if e.errno == errno.ENOENT:
                        self.log.warning("%s doesn't exist", os_path)
                    elif e.errno != errno.EACCES:  # Don't provide clues about protected files
                        self.log.warning("Error stat-ing %s: %s", os_path, e)
                    continue

                if (
                    not stat.S_ISLNK(st.st_mode)
                    and not stat.S_ISREG(st.st_mode)
                    and not stat.S_ISDIR(st.st_mode)
                ):
                    self.log.debug("%s not a regular file", os_path)
                    continue

                try:
                    if self.should_list(name):
                        if self.allow_hidden or not is_file_hidden(os_path, stat_res=st):
                            contents.append(await self.get(path=f"{path}/{name}", content=False))
                except OSError as e:
                    # ELOOP: recursive symlink, also don't show failure due to permissions
                    if e.errno not in [errno.ELOOP, errno.EACCES]:
                        self.log.warning(
                            "Unknown error checking if file %r is hidden",
                            os_path,
                            exc_info=True,
                        )

            model["format"] = "json"

        return model

    async def _file_model(self, path, content=True, format=None):
        """Build a model for a file

        if content is requested, include the file contents.

        format:
          If 'text', the contents will be decoded as UTF-8.
          If 'base64', the raw bytes contents will be encoded as base64.
          If not specified, try to decode as UTF-8, and fall back to base64
        """
        model = self._base_model(path)
        model["type"] = "file"

        os_path = self._get_os_path(path)
        model["mimetype"] = mimetypes.guess_type(os_path)[0]

        if content:
            content, format = await self._read_file(os_path, format)
            if model["mimetype"] is None:
                default_mime = {
                    "text": "text/plain",
                    "base64": "application/octet-stream",
                }[format]
                model["mimetype"] = default_mime

            model.update(
                content=content,
                format=format,
            )

        return model

    async def _notebook_model(self, path, content=True):
        """Build a notebook model

        if content is requested, the notebook content will be populated
        as a JSON structure (not double-serialized)
        """
        model = self._base_model(path)
        model["type"] = "notebook"
        os_path = self._get_os_path(path)

        if content:
            validation_error: dict = {}
            nb = await self._read_notebook(
                os_path, as_version=4, capture_validation_error=validation_error
            )
            self.mark_trusted_cells(nb, path)
            model["content"] = nb
            model["format"] = "json"
            self.validate_notebook_model(model, validation_error)

        return model

    async def get(self, path, content=True, type=None, format=None):
        """Takes a path for an entity and returns its model

        Parameters
        ----------
        path : str
            the API path that describes the relative path for the target
        content : bool
            Whether to include the contents in the reply
        type : str, optional
            The requested type - 'file', 'notebook', or 'directory'.
            Will raise HTTPError 400 if the content doesn't match.
        format : str, optional
            The requested format for file contents. 'text' or 'base64'.
            Ignored if this returns a notebook or directory model.

        Returns
        -------
        model : dict
            the contents model. If content=True, returns the contents
            of the file or directory as well.
        """
        path = path.strip("/")

        if not self.exists(path):
            raise web.HTTPError(404, "No such file or directory: %s" % path)

        os_path = self._get_os_path(path)
        if os.path.isdir(os_path):
            if type not in (None, "directory"):
                raise web.HTTPError(
                    400,
                    f"{path} is a directory, not a {type}",
                    reason="bad type",
                )
            model = await self._dir_model(path, content=content)
        elif type == "notebook" or (type is None and path.endswith(".ipynb")):
            model = await self._notebook_model(path, content=content)
        else:
            if type == "directory":
                raise web.HTTPError(400, "%s is not a directory" % path, reason="bad type")
            model = await self._file_model(path, content=content, format=format)
        return model

    async def _save_directory(self, os_path, model, path=""):
        """create a directory"""
        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            raise web.HTTPError(400, "Cannot create hidden directory %r" % os_path)
        if not os.path.exists(os_path):
            with self.perm_to_403():
                await run_sync(os.mkdir, os_path)
        elif not os.path.isdir(os_path):
            raise web.HTTPError(400, "Not a directory: %s" % (os_path))
        else:
            self.log.debug("Directory %r already exists", os_path)

    async def save(self, model, path=""):
        """Save the file model and return the model with no content."""
        path = path.strip("/")

        self.run_pre_save_hook(model=model, path=path)

        if "type" not in model:
            raise web.HTTPError(400, "No file type provided")
        if "content" not in model and model["type"] != "directory":
            raise web.HTTPError(400, "No file content provided")

        os_path = self._get_os_path(path)
        self.log.debug("Saving %s", os_path)

        validation_error: dict = {}
        try:
            if model["type"] == "notebook":
                nb = nbformat.from_dict(model["content"])
                self.check_and_sign(nb, path)
                await self._save_notebook(os_path, nb, capture_validation_error=validation_error)
                # One checkpoint should always exist for notebooks.
                if not (await self.checkpoints.list_checkpoints(path)):
                    await self.create_checkpoint(path)
            elif model["type"] == "file":
                # Missing format will be handled internally by _save_file.
                await self._save_file(os_path, model["content"], model.get("format"))
            elif model["type"] == "directory":
                await self._save_directory(os_path, model, path)
            else:
                raise web.HTTPError(400, "Unhandled contents type: %s" % model["type"])
        except web.HTTPError:
            raise
        except Exception as e:
            self.log.error("Error while saving file: %s %s", path, e, exc_info=True)
            raise web.HTTPError(500, f"Unexpected error while saving file: {path} {e}") from e

        validation_message = None
        if model["type"] == "notebook":
            self.validate_notebook_model(model, validation_error=validation_error)
            validation_message = model.get("message", None)

        model = await self.get(path, content=False)
        if validation_message:
            model["message"] = validation_message

        self.run_post_save_hooks(model=model, os_path=os_path)

        return model

    async def delete_file(self, path):
        """Delete file at path."""
        path = path.strip("/")
        os_path = self._get_os_path(path)
        rm = os.unlink

        if is_hidden(os_path, self.root_dir) and not self.allow_hidden:
            raise web.HTTPError(400, f"Cannot delete file or directory {os_path!r}")

        if not os.path.exists(os_path):
            raise web.HTTPError(404, "File or directory does not exist: %s" % os_path)

        async def _check_trash(os_path):
            if sys.platform in {"win32", "darwin"}:
                return True

            # It's a bit more nuanced than this, but until we can better
            # distinguish errors from send2trash, assume that we can only trash
            # files on the same partition as the home directory.
            file_dev = (await run_sync(os.stat, os_path)).st_dev
            home_dev = (await run_sync(os.stat, os.path.expanduser("~"))).st_dev
            return file_dev == home_dev

        async def is_non_empty_dir(os_path):
            if os.path.isdir(os_path):
                # A directory containing only leftover checkpoints is
                # considered empty.
                cp_dir = getattr(self.checkpoints, "checkpoint_dir", None)
                dir_contents = set(await run_sync(os.listdir, os_path))
                if dir_contents - {cp_dir}:
                    return True

            return False

        if self.delete_to_trash:
            if (
                not self.always_delete_dir
                and sys.platform == "win32"
                and await is_non_empty_dir(os_path)
            ):
                # send2trash can really delete files on Windows, so disallow
                # deleting non-empty files. See Github issue 3631.
                raise web.HTTPError(400, "Directory %s not empty" % os_path)
            if await _check_trash(os_path):
                # Looking at the code in send2trash, I don't think the errors it
                # raises let us distinguish permission errors from other errors in
                # code. So for now, the "look before you leap" approach is used.
                if not self.is_writable(path):
                    raise web.HTTPError(403, "Permission denied: %s" % path)
                self.log.debug("Sending %s to trash", os_path)
                send2trash(os_path)
                return
            else:
                self.log.warning(
                    "Skipping trash for %s, on different device to home directory",
                    os_path,
                )

        if os.path.isdir(os_path):
            # Don't permanently delete non-empty directories.
            if not self.always_delete_dir and await is_non_empty_dir(os_path):
                raise web.HTTPError(400, "Directory %s not empty" % os_path)
            self.log.debug("Removing directory %s", os_path)
            with self.perm_to_403():
                await run_sync(shutil.rmtree, os_path)
        else:
            self.log.debug("Unlinking file %s", os_path)
            with self.perm_to_403():
                await run_sync(rm, os_path)

    async def rename_file(self, old_path, new_path):
        """Rename a file."""
        old_path = old_path.strip("/")
        new_path = new_path.strip("/")
        if new_path == old_path:
            return

        new_os_path = self._get_os_path(new_path)
        old_os_path = self._get_os_path(old_path)

        if (
            is_hidden(old_os_path, self.root_dir) or is_hidden(new_os_path, self.root_dir)
        ) and not self.allow_hidden:
            raise web.HTTPError(400, f"Cannot rename file or directory {old_os_path!r}")

        # Should we proceed with the move?
        if os.path.exists(new_os_path) and not samefile(old_os_path, new_os_path):
            raise web.HTTPError(409, "File already exists: %s" % new_path)

        # Move the file
        try:
            with self.perm_to_403():
                await run_sync(shutil.move, old_os_path, new_os_path)
        except web.HTTPError:
            raise
        except Exception as e:
            raise web.HTTPError(500, f"Unknown error renaming file: {old_path} {e}") from e

    async def dir_exists(self, path):
        """Does a directory exist at the given path"""
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        return os.path.isdir(os_path)

    async def file_exists(self, path):
        """Does a file exist at the given path"""
        path = path.strip("/")
        os_path = self._get_os_path(path)
        return os.path.isfile(os_path)

    async def is_hidden(self, path):
        """Is path a hidden directory or file"""
        path = path.strip("/")
        os_path = self._get_os_path(path=path)
        return is_hidden(os_path, self.root_dir)

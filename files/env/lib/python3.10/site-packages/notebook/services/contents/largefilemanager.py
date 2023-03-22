from notebook.services.contents.filemanager import FileContentsManager
from tornado import web
import base64
import os

class LargeFileManager(FileContentsManager):
    """Handle large file upload."""

    def save(self, model, path=''):
        """Save the file model and return the model with no content."""
        chunk = model.get('chunk', None)
        if chunk is not None:
            path = path.strip('/')

            if 'type' not in model:
                raise web.HTTPError(400, 'No file type provided')
            if model['type'] != 'file':
                raise web.HTTPError(400, f'File type "{model["type"]}" is not supported for large file transfer')
            if 'content' not in model and model['type'] != 'directory':
                raise web.HTTPError(400, 'No file content provided')

            os_path = self._get_os_path(path)

            try:
                if chunk == 1:
                    self.log.debug("Saving %s", os_path)
                    self.run_pre_save_hook(model=model, path=path)
                    super()._save_file(os_path, model['content'], model.get('format'))
                else:
                    self._save_large_file(os_path, model['content'], model.get('format'))
            except web.HTTPError:
                raise
            except Exception as e:
                self.log.error('Error while saving file: %s %s', path, e, exc_info=True)
                raise web.HTTPError(500, f'Unexpected error while saving file: {path} {e}') from e

            model = self.get(path, content=False)

            # Last chunk
            if chunk == -1:
                self.run_post_save_hook(model=model, os_path=os_path)
            return model
        else:
            return super().save(model, path)

    def _save_large_file(self, os_path, content, format):
        """Save content of a generic file."""
        if format not in {'text', 'base64'}:
            raise web.HTTPError(
                400,
                "Must specify format of file contents as 'text' or 'base64'",
            )
        try:
            if format == 'text':
                bcontent = content.encode('utf8')
            else:
                b64_bytes = content.encode('ascii')
                bcontent = base64.b64decode(b64_bytes)
        except Exception as e:
            raise web.HTTPError(
                400, f'Encoding error saving {os_path}: {e}'
            ) from e

        with self.perm_to_403(os_path):
            if os.path.islink(os_path):
                os_path = os.path.join(os.path.dirname(os_path), os.readlink(os_path))
            with open(os_path, 'ab') as f:
                f.write(bcontent)

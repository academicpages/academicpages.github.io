"""
Classes for managing Checkpoints.
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado.web import HTTPError

from traitlets.config.configurable import LoggingConfigurable


class Checkpoints(LoggingConfigurable):
    """
    Base class for managing checkpoints for a ContentsManager.

    Subclasses are required to implement:

    create_checkpoint(self, contents_mgr, path)
    restore_checkpoint(self, contents_mgr, checkpoint_id, path)
    rename_checkpoint(self, checkpoint_id, old_path, new_path)
    delete_checkpoint(self, checkpoint_id, path)
    list_checkpoints(self, path)
    """
    def create_checkpoint(self, contents_mgr, path):
        """Create a checkpoint."""
        raise NotImplementedError("must be implemented in a subclass")

    def restore_checkpoint(self, contents_mgr, checkpoint_id, path):
        """Restore a checkpoint"""
        raise NotImplementedError("must be implemented in a subclass")

    def rename_checkpoint(self, checkpoint_id, old_path, new_path):
        """Rename a single checkpoint from old_path to new_path."""
        raise NotImplementedError("must be implemented in a subclass")

    def delete_checkpoint(self, checkpoint_id, path):
        """delete a checkpoint for a file"""
        raise NotImplementedError("must be implemented in a subclass")

    def list_checkpoints(self, path):
        """Return a list of checkpoints for a given file"""
        raise NotImplementedError("must be implemented in a subclass")

    def rename_all_checkpoints(self, old_path, new_path):
        """Rename all checkpoints for old_path to new_path."""
        for cp in self.list_checkpoints(old_path):
            self.rename_checkpoint(cp['id'], old_path, new_path)

    def delete_all_checkpoints(self, path):
        """Delete all checkpoints for the given path."""
        for checkpoint in self.list_checkpoints(path):
            self.delete_checkpoint(checkpoint['id'], path)


class GenericCheckpointsMixin:
    """
    Helper for creating Checkpoints subclasses that can be used with any
    ContentsManager.

    Provides a ContentsManager-agnostic implementation of `create_checkpoint`
    and `restore_checkpoint` in terms of the following operations:

    - create_file_checkpoint(self, content, format, path)
    - create_notebook_checkpoint(self, nb, path)
    - get_file_checkpoint(self, checkpoint_id, path)
    - get_notebook_checkpoint(self, checkpoint_id, path)

    To create a generic CheckpointManager, add this mixin to a class that
    implement the above four methods plus the remaining Checkpoints API
    methods:

    - delete_checkpoint(self, checkpoint_id, path)
    - list_checkpoints(self, path)
    - rename_checkpoint(self, checkpoint_id, old_path, new_path)
    """

    def create_checkpoint(self, contents_mgr, path):
        model = contents_mgr.get(path, content=True)
        type = model['type']
        if type == 'notebook':
            return self.create_notebook_checkpoint(
                model['content'],
                path,
            )
        elif type == 'file':
            return self.create_file_checkpoint(
                model['content'],
                model['format'],
                path,
            )
        else:
            raise HTTPError(500, f'Unexpected type {type}')

    def restore_checkpoint(self, contents_mgr, checkpoint_id, path):
        """Restore a checkpoint."""
        type = contents_mgr.get(path, content=False)['type']
        if type == 'notebook':
            model = self.get_notebook_checkpoint(checkpoint_id, path)
        elif type == 'file':
            model = self.get_file_checkpoint(checkpoint_id, path)
        else:
            raise HTTPError(500, f'Unexpected type {type}')
        contents_mgr.save(model, path)

    # Required Methods
    def create_file_checkpoint(self, content, format, path):
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
        raise NotImplementedError("must be implemented in a subclass")

    def create_notebook_checkpoint(self, nb, path):
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
        raise NotImplementedError("must be implemented in a subclass")

    def get_file_checkpoint(self, checkpoint_id, path):
        """Get the content of a checkpoint for a non-notebook file.

         Returns a dict of the form:
         {
             'type': 'file',
             'content': <str>,
             'format': {'text','base64'},
         }
        """
        raise NotImplementedError("must be implemented in a subclass")

    def get_notebook_checkpoint(self, checkpoint_id, path):
        """Get the content of a checkpoint for a notebook.

        Returns a dict of the form:
        {
            'type': 'notebook',
            'content': <output of nbformat.read>,
        }
        """
        raise NotImplementedError("must be implemented in a subclass")

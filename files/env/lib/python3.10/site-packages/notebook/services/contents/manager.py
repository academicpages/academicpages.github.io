"""A base class for contents managers."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from fnmatch import fnmatch
import itertools
import json
import os
import re

from tornado.web import HTTPError, RequestHandler

from ...files.handlers import FilesHandler
from .checkpoints import Checkpoints
from traitlets.config.configurable import LoggingConfigurable
from nbformat import sign, validate as validate_nb, ValidationError
from nbformat.v4 import new_notebook
from ipython_genutils.importstring import import_item
from traitlets import (
    Any,
    Bool,
    Dict,
    Instance,
    List,
    TraitError,
    Type,
    Unicode,
    validate,
    default,
)
from ipython_genutils.py3compat import string_types
from notebook.base.handlers import IPythonHandler
from notebook.transutils import _


copy_pat = re.compile(r'\-Copy\d*\.')


class ContentsManager(LoggingConfigurable):
    """Base class for serving files and directories.

    This serves any text or binary file,
    as well as directories,
    with special handling for JSON notebook documents.

    Most APIs take a path argument,
    which is always an API-style unicode path,
    and always refers to a directory.

    - unicode, not url-escaped
    - '/'-separated
    - leading and trailing '/' will be stripped
    - if unspecified, path defaults to '',
      indicating the root path.

    """

    root_dir = Unicode('/', config=True)

    allow_hidden = Bool(False, config=True, help="Allow access to hidden files")

    notary = Instance(sign.NotebookNotary)
    def _notary_default(self):
        return sign.NotebookNotary(parent=self)

    hide_globs = List(Unicode(), [
            '__pycache__', '*.pyc', '*.pyo',
            '.DS_Store', '*.so', '*.dylib', '*~',
        ], config=True, help="""
        Glob patterns to hide in file and directory listings.
    """)

    untitled_notebook = Unicode(_("Untitled"), config=True,
        help="The base name used when creating untitled notebooks."
    )

    untitled_file = Unicode("untitled", config=True,
        help="The base name used when creating untitled files."
    )

    untitled_directory = Unicode("Untitled Folder", config=True,
        help="The base name used when creating untitled directories."
    )

    pre_save_hook = Any(None, config=True, allow_none=True,
        help="""Python callable or importstring thereof

        To be called on a contents model prior to save.

        This can be used to process the structure,
        such as removing notebook outputs or other side effects that
        should not be saved.

        It will be called as (all arguments passed by keyword)::

            hook(path=path, model=model, contents_manager=self)

        - model: the model to be saved. Includes file contents.
          Modifying this dict will affect the file that is stored.
        - path: the API path of the save destination
        - contents_manager: this ContentsManager instance
        """
    )

    @validate('pre_save_hook')
    def _validate_pre_save_hook(self, proposal):
        value = proposal['value']
        if isinstance(value, string_types):
            value = import_item(self.pre_save_hook)
        if not callable(value):
            raise TraitError("pre_save_hook must be callable")
        return value

    def run_pre_save_hook(self, model, path, **kwargs):
        """Run the pre-save hook if defined, and log errors"""
        if self.pre_save_hook:
            try:
                self.log.debug("Running pre-save hook on %s", path)
                self.pre_save_hook(model=model, path=path, contents_manager=self, **kwargs)
            except Exception:
                self.log.error("Pre-save hook failed on %s", path, exc_info=True)

    checkpoints_class = Type(Checkpoints, config=True)
    checkpoints = Instance(Checkpoints, config=True)
    checkpoints_kwargs = Dict(config=True)

    @default('checkpoints')
    def _default_checkpoints(self):
        return self.checkpoints_class(**self.checkpoints_kwargs)

    @default('checkpoints_kwargs')
    def _default_checkpoints_kwargs(self):
        return dict(
            parent=self,
            log=self.log,
        )

    files_handler_class = Type(
        FilesHandler, klass=RequestHandler, allow_none=True, config=True,
        help="""handler class to use when serving raw file requests.

        Default is a fallback that talks to the ContentsManager API,
        which may be inefficient, especially for large files.

        Local files-based ContentsManagers can use a StaticFileHandler subclass,
        which will be much more efficient.

        Access to these files should be Authenticated.
        """
    )

    files_handler_params = Dict(
        config=True,
        help="""Extra parameters to pass to files_handler_class.

        For example, StaticFileHandlers generally expect a `path` argument
        specifying the root directory from which to serve files.
        """
    )

    def get_extra_handlers(self):
        """Return additional handlers

        Default: self.files_handler_class on /files/.*
        """
        handlers = []
        if self.files_handler_class:
            handlers.append(
                (r"/files/(.*)", self.files_handler_class, self.files_handler_params)
            )
        return handlers

    # ContentsManager API part 1: methods that must be
    # implemented in subclasses.

    def dir_exists(self, path):
        """Does a directory exist at the given path?

        Like os.path.isdir

        Override this method in subclasses.

        Parameters
        ----------
        path : string
            The path to check

        Returns
        -------
        exists : bool
            Whether the path does indeed exist.
        """
        raise NotImplementedError

    def is_hidden(self, path):
        """Is path a hidden directory or file?

        Parameters
        ----------
        path : string
            The path to check. This is an API path (`/` separated,
            relative to root dir).

        Returns
        -------
        hidden : bool
            Whether the path is hidden.

        """
        raise NotImplementedError

    def file_exists(self, path=''):
        """Does a file exist at the given path?

        Like os.path.isfile

        Override this method in subclasses.

        Parameters
        ----------
        path : string
            The API path of a file to check for.

        Returns
        -------
        exists : bool
            Whether the file exists.
        """
        raise NotImplementedError('must be implemented in a subclass')

    def exists(self, path):
        """Does a file or directory exist at the given path?

        Like os.path.exists

        Parameters
        ----------
        path : string
            The API path of a file or directory to check for.

        Returns
        -------
        exists : bool
            Whether the target exists.
        """
        return self.file_exists(path) or self.dir_exists(path)

    def get(self, path, content=True, type=None, format=None):
        """Get a file or directory model."""
        raise NotImplementedError('must be implemented in a subclass')

    def save(self, model, path):
        """
        Save a file or directory model to path.

        Should return the saved model with no content.  Save implementations
        should call self.run_pre_save_hook(model=model, path=path) prior to
        writing any data.
        """
        raise NotImplementedError('must be implemented in a subclass')

    def delete_file(self, path):
        """Delete the file or directory at path."""
        raise NotImplementedError('must be implemented in a subclass')

    def rename_file(self, old_path, new_path):
        """Rename a file or directory."""
        raise NotImplementedError('must be implemented in a subclass')

    # ContentsManager API part 2: methods that have useable default
    # implementations, but can be overridden in subclasses.

    def delete(self, path):
        """Delete a file/directory and any associated checkpoints."""
        path = path.strip('/')
        if not path:
            raise HTTPError(400, "Can't delete root")
        self.delete_file(path)
        self.checkpoints.delete_all_checkpoints(path)

    def rename(self, old_path, new_path):
        """Rename a file and any checkpoints associated with that file."""
        self.rename_file(old_path, new_path)
        self.checkpoints.rename_all_checkpoints(old_path, new_path)

    def update(self, model, path):
        """Update the file's path

        For use in PATCH requests, to enable renaming a file without
        re-uploading its contents. Only used for renaming at the moment.
        """
        path = path.strip('/')
        new_path = model.get('path', path).strip('/')
        if path != new_path:
            self.rename(path, new_path)
        model = self.get(new_path, content=False)
        return model

    def info_string(self):
        return "Serving contents"

    def get_kernel_path(self, path, model=None):
        """Return the API path for the kernel

        KernelManagers can turn this value into a filesystem path,
        or ignore it altogether.

        The default value here will start kernels in the directory of the
        notebook server. FileContentsManager overrides this to use the
        directory containing the notebook.
        """
        return ''

    def increment_filename(self, filename, path='', insert=''):
        """Increment a filename until it is unique.

        Parameters
        ----------
        filename : unicode
            The name of a file, including extension
        path : unicode
            The API path of the target's directory
        insert: unicode
            The characters to insert after the base filename

        Returns
        -------
        name : unicode
            A filename that is unique, based on the input filename.
        """
        # Extract the full suffix from the filename (e.g. .tar.gz)
        path = path.strip('/')
        basename, dot, ext = filename.rpartition('.')
        if ext != 'ipynb':
                basename, dot, ext = filename.partition('.')

        suffix = dot + ext

        for i in itertools.count():
            if i:
                insert_i = f'{insert}{i}'
            else:
                insert_i = ''
            name = f'{basename}{insert_i}{suffix}'
            if not self.exists(f'{path}/{name}'):
                break
        return name

    def validate_notebook_model(self, model):
        """Add failed-validation message to model"""
        try:
            validate_nb(model['content'])
        except ValidationError as e:
            model['message'] = f'Notebook validation failed: {e.message}:\n' \
                               f'{json.dumps(e.instance, indent=1, default=lambda obj: "<UNKNOWN>")}'
        return model

    def new_untitled(self, path='', type='', ext=''):
        """Create a new untitled file or directory in path

        path must be a directory

        File extension can be specified.

        Use `new` to create files with a fully specified path (including filename).
        """
        path = path.strip('/')
        if not self.dir_exists(path):
            raise HTTPError(404, f'No such directory: {path}')

        model = {}
        if type:
            model['type'] = type

        if ext == '.ipynb':
            model.setdefault('type', 'notebook')
        else:
            model.setdefault('type', 'file')

        insert = ''
        if model['type'] == 'directory':
            untitled = self.untitled_directory
            insert = ' '
        elif model['type'] == 'notebook':
            untitled = self.untitled_notebook
            ext = '.ipynb'
        elif model['type'] == 'file':
            untitled = self.untitled_file
        else:
            raise HTTPError(400, f"Unexpected model type: {model['type']!r}")

        name = self.increment_filename(untitled + ext, path, insert=insert)
        path = f'{path}/{name}'
        return self.new(model, path)

    def new(self, model=None, path=''):
        """Create a new file or directory and return its model with no content.

        To create a new untitled entity in a directory, use `new_untitled`.
        """
        path = path.strip('/')
        if model is None:
            model = {}

        if path.endswith('.ipynb'):
            model.setdefault('type', 'notebook')
        else:
            model.setdefault('type', 'file')

        # no content, not a directory, so fill out new-file model
        if 'content' not in model and model['type'] != 'directory':
            if model['type'] == 'notebook':
                model['content'] = new_notebook()
                model['format'] = 'json'
            else:
                model['content'] = ''
                model['type'] = 'file'
                model['format'] = 'text'

        model = self.save(model, path)
        return model

    def copy(self, from_path, to_path=None):
        """Copy an existing file and return its new model.

        If to_path not specified, it will be the parent directory of from_path.
        If to_path is a directory, filename will increment `from_path-Copy#.ext`.
        Considering multi-part extensions, the Copy# part will be placed before the first dot for all the extensions except `ipynb`.
        For easier manual searching in case of notebooks, the Copy# part will be placed before the last dot.

        from_path must be a full path to a file.
        """
        path = from_path.strip('/')
        if to_path is not None:
            to_path = to_path.strip('/')

        if '/' in path:
            from_dir, from_name = path.rsplit('/', 1)
        else:
            from_dir = ''
            from_name = path

        model = self.get(path)
        model.pop('path', None)
        model.pop('name', None)
        if model['type'] == 'directory':
            raise HTTPError(400, "Can't copy directories")

        if to_path is None:
            to_path = from_dir
        if self.dir_exists(to_path):
            name = copy_pat.sub('.', from_name)
            to_name = self.increment_filename(name, to_path, insert='-Copy')
            to_path = f'{to_path}/{to_name}'

        model = self.save(model, to_path)
        return model

    def log_info(self):
        self.log.info(self.info_string())

    def trust_notebook(self, path):
        """Explicitly trust a notebook

        Parameters
        ----------
        path : string
            The path of a notebook
        """
        model = self.get(path)
        nb = model['content']
        self.log.warning("Trusting notebook %s", path)
        self.notary.mark_cells(nb, True)
        self.check_and_sign(nb, path)

    def check_and_sign(self, nb, path=''):
        """Check for trusted cells, and sign the notebook.

        Called as a part of saving notebooks.

        Parameters
        ----------
        nb : dict
            The notebook dict
        path : string
            The notebook's path (for logging)
        """
        if self.notary.check_cells(nb):
            self.notary.sign(nb)
        else:
            self.log.warning("Notebook %s is not trusted", path)

    def mark_trusted_cells(self, nb, path=''):
        """Mark cells as trusted if the notebook signature matches.

        Called as a part of loading notebooks.

        Parameters
        ----------
        nb : dict
            The notebook object (in current nbformat)
        path : string
            The notebook's path (for logging)
        """
        trusted = self.notary.check_signature(nb)
        if not trusted:
            self.log.warning("Notebook %s is not trusted", path)
        self.notary.mark_cells(nb, trusted)

    def should_list(self, name):
        """Should this file/directory name be displayed in a listing?"""
        return not any(fnmatch(name, glob) for glob in self.hide_globs)

    # Part 3: Checkpoints API
    def create_checkpoint(self, path):
        """Create a checkpoint."""
        return self.checkpoints.create_checkpoint(self, path)

    def restore_checkpoint(self, checkpoint_id, path):
        """
        Restore a checkpoint.
        """
        self.checkpoints.restore_checkpoint(self, checkpoint_id, path)

    def list_checkpoints(self, path):
        return self.checkpoints.list_checkpoints(path)

    def delete_checkpoint(self, checkpoint_id, path):
        return self.checkpoints.delete_checkpoint(checkpoint_id, path)

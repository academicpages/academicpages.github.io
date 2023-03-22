"""A base class session manager."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import uuid

try:
    import sqlite3
except ImportError:
    # fallback on pysqlite2 if Python was build without sqlite
    from pysqlite2 import dbapi2 as sqlite3

from tornado import gen, web

from traitlets.config.configurable import LoggingConfigurable
from ipython_genutils.py3compat import unicode_type
from traitlets import Instance

from notebook.utils import maybe_future
from notebook.traittypes import InstanceFromClasses

class SessionManager(LoggingConfigurable):

    kernel_manager = Instance('notebook.services.kernels.kernelmanager.MappingKernelManager')
    contents_manager = InstanceFromClasses(
        klasses=[
            'notebook.services.contents.manager.ContentsManager',
            # To make custom ContentsManagers both forward+backward
            # compatible, we'll relax the strictness of this trait
            # and allow jupyter_server contents managers to pass
            # through. If jupyter_server is not installed, this class
            # will be ignored.
            'jupyter_server.services.contents.manager.ContentsManager'
        ]
    )

    # Session database initialized below
    _cursor = None
    _connection = None
    _columns = {'session_id', 'path', 'name', 'type', 'kernel_id'}

    @property
    def cursor(self):
        """Start a cursor and create a database called 'session'"""
        if self._cursor is None:
            self._cursor = self.connection.cursor()
            self._cursor.execute("""CREATE TABLE session
                (session_id, path, name, type, kernel_id)""")
        return self._cursor

    @property
    def connection(self):
        """Start a database connection"""
        if self._connection is None:
            self._connection = sqlite3.connect(':memory:')
            self._connection.row_factory = sqlite3.Row
        return self._connection

    def close(self):
        """Close the sqlite connection"""
        if self._cursor is not None:
            self._cursor.close()
            self._cursor = None

    def __del__(self):
        """Close connection once SessionManager closes"""
        self.close()

    @gen.coroutine
    def session_exists(self, path):
        """Check to see if the session of a given name exists"""
        exists = False
        self.cursor.execute("SELECT * FROM session WHERE path=?", (path,))
        row = self.cursor.fetchone()
        if row is not None:
            # Note, although we found a row for the session, the associated kernel may have
            # been culled or died unexpectedly.  If that's the case, we should delete the
            # row, thereby terminating the session.  This can be done via a call to
            # row_to_model that tolerates that condition.  If row_to_model returns None,
            # we'll return false, since, at that point, the session doesn't exist anyway.
            model = yield maybe_future(self.row_to_model(row, tolerate_culled=True))
            if model is not None:
                exists = True
        raise gen.Return(exists)

    def new_session_id(self):
        "Create a uuid for a new session"
        return unicode_type(uuid.uuid4())

    @gen.coroutine
    def create_session(self, path=None, name=None, type=None, kernel_name=None, kernel_id=None):
        """Creates a session and returns its model"""
        session_id = self.new_session_id()
        if kernel_id is not None and kernel_id in self.kernel_manager:
            pass
        else:
            kernel_id = yield self.start_kernel_for_session(session_id, path, name, type, kernel_name)
        result = yield maybe_future(
            self.save_session(session_id, path=path, name=name, type=type, kernel_id=kernel_id)
        )
        # py2-compat
        raise gen.Return(result)

    @gen.coroutine
    def start_kernel_for_session(self, session_id, path, name, type, kernel_name):
        """Start a new kernel for a given session."""
        # allow contents manager to specify kernels cwd
        kernel_path = self.contents_manager.get_kernel_path(path=path)
        kernel_id = yield maybe_future(
            self.kernel_manager.start_kernel(path=kernel_path, kernel_name=kernel_name)
        )
        # py2-compat
        raise gen.Return(kernel_id)

    @gen.coroutine
    def save_session(self, session_id, path=None, name=None, type=None, kernel_id=None):
        """Saves the items for the session with the given session_id

        Given a session_id (and any other of the arguments), this method
        creates a row in the sqlite session database that holds the information
        for a session.

        Parameters
        ----------
        session_id : str
            uuid for the session; this method must be given a session_id
        path : str
            the path for the given session
        name: str
            the name of the session
        type: string
            the type of the session
        kernel_id : str
            a uuid for the kernel associated with this session

        Returns
        -------
        model : dict
            a dictionary of the session model
        """
        self.cursor.execute("INSERT INTO session VALUES (?,?,?,?,?)",
            (session_id, path, name, type, kernel_id)
        )
        result = yield maybe_future(self.get_session(session_id=session_id))
        raise gen.Return(result)

    @gen.coroutine
    def get_session(self, **kwargs):
        """Returns the model for a particular session.

        Takes a keyword argument and searches for the value in the session
        database, then returns the rest of the session's info.

        Parameters
        ----------
        **kwargs : keyword argument
            must be given one of the keywords and values from the session database
            (i.e. session_id, path, name, type, kernel_id)

        Returns
        -------
        model : dict
            returns a dictionary that includes all the information from the
            session described by the kwarg.
        """
        if not kwargs:
            raise TypeError("must specify a column to query")

        conditions = []
        for column in kwargs.keys():
            if column not in self._columns:
                raise TypeError("No such column: %r", column)
            conditions.append(f"{column}=?")

        query = f"SELECT * FROM session WHERE {' AND '.join(conditions)}"

        self.cursor.execute(query, list(kwargs.values()))
        try:
            row = self.cursor.fetchone()
        except KeyError:
            # The kernel is missing, so the session just got deleted.
            row = None

        if row is None:
            q = []
            for key, value in kwargs.items():
                q.append(f"{key}={value!r}")

            raise web.HTTPError(404, f'Session not found: {", ".join(q)}')

        try:
            model = yield maybe_future(self.row_to_model(row))
        except KeyError as e:
            raise web.HTTPError(404, f'Session not found: {e}')
        raise gen.Return(model)

    @gen.coroutine
    def update_session(self, session_id, **kwargs):
        """Updates the values in the session database.

        Changes the values of the session with the given session_id
        with the values from the keyword arguments.

        Parameters
        ----------
        session_id : str
            a uuid that identifies a session in the sqlite3 database
        **kwargs : str
            the key must correspond to a column title in session database,
            and the value replaces the current value in the session
            with session_id.
        """
        yield maybe_future(self.get_session(session_id=session_id))

        if not kwargs:
            # no changes
            return

        sets = []
        for column in kwargs.keys():
            if column not in self._columns:
                raise TypeError(f"No such column: {column!r}")
            sets.append(f"{column}=?")
        query = f"UPDATE session SET {', '.join(sets)} WHERE session_id=?"
        self.cursor.execute(query, list(kwargs.values()) + [session_id])

    def kernel_culled(self, kernel_id):
        """Checks if the kernel is still considered alive and returns true if its not found. """
        return kernel_id not in self.kernel_manager

    @gen.coroutine
    def row_to_model(self, row, tolerate_culled=False):
        """Takes sqlite database session row and turns it into a dictionary"""
        kernel_culled = yield maybe_future(self.kernel_culled(row['kernel_id']))
        if kernel_culled:
            # The kernel was culled or died without deleting the session.
            # We can't use delete_session here because that tries to find
            # and shut down the kernel - so we'll delete the row directly.
            #
            # If caller wishes to tolerate culled kernels, log a warning
            # and return None.  Otherwise, raise KeyError with a similar
            # message.
            self.cursor.execute("DELETE FROM session WHERE session_id=?",
                                (row['session_id'],))
            msg = "Kernel '{kernel_id}' appears to have been culled or died unexpectedly, " \
                  "invalidating session '{session_id}'. The session has been removed.".\
                format(kernel_id=row['kernel_id'],session_id=row['session_id'])
            if tolerate_culled:
                self.log.warning(msg + "  Continuing...")
                raise gen.Return(None)
            raise KeyError(msg)

        kernel_model = yield maybe_future(self.kernel_manager.kernel_model(row['kernel_id']))
        model = {
            'id': row['session_id'],
            'path': row['path'],
            'name': row['name'],
            'type': row['type'],
            'kernel': kernel_model
        }
        if row['type'] == 'notebook':
            # Provide the deprecated API.
            model['notebook'] = {'path': row['path'], 'name': row['name']}
        raise gen.Return(model)

    @gen.coroutine
    def list_sessions(self):
        """Returns a list of dictionaries containing all the information from
        the session database"""
        c = self.cursor.execute("SELECT * FROM session")
        result = []
        # We need to use fetchall() here, because row_to_model can delete rows,
        # which messes up the cursor if we're iterating over rows.
        for row in c.fetchall():
            try:
                model = yield maybe_future(self.row_to_model(row))
                result.append(model)
            except KeyError:
                pass
        raise gen.Return(result)

    @gen.coroutine
    def delete_session(self, session_id):
        """Deletes the row in the session database with given session_id"""
        session = yield maybe_future(self.get_session(session_id=session_id))
        yield maybe_future(self.kernel_manager.shutdown_kernel(session['kernel']['id']))
        self.cursor.execute("DELETE FROM session WHERE session_id=?", (session_id,))

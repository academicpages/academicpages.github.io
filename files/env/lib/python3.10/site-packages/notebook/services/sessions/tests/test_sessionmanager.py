"""Tests for the session manager."""

from functools import partial
from unittest import TestCase

from tornado import gen, web
from tornado.ioloop import IOLoop

from ..sessionmanager import SessionManager
from notebook.services.kernels.kernelmanager import MappingKernelManager
from notebook.services.contents.manager import ContentsManager
from notebook._tz import utcnow, isoformat

class DummyKernel:
    def __init__(self, kernel_name='python'):
        self.kernel_name = kernel_name

dummy_date = utcnow()
dummy_date_s = isoformat(dummy_date)

class DummyMKM(MappingKernelManager):
    """MappingKernelManager interface that doesn't start kernels, for testing"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_letters = iter('ABCDEFGHIJK')

    def _new_id(self):
        return next(self.id_letters)

    def start_kernel(self, kernel_id=None, path=None, kernel_name='python', **kwargs):
        kernel_id = kernel_id or self._new_id()
        k = self._kernels[kernel_id] = DummyKernel(kernel_name=kernel_name)
        self._kernel_connections[kernel_id] = 0
        k.last_activity = dummy_date
        k.execution_state = 'idle'
        return kernel_id

    def shutdown_kernel(self, kernel_id, now=False):
        del self._kernels[kernel_id]


class TestSessionManager(TestCase):

    def setUp(self):
        self.sm = SessionManager(
            kernel_manager=DummyMKM(),
            contents_manager=ContentsManager(),
        )
        self.loop = IOLoop()
        self.addCleanup(partial(self.loop.close, all_fds=True))

    def create_sessions(self, *kwarg_list):
        @gen.coroutine
        def co_add():
            sessions = []
            for kwargs in kwarg_list:
                kwargs.setdefault('type', 'notebook')
                session = yield self.sm.create_session(**kwargs)
                sessions.append(session)
            raise gen.Return(sessions)
        return self.loop.run_sync(co_add)

    def create_session(self, **kwargs):
        return self.create_sessions(kwargs)[0]

    def test_get_session(self):
        sm = self.sm
        session_id = self.create_session(path='/path/to/test.ipynb', kernel_name='bar')['id']
        model = self.loop.run_sync(lambda: sm.get_session(session_id=session_id))
        expected = {'id':session_id,
                    'path': '/path/to/test.ipynb',
                    'notebook': {'path': '/path/to/test.ipynb', 'name': None},
                    'type': 'notebook',
                    'name': None,
                    'kernel': {
                        'id': 'A',
                        'name': 'bar',
                        'connections': 0,
                        'last_activity': dummy_date_s,
                        'execution_state': 'idle',
                    }}
        self.assertEqual(model, expected)

    def test_bad_get_session(self):
        # Should raise error if a bad key is passed to the database.
        sm = self.sm
        session_id = self.create_session(path='/path/to/test.ipynb',
                                       kernel_name='foo')['id']
        with self.assertRaises(TypeError):
            self.loop.run_sync(lambda: sm.get_session(bad_id=session_id)) # Bad keyword

    def test_get_session_dead_kernel(self):
        sm = self.sm
        session = self.create_session(path='/path/to/1/test1.ipynb', kernel_name='python')
        # kill the kernel
        sm.kernel_manager.shutdown_kernel(session['kernel']['id'])
        with self.assertRaises(web.HTTPError):
            self.loop.run_sync(lambda: sm.get_session(session_id=session['id']))
        # no sessions left
        listed = self.loop.run_sync(lambda: sm.list_sessions())
        self.assertEqual(listed, [])

    def test_list_sessions(self):
        sm = self.sm
        sessions = self.create_sessions(
            {'path': '/path/to/1/test1.ipynb', 'kernel_name': 'python'},
            {'path': '/path/to/2/test2.py', 'type': 'file', 'kernel_name': 'python'},
            {'path': '/path/to/3', 'name': 'foo', 'type': 'console', 'kernel_name': 'python'},
        )

        sessions = self.loop.run_sync(lambda: sm.list_sessions())
        expected = [
            {
                'id':sessions[0]['id'],
                'path': '/path/to/1/test1.ipynb',
                'type': 'notebook',
                'notebook': {'path': '/path/to/1/test1.ipynb', 'name': None},
                'name': None,
                'kernel': {
                    'id': 'A',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }, {
                'id':sessions[1]['id'],
                'path': '/path/to/2/test2.py',
                'type': 'file',
                'name': None,
                'kernel': {
                    'id': 'B',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }, {
                'id':sessions[2]['id'],
                'path': '/path/to/3',
                'type': 'console',
                'name': 'foo',
                'kernel': {
                    'id': 'C',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }
        ]
        self.assertEqual(sessions, expected)

    def test_list_sessions_dead_kernel(self):
        sm = self.sm
        sessions = self.create_sessions(
            dict(path='/path/to/1/test1.ipynb', kernel_name='python'),
            dict(path='/path/to/2/test2.ipynb', kernel_name='python'),
        )
        # kill one of the kernels
        sm.kernel_manager.shutdown_kernel(sessions[0]['kernel']['id'])
        listed = self.loop.run_sync(lambda: sm.list_sessions())
        expected = [
            {
                'id': sessions[1]['id'],
                'path': '/path/to/2/test2.ipynb',
                'type': 'notebook',
                'name': None,
                'notebook': {'path': '/path/to/2/test2.ipynb', 'name': None},
                'kernel': {
                    'id': 'B',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }
        ]
        self.assertEqual(listed, expected)

    def test_update_session(self):
        sm = self.sm
        session_id = self.create_session(path='/path/to/test.ipynb',
                                       kernel_name='julia')['id']
        self.loop.run_sync(lambda: sm.update_session(session_id, path='/path/to/new_name.ipynb'))
        model = self.loop.run_sync(lambda: sm.get_session(session_id=session_id))
        expected = {'id':session_id,
                    'path': '/path/to/new_name.ipynb',
                    'type': 'notebook',
                    'name': None,
                    'notebook': {'path': '/path/to/new_name.ipynb', 'name': None},
                    'kernel': {
                        'id': 'A',
                        'name':'julia',
                        'connections': 0,
                        'last_activity': dummy_date_s,
                        'execution_state': 'idle',
                    }
        }
        self.assertEqual(model, expected)
    
    def test_bad_update_session(self):
        # try to update a session with a bad keyword ~ raise error
        sm = self.sm
        session_id = self.create_session(path='/path/to/test.ipynb',
                                       kernel_name='ir')['id']
        with self.assertRaises(TypeError):
            self.loop.run_sync(lambda: sm.update_session(session_id=session_id, bad_kw='test.ipynb')) # Bad keyword

    def test_delete_session(self):
        sm = self.sm
        sessions = self.create_sessions(
            dict(path='/path/to/1/test1.ipynb', kernel_name='python'),
            dict(path='/path/to/2/test2.ipynb', kernel_name='python'),
            dict(path='/path/to/3', name='foo', type='console', kernel_name='python'),
        )
        self.loop.run_sync(lambda: sm.delete_session(sessions[1]['id']))
        new_sessions = self.loop.run_sync(lambda: sm.list_sessions())
        expected = [{
                'id': sessions[0]['id'],
                'path': '/path/to/1/test1.ipynb',
                'type': 'notebook',
                'name': None,
                'notebook': {'path': '/path/to/1/test1.ipynb', 'name': None},
                'kernel': {
                    'id': 'A',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }, {
                'id': sessions[2]['id'],
                'type': 'console',
                'path': '/path/to/3',
                'name': 'foo',
                'kernel': {
                    'id': 'C',
                    'name':'python',
                    'connections': 0,
                    'last_activity': dummy_date_s,
                    'execution_state': 'idle',
                }
            }
        ]
        self.assertEqual(new_sessions, expected)

    def test_bad_delete_session(self):
        # try to delete a session that doesn't exist ~ raise error
        sm = self.sm
        self.create_session(path='/path/to/test.ipynb', kernel_name='python')
        with self.assertRaises(TypeError):
            self.loop.run_sync(lambda : sm.delete_session(bad_kwarg='23424')) # Bad keyword
        with self.assertRaises(web.HTTPError):
            self.loop.run_sync(lambda : sm.delete_session(session_id='23424')) # nonexistent


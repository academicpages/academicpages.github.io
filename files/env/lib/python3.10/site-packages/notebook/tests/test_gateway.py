"""Test GatewayClient"""
import os
import json
import uuid
from datetime import datetime
from io import StringIO
from unittest.mock import patch

from tornado.web import HTTPError
from tornado.httpclient import HTTPRequest, HTTPResponse

from notebook.gateway.managers import GatewayClient
from notebook.utils import maybe_future
from .launchnotebook import NotebookTestBase


def generate_kernelspec(name):
    argv_stanza = ['python', '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    spec_stanza = {'spec': {'argv': argv_stanza, 'env': {}, 'display_name': name, 'language': 'python', 'interrupt_mode': 'signal', 'metadata': {}}}
    kernelspec_stanza = {'name': name, 'spec': spec_stanza, 'resources': {}}
    return kernelspec_stanza


# We'll mock up two kernelspecs - kspec_foo and kspec_bar
kernelspecs = {'default': 'kspec_foo', 'kernelspecs': {'kspec_foo': generate_kernelspec('kspec_foo'), 'kspec_bar': generate_kernelspec('kspec_bar')}}


# maintain a dictionary of expected running kernels.  Key = kernel_id, Value = model.
running_kernels = dict()


def generate_model(name):
    """Generate a mocked kernel model.  Caller is responsible for adding model to running_kernels dictionary."""
    dt = datetime.utcnow().isoformat() + 'Z'
    kernel_id = str(uuid.uuid4())
    model = {'id': kernel_id, 'name': name, 'last_activity': str(dt), 'execution_state': 'idle', 'connections': 1}
    return model


async def mock_gateway_request(url, **kwargs):
    method = 'GET'
    if kwargs['method']:
        method = kwargs['method']

    request = HTTPRequest(url=url, **kwargs)

    endpoint = str(url)

    # Fetch all kernelspecs
    if endpoint.endswith('/api/kernelspecs') and method == 'GET':
        response_buf = StringIO(json.dumps(kernelspecs))
        response = await maybe_future(HTTPResponse(request, 200, buffer=response_buf))
        return response

    # Fetch named kernelspec
    if endpoint.rfind('/api/kernelspecs/') >= 0 and method == 'GET':
        requested_kernelspec = endpoint.rpartition('/')[2]
        kspecs = kernelspecs.get('kernelspecs')
        if requested_kernelspec in kspecs:
            response_buf = StringIO(json.dumps(kspecs.get(requested_kernelspec)))
            response = await maybe_future(HTTPResponse(request, 200, buffer=response_buf))
            return response
        else:
            raise HTTPError(404, message=f'Kernelspec does not exist: {requested_kernelspec}')

    # Create kernel
    if endpoint.endswith('/api/kernels') and method == 'POST':
        json_body = json.loads(kwargs['body'])
        name = json_body.get('name')
        env = json_body.get('env')
        kspec_name = env.get('KERNEL_KSPEC_NAME')
        assert name == kspec_name   # Ensure that KERNEL_ env values get propagated
        model = generate_model(name)
        running_kernels[model.get('id')] = model  # Register model as a running kernel
        response_buf = StringIO(json.dumps(model))
        response = await maybe_future(HTTPResponse(request, 201, buffer=response_buf))
        return response

    # Fetch list of running kernels
    if endpoint.endswith('/api/kernels') and method == 'GET':
        kernels = []
        for kernel_id in running_kernels.keys():
            model = running_kernels.get(kernel_id)
            kernels.append(model)
        response_buf = StringIO(json.dumps(kernels))
        response = await maybe_future(HTTPResponse(request, 200, buffer=response_buf))
        return response

    # Interrupt or restart existing kernel
    if endpoint.rfind('/api/kernels/') >= 0 and method == 'POST':
        requested_kernel_id, sep, action = endpoint.rpartition('/api/kernels/')[2].rpartition('/')

        if action == 'interrupt':
            if requested_kernel_id in running_kernels:
                response = await maybe_future(HTTPResponse(request, 204))
                return response
            else:
                raise HTTPError(404, message=f'Kernel does not exist: {requested_kernel_id}')
        elif action == 'restart':
            if requested_kernel_id in running_kernels:
                response_buf = StringIO(json.dumps(running_kernels.get(requested_kernel_id)))
                response = await maybe_future(HTTPResponse(request, 204, buffer=response_buf))
                return response
            else:
                raise HTTPError(404, message=f'Kernel does not exist: {requested_kernel_id}')
        else:
            raise HTTPError(404, message=f'Bad action detected: {action}')

    # Shutdown existing kernel
    if endpoint.rfind('/api/kernels/') >= 0 and method == 'DELETE':
        requested_kernel_id = endpoint.rpartition('/')[2]
        running_kernels.pop(requested_kernel_id)  # Simulate shutdown by removing kernel from running set
        response = await maybe_future(HTTPResponse(request, 204))
        return response

    # Fetch existing kernel
    if endpoint.rfind('/api/kernels/') >= 0 and method == 'GET':
        requested_kernel_id = endpoint.rpartition('/')[2]
        if requested_kernel_id in running_kernels:
            response_buf = StringIO(json.dumps(running_kernels.get(requested_kernel_id)))
            response = await maybe_future(HTTPResponse(request, 200, buffer=response_buf))
            return response
        else:
            raise HTTPError(404, message=f'Kernel does not exist: {requested_kernel_id}')


mocked_gateway = patch('notebook.gateway.managers.gateway_request', mock_gateway_request)


class TestGateway(NotebookTestBase):

    mock_gateway_url = 'http://mock-gateway-server:8889'
    mock_http_user = 'alice'

    @classmethod
    def setup_class(cls):
        GatewayClient.clear_instance()
        super().setup_class()

    @classmethod
    def teardown_class(cls):
        GatewayClient.clear_instance()
        super().teardown_class()

    @classmethod
    def get_patch_env(cls):
        test_env = super().get_patch_env()
        test_env.update({'JUPYTER_GATEWAY_URL': TestGateway.mock_gateway_url,
                         'JUPYTER_GATEWAY_CONNECT_TIMEOUT': '44.4'})
        return test_env

    @classmethod
    def get_argv(cls):
        argv = super().get_argv()
        argv.extend(['--GatewayClient.request_timeout=96.0', '--GatewayClient.http_user=' + TestGateway.mock_http_user])
        return argv

    def setUp(self):
        kwargs = dict()
        GatewayClient.instance().load_connection_args(**kwargs)
        super().setUp()

    def test_gateway_options(self):
        assert self.notebook.gateway_config.gateway_enabled == True
        assert self.notebook.gateway_config.url == TestGateway.mock_gateway_url
        assert self.notebook.gateway_config.http_user == TestGateway.mock_http_user
        assert self.notebook.gateway_config.connect_timeout == self.notebook.gateway_config.connect_timeout
        assert self.notebook.gateway_config.connect_timeout == 44.4
        assert self.notebook.gateway_config.request_timeout == 96.0
        assert os.environ['KERNEL_LAUNCH_TIMEOUT'] == str(96)  # Ensure KLT gets set from request-timeout

    def test_gateway_class_mappings(self):
        # Ensure appropriate class mappings are in place.
        assert self.notebook.kernel_manager_class.__name__ == 'GatewayKernelManager'
        assert self.notebook.session_manager_class.__name__ == 'GatewaySessionManager'
        assert self.notebook.kernel_spec_manager_class.__name__ == 'GatewayKernelSpecManager'

    def test_gateway_get_kernelspecs(self):
        # Validate that kernelspecs come from gateway.
        with mocked_gateway:
            response = self.request('GET', '/api/kernelspecs')
            self.assertEqual(response.status_code, 200)
            content = json.loads(response.content.decode('utf-8'))
            kspecs = content.get('kernelspecs')
            assert len(kspecs) == 2
            assert kspecs.get('kspec_bar').get('name') == 'kspec_bar'

    def test_gateway_get_named_kernelspec(self):
        # Validate that a specific kernelspec can be retrieved from gateway.
        with mocked_gateway:
            response = self.request('GET', '/api/kernelspecs/kspec_foo')
            assert response.status_code == 200
            kspec_foo = json.loads(response.content.decode('utf-8'))
            assert kspec_foo.get('name') == 'kspec_foo'

            response = self.request('GET', '/api/kernelspecs/no_such_spec')
            assert response.status_code == 404

    def test_gateway_session_lifecycle(self):
        # Validate session lifecycle functions; create and delete.

        # create
        session_id, kernel_id = self.create_session('kspec_foo')

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # interrupt
        self.interrupt_kernel(kernel_id)

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # restart
        self.restart_kernel(kernel_id)

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # delete
        self.delete_session(session_id)
        self.assertFalse(self.is_kernel_running(kernel_id))

    def test_gateway_kernel_lifecycle(self):
        # Validate kernel lifecycle functions; create, interrupt, restart and delete.

        # create
        kernel_id = self.create_kernel('kspec_bar')

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # interrupt
        self.interrupt_kernel(kernel_id)

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # restart
        self.restart_kernel(kernel_id)

        # ensure kernel still considered running
        self.assertTrue(self.is_kernel_running(kernel_id))

        # delete
        self.delete_kernel(kernel_id)
        self.assertFalse(self.is_kernel_running(kernel_id))

    def create_session(self, kernel_name):
        """Creates a session for a kernel.  The session is created against the notebook server
           which then uses the gateway for kernel management.
        """
        with mocked_gateway:
            nb_path = os.path.join(self.notebook_dir, 'testgw.ipynb')
            kwargs = dict()
            kwargs['json'] = {'path': nb_path, 'type': 'notebook', 'kernel': {'name': kernel_name}}

            # add a KERNEL_ value to the current env and we'll ensure that that value exists in the mocked method
            os.environ['KERNEL_KSPEC_NAME'] = kernel_name

            # Create the kernel... (also tests get_kernel)
            response = self.request('POST', '/api/sessions', **kwargs)
            self.assertEqual(response.status_code, 201)
            model = json.loads(response.content.decode('utf-8'))
            self.assertEqual(model.get('path'), nb_path)
            kernel_id = model.get('kernel').get('id')
            # ensure its in the running_kernels and name matches.
            running_kernel = running_kernels.get(kernel_id)
            self.assertEqual(kernel_id, running_kernel.get('id'))
            self.assertEqual(model.get('kernel').get('name'), running_kernel.get('name'))
            session_id = model.get('id')

            # restore env
            os.environ.pop('KERNEL_KSPEC_NAME')
            return session_id, kernel_id

    def delete_session(self, session_id):
        """Deletes a session corresponding to the given session id.
        """
        with mocked_gateway:
            # Delete the session (and kernel)
            response = self.request('DELETE', '/api/sessions/' + session_id)
            self.assertEqual(response.status_code, 204)
            self.assertEqual(response.reason, 'No Content')

    def is_kernel_running(self, kernel_id):
        """Issues request to get the set of running kernels
        """
        with mocked_gateway:
            # Get list of running kernels
            response = self.request('GET', '/api/kernels')
            self.assertEqual(response.status_code, 200)
            kernels = json.loads(response.content.decode('utf-8'))
            self.assertEqual(len(kernels), len(running_kernels))
            for model in kernels:
                if model.get('id') == kernel_id:
                    return True
            return False

    def create_kernel(self, kernel_name):
        """Issues request to restart the given kernel
        """
        with mocked_gateway:
            kwargs = dict()
            kwargs['json'] = {'name': kernel_name}

            # add a KERNEL_ value to the current env and we'll ensure that that value exists in the mocked method
            os.environ['KERNEL_KSPEC_NAME'] = kernel_name

            response = self.request('POST', '/api/kernels', **kwargs)
            self.assertEqual(response.status_code, 201)
            model = json.loads(response.content.decode('utf-8'))
            kernel_id = model.get('id')
            # ensure its in the running_kernels and name matches.
            running_kernel = running_kernels.get(kernel_id)
            self.assertEqual(kernel_id, running_kernel.get('id'))
            self.assertEqual(model.get('name'), kernel_name)

            # restore env
            os.environ.pop('KERNEL_KSPEC_NAME')
            return kernel_id

    def interrupt_kernel(self, kernel_id):
        """Issues request to interrupt the given kernel
        """
        with mocked_gateway:
            response = self.request('POST', '/api/kernels/' + kernel_id + '/interrupt')
            self.assertEqual(response.status_code, 204)
            self.assertEqual(response.reason, 'No Content')

    def restart_kernel(self, kernel_id):
        """Issues request to restart the given kernel
        """
        with mocked_gateway:
            response = self.request('POST', '/api/kernels/' + kernel_id + '/restart')
            self.assertEqual(response.status_code, 200)
            model = json.loads(response.content.decode('utf-8'))
            restarted_kernel_id = model.get('id')
            # ensure its in the running_kernels and name matches.
            running_kernel = running_kernels.get(restarted_kernel_id)
            self.assertEqual(restarted_kernel_id, running_kernel.get('id'))
            self.assertEqual(model.get('name'), running_kernel.get('name'))

    def delete_kernel(self, kernel_id):
        """Deletes kernel corresponding to the given kernel id.
        """
        with mocked_gateway:
            # Delete the session (and kernel)
            response = self.request('DELETE', '/api/kernels/' + kernel_id)
            self.assertEqual(response.status_code, 204)
            self.assertEqual(response.reason, 'No Content')

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import json

from socket import gaierror
from tornado import web
from tornado.escape import json_encode, json_decode, url_escape
from tornado.httpclient import HTTPClient, AsyncHTTPClient, HTTPError

from ..services.kernels.kernelmanager import AsyncMappingKernelManager
from ..services.sessions.sessionmanager import SessionManager

from jupyter_client.kernelspec import KernelSpecManager
from ..utils import url_path_join

from traitlets import Instance, Unicode, Int, Float, Bool, default, validate, TraitError
from traitlets.config import SingletonConfigurable


class GatewayClient(SingletonConfigurable):
    """This class manages the configuration.  It's its own singleton class so that we
       can share these values across all objects.  It also contains some helper methods
       to build request arguments out of the various config options.

    """

    url = Unicode(default_value=None, allow_none=True, config=True,
        help="""The url of the Kernel or Enterprise Gateway server where
        kernel specifications are defined and kernel management takes place.
        If defined, this Notebook server acts as a proxy for all kernel
        management and kernel specification retrieval.  (JUPYTER_GATEWAY_URL env var)
        """
    )

    url_env = 'JUPYTER_GATEWAY_URL'

    @default('url')
    def _url_default(self):
        return os.environ.get(self.url_env)

    @validate('url')
    def _url_validate(self, proposal):
        value = proposal['value']
        # Ensure value, if present, starts with 'http'
        if value is not None and len(value) > 0:
            if not str(value).lower().startswith('http'):
                raise TraitError(f"GatewayClient url must start with 'http': '{value!r}'")
        return value

    ws_url = Unicode(default_value=None, allow_none=True, config=True,
        help="""The websocket url of the Kernel or Enterprise Gateway server.  If not provided, this value
        will correspond to the value of the Gateway url with 'ws' in place of 'http'.  (JUPYTER_GATEWAY_WS_URL env var)
        """
    )

    ws_url_env = 'JUPYTER_GATEWAY_WS_URL'

    @default('ws_url')
    def _ws_url_default(self):
        default_value = os.environ.get(self.ws_url_env)
        if default_value is None:
            if self.gateway_enabled:
                default_value = self.url.lower().replace('http', 'ws')
        return default_value

    @validate('ws_url')
    def _ws_url_validate(self, proposal):
        value = proposal['value']
        # Ensure value, if present, starts with 'ws'
        if value is not None and len(value) > 0:
            if not str(value).lower().startswith('ws'):
                raise TraitError(f"GatewayClient ws_url must start with 'ws': '{value!r}'")
        return value

    kernels_endpoint_default_value = '/api/kernels'
    kernels_endpoint_env = 'JUPYTER_GATEWAY_KERNELS_ENDPOINT'
    kernels_endpoint = Unicode(default_value=kernels_endpoint_default_value, config=True,
        help="""The gateway API endpoint for accessing kernel resources (JUPYTER_GATEWAY_KERNELS_ENDPOINT env var)""")

    @default('kernels_endpoint')
    def _kernels_endpoint_default(self):
        return os.environ.get(self.kernels_endpoint_env, self.kernels_endpoint_default_value)

    kernelspecs_endpoint_default_value = '/api/kernelspecs'
    kernelspecs_endpoint_env = 'JUPYTER_GATEWAY_KERNELSPECS_ENDPOINT'
    kernelspecs_endpoint = Unicode(default_value=kernelspecs_endpoint_default_value, config=True,
        help="""The gateway API endpoint for accessing kernelspecs (JUPYTER_GATEWAY_KERNELSPECS_ENDPOINT env var)""")

    @default('kernelspecs_endpoint')
    def _kernelspecs_endpoint_default(self):
        return os.environ.get(self.kernelspecs_endpoint_env, self.kernelspecs_endpoint_default_value)

    kernelspecs_resource_endpoint_default_value = '/kernelspecs'
    kernelspecs_resource_endpoint_env = 'JUPYTER_GATEWAY_KERNELSPECS_RESOURCE_ENDPOINT'
    kernelspecs_resource_endpoint = Unicode(default_value=kernelspecs_resource_endpoint_default_value, config=True,
        help="""The gateway endpoint for accessing kernelspecs resources
            (JUPYTER_GATEWAY_KERNELSPECS_RESOURCE_ENDPOINT env var)""")

    @default('kernelspecs_resource_endpoint')
    def _kernelspecs_resource_endpoint_default(self):
        return os.environ.get(self.kernelspecs_resource_endpoint_env, self.kernelspecs_resource_endpoint_default_value)

    connect_timeout_default_value = 40.0
    connect_timeout_env = 'JUPYTER_GATEWAY_CONNECT_TIMEOUT'
    connect_timeout = Float(default_value=connect_timeout_default_value, config=True,
        help="""The time allowed for HTTP connection establishment with the Gateway server.
        (JUPYTER_GATEWAY_CONNECT_TIMEOUT env var)""")

    @default('connect_timeout')
    def connect_timeout_default(self):
        return float(os.environ.get('JUPYTER_GATEWAY_CONNECT_TIMEOUT', self.connect_timeout_default_value))

    request_timeout_default_value = 40.0
    request_timeout_env = 'JUPYTER_GATEWAY_REQUEST_TIMEOUT'
    request_timeout = Float(default_value=request_timeout_default_value, config=True,
        help="""The time allowed for HTTP request completion. (JUPYTER_GATEWAY_REQUEST_TIMEOUT env var)""")

    @default('request_timeout')
    def request_timeout_default(self):
        return float(os.environ.get('JUPYTER_GATEWAY_REQUEST_TIMEOUT', self.request_timeout_default_value))

    client_key = Unicode(default_value=None, allow_none=True, config=True,
        help="""The filename for client SSL key, if any.  (JUPYTER_GATEWAY_CLIENT_KEY env var)
        """
    )
    client_key_env = 'JUPYTER_GATEWAY_CLIENT_KEY'

    @default('client_key')
    def _client_key_default(self):
        return os.environ.get(self.client_key_env)

    client_cert = Unicode(default_value=None, allow_none=True, config=True,
        help="""The filename for client SSL certificate, if any.  (JUPYTER_GATEWAY_CLIENT_CERT env var)
        """
    )
    client_cert_env = 'JUPYTER_GATEWAY_CLIENT_CERT'

    @default('client_cert')
    def _client_cert_default(self):
        return os.environ.get(self.client_cert_env)

    ca_certs = Unicode(default_value=None, allow_none=True, config=True,
        help="""The filename of CA certificates or None to use defaults.  (JUPYTER_GATEWAY_CA_CERTS env var)
        """
    )
    ca_certs_env = 'JUPYTER_GATEWAY_CA_CERTS'

    @default('ca_certs')
    def _ca_certs_default(self):
        return os.environ.get(self.ca_certs_env)

    http_user = Unicode(default_value=None, allow_none=True, config=True,
        help="""The username for HTTP authentication. (JUPYTER_GATEWAY_HTTP_USER env var)
        """
    )
    http_user_env = 'JUPYTER_GATEWAY_HTTP_USER'

    @default('http_user')
    def _http_user_default(self):
        return os.environ.get(self.http_user_env)

    http_pwd = Unicode(default_value=None, allow_none=True, config=True,
        help="""The password for HTTP authentication.  (JUPYTER_GATEWAY_HTTP_PWD env var)
        """
    )
    http_pwd_env = 'JUPYTER_GATEWAY_HTTP_PWD'

    @default('http_pwd')
    def _http_pwd_default(self):
        return os.environ.get(self.http_pwd_env)

    headers_default_value = '{}'
    headers_env = 'JUPYTER_GATEWAY_HEADERS'
    headers = Unicode(default_value=headers_default_value, allow_none=True, config=True,
        help="""Additional HTTP headers to pass on the request.  This value will be converted to a dict.
          (JUPYTER_GATEWAY_HEADERS env var)
        """
    )

    @default('headers')
    def _headers_default(self):
        return os.environ.get(self.headers_env, self.headers_default_value)

    auth_token = Unicode(default_value=None, allow_none=True, config=True,
        help="""The authorization token used in the HTTP headers.  (JUPYTER_GATEWAY_AUTH_TOKEN env var)
        """
    )
    auth_token_env = 'JUPYTER_GATEWAY_AUTH_TOKEN'

    @default('auth_token')
    def _auth_token_default(self):
        return os.environ.get(self.auth_token_env, '')

    validate_cert_default_value = True
    validate_cert_env = 'JUPYTER_GATEWAY_VALIDATE_CERT'
    validate_cert = Bool(default_value=validate_cert_default_value, config=True,
        help="""For HTTPS requests, determines if server's certificate should be validated or not.
        (JUPYTER_GATEWAY_VALIDATE_CERT env var)"""
    )

    @default('validate_cert')
    def validate_cert_default(self):
        return bool(os.environ.get(self.validate_cert_env, str(self.validate_cert_default_value)) not in ['no', 'false'])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._static_args = {}  # initialized on first use

    env_whitelist_default_value = ''
    env_whitelist_env = 'JUPYTER_GATEWAY_ENV_WHITELIST'
    env_whitelist = Unicode(default_value=env_whitelist_default_value, config=True,
        help="""A comma-separated list of environment variable names that will be included, along with
         their values, in the kernel startup request.  The corresponding `env_whitelist` configuration
         value must also be set on the Gateway server - since that configuration value indicates which
         environmental values to make available to the kernel. (JUPYTER_GATEWAY_ENV_WHITELIST env var)""")

    @default('env_whitelist')
    def _env_whitelist_default(self):
        return os.environ.get(self.env_whitelist_env, self.env_whitelist_default_value)

    gateway_retry_interval_default_value = 1.0
    gateway_retry_interval_env = 'JUPYTER_GATEWAY_RETRY_INTERVAL'
    gateway_retry_interval = Float(default_value=gateway_retry_interval_default_value, config=True,
        help="""The time allowed for HTTP reconnection with the Gateway server for the first time.
                Next will be JUPYTER_GATEWAY_RETRY_INTERVAL multiplied by two in factor of numbers of retries
                but less than JUPYTER_GATEWAY_RETRY_INTERVAL_MAX.
                (JUPYTER_GATEWAY_RETRY_INTERVAL env var)""")

    @default('gateway_retry_interval')
    def gateway_retry_interval_default(self):
        return float(os.environ.get('JUPYTER_GATEWAY_RETRY_INTERVAL', self.gateway_retry_interval_default_value))

    gateway_retry_interval_max_default_value = 30.0
    gateway_retry_interval_max_env = 'JUPYTER_GATEWAY_RETRY_INTERVAL_MAX'
    gateway_retry_interval_max = Float(default_value=gateway_retry_interval_max_default_value, config=True,
        help="""The maximum time allowed for HTTP reconnection retry with the Gateway server.
                (JUPYTER_GATEWAY_RETRY_INTERVAL_MAX env var)""")

    @default('gateway_retry_interval_max')
    def gateway_retry_interval_max_default(self):
        return float(os.environ.get('JUPYTER_GATEWAY_RETRY_INTERVAL_MAX', self.gateway_retry_interval_max_default_value))

    gateway_retry_max_default_value = 5
    gateway_retry_max_env = 'JUPYTER_GATEWAY_RETRY_MAX'
    gateway_retry_max = Int(default_value=gateway_retry_max_default_value, config=True,
        help="""The maximum retries allowed for HTTP reconnection with the Gateway server.
                (JUPYTER_GATEWAY_RETRY_MAX env var)""")

    @default('gateway_retry_max')
    def gateway_retry_max_default(self):
        return int(os.environ.get('JUPYTER_GATEWAY_RETRY_MAX', self.gateway_retry_max_default_value))

    @property
    def gateway_enabled(self):
        return bool(self.url is not None and len(self.url) > 0)

    # Ensure KERNEL_LAUNCH_TIMEOUT has a default value.
    KERNEL_LAUNCH_TIMEOUT = int(os.environ.get('KERNEL_LAUNCH_TIMEOUT', 40))

    def init_static_args(self):
        """Initialize arguments used on every request.  Since these are static values, we'll
        perform this operation once.

        """
        # Ensure that request timeout and KERNEL_LAUNCH_TIMEOUT are the same, taking the
        #  greater value of the two.
        if self.request_timeout < float(GatewayClient.KERNEL_LAUNCH_TIMEOUT):
            self.request_timeout = float(GatewayClient.KERNEL_LAUNCH_TIMEOUT)
        elif self.request_timeout > float(GatewayClient.KERNEL_LAUNCH_TIMEOUT):
            GatewayClient.KERNEL_LAUNCH_TIMEOUT = int(self.request_timeout)
        # Ensure any adjustments are reflected in env.
        os.environ['KERNEL_LAUNCH_TIMEOUT'] = str(GatewayClient.KERNEL_LAUNCH_TIMEOUT)

        self._static_args['headers'] = json.loads(self.headers)
        if 'Authorization' not in self._static_args['headers'].keys():
            self._static_args['headers'].update({
                'Authorization': f'token {self.auth_token}'
            })
        self._static_args['connect_timeout'] = self.connect_timeout
        self._static_args['request_timeout'] = self.request_timeout
        self._static_args['validate_cert'] = self.validate_cert
        if self.client_cert:
            self._static_args['client_cert'] = self.client_cert
            self._static_args['client_key'] = self.client_key
            if self.ca_certs:
                self._static_args['ca_certs'] = self.ca_certs
        if self.http_user:
            self._static_args['auth_username'] = self.http_user
        if self.http_pwd:
            self._static_args['auth_password'] = self.http_pwd

    def load_connection_args(self, **kwargs):
        """Merges the static args relative to the connection, with the given keyword arguments.  If statics
         have yet to be initialized, we'll do that here.

        """
        if len(self._static_args) == 0:
            self.init_static_args()

        for arg, static_value in self._static_args.items():
            if arg == 'headers':
                given_value = kwargs.setdefault(arg, {})
                if isinstance(given_value, dict):
                    given_value.update(static_value)
            else:
                kwargs[arg] = static_value
        return kwargs


async def gateway_request(endpoint, **kwargs):
    """Make an async request to kernel gateway endpoint, returns a response """
    client = AsyncHTTPClient()
    kwargs = GatewayClient.instance().load_connection_args(**kwargs)
    try:
        response = await client.fetch(endpoint, **kwargs)
    # Trap a set of common exceptions so that we can inform the user that their Gateway url is incorrect
    # or the server is not running.
    # NOTE: We do this here since this handler is called during the Notebook's startup and subsequent refreshes
    # of the tree view.
    except ConnectionRefusedError as e:
        raise web.HTTPError(
            503,
            f"Connection refused from Gateway server url '{GatewayClient.instance().url}'.  "
            f"Check to be sure the Gateway instance is running."
        ) from e
    except HTTPError as e:
        # This can occur if the host is valid (e.g., foo.com) but there's nothing there.
        raise web.HTTPError(
            e.code,
            f"Error attempting to connect to Gateway server url '{GatewayClient.instance().url}'.  "
            f"Ensure gateway url is valid and the Gateway instance is running."
        ) from e
    except gaierror as e:
        raise web.HTTPError(
            404,
            f"The Gateway server specified in the gateway_url '{GatewayClient.instance().url}' "
            f"doesn't appear to be valid.  "
            f"Ensure gateway url is valid and the Gateway instance is running."
        ) from e

    return response


class GatewayKernelManager(AsyncMappingKernelManager):
    """Kernel manager that supports remote kernels hosted by Jupyter Kernel or Enterprise Gateway."""

    # We'll maintain our own set of kernel ids
    _kernels = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_endpoint = url_path_join(GatewayClient.instance().url, GatewayClient.instance().kernels_endpoint)

    def __contains__(self, kernel_id):
        return kernel_id in self._kernels

    def remove_kernel(self, kernel_id):
        """Complete override since we want to be more tolerant of missing keys """
        try:
            return self._kernels.pop(kernel_id)
        except KeyError:
            pass

    def _get_kernel_endpoint_url(self, kernel_id=None):
        """Builds a url for the kernels endpoint

        Parameters
        ----------
        kernel_id: kernel UUID (optional)
        """
        if kernel_id:
            return url_path_join(self.base_endpoint, url_escape(str(kernel_id)))

        return self.base_endpoint

    async def start_kernel(self, kernel_id=None, path=None, **kwargs):
        """Start a kernel for a session and return its kernel_id.

        Parameters
        ----------
        kernel_id : uuid
            The uuid to associate the new kernel with. If this
            is not None, this kernel will be persistent whenever it is
            requested.
        path : API path
            The API path (unicode, '/' delimited) for the cwd.
            Will be transformed to an OS path relative to root_dir.
        """
        self.log.info('Request start kernel: kernel_id=%s, path="%s"', kernel_id, path)

        if kernel_id is None:
            if path is not None:
                kwargs['cwd'] = self.cwd_for_path(path)
            kernel_name = kwargs.get('kernel_name', 'python3')
            kernel_url = self._get_kernel_endpoint_url()
            self.log.debug(f"Request new kernel at: {kernel_url}")

            # Let KERNEL_USERNAME take precedent over http_user config option.
            if os.environ.get('KERNEL_USERNAME') is None and GatewayClient.instance().http_user:
                os.environ['KERNEL_USERNAME'] = GatewayClient.instance().http_user

            kernel_env = {k: v for (k, v) in dict(os.environ).items() if k.startswith('KERNEL_')
                        or k in GatewayClient.instance().env_whitelist.split(",")}

            # Convey the full path to where this notebook file is located.
            if path is not None and kernel_env.get('KERNEL_WORKING_DIR') is None:
                kernel_env['KERNEL_WORKING_DIR'] = kwargs['cwd']

            json_body = json_encode({'name': kernel_name, 'env': kernel_env})

            response = await gateway_request(
                kernel_url, method='POST', headers={'Content-Type': 'application/json'}, body=json_body
            )
            kernel = json_decode(response.body)
            kernel_id = kernel['id']
            self.log.info(f"Kernel started: {kernel_id}")
            self.log.debug(f"Kernel args: {kwargs!r}")
        else:
            kernel = await self.get_kernel(kernel_id)
            kernel_id = kernel['id']
            self.log.info(f"Using existing kernel: {kernel_id}")

        self._kernels[kernel_id] = kernel
        return kernel_id

    async def get_kernel(self, kernel_id=None, **kwargs):
        """Get kernel for kernel_id.

        Parameters
        ----------
        kernel_id : uuid
            The uuid of the kernel.
        """
        kernel_url = self._get_kernel_endpoint_url(kernel_id)
        self.log.debug(f"Request kernel at: {kernel_url}")
        try:
            response = await gateway_request(kernel_url, method='GET')
        except web.HTTPError as error:
            if error.status_code == 404:
                self.log.warn(f"Kernel not found at: {kernel_url}")
                self.remove_kernel(kernel_id)
                kernel = None
            else:
                raise
        else:
            kernel = json_decode(response.body)
            # Only update our models if we already know about this kernel
            if kernel_id in self._kernels:
                self._kernels[kernel_id] = kernel
                self.log.debug("Kernel retrieved: %s", kernel)
            else:
                self.log.warning("Kernel '%s' is not managed by this instance.", kernel_id)
                kernel = None
        return kernel

    async def kernel_model(self, kernel_id):
        """Return a dictionary of kernel information described in the
        JSON standard model.

        Parameters
        ----------
        kernel_id : uuid
            The uuid of the kernel.
        """
        self.log.debug("RemoteKernelManager.kernel_model: %s", kernel_id)
        model = await self.get_kernel(kernel_id)
        return model

    async def list_kernels(self, **kwargs):
        """Get a list of kernels."""
        kernel_url = self._get_kernel_endpoint_url()
        self.log.debug("Request list kernels: %s", kernel_url)
        response = await gateway_request(kernel_url, method='GET')
        kernels = json_decode(response.body)
        # Only update our models if we already know about the kernels
        self._kernels = {x['id']: x for x in kernels if x['id'] in self._kernels}
        return list(self._kernels.values())

    async def shutdown_kernel(self, kernel_id, now=False, restart=False):
        """Shutdown a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to shutdown.
        now : bool
            Shutdown the kernel immediately (True) or gracefully (False)
        restart : bool
            The purpose of this shutdown is to restart the kernel (True)
        """
        kernel_url = self._get_kernel_endpoint_url(kernel_id)
        self.log.debug("Request shutdown kernel at: %s", kernel_url)
        response = await gateway_request(kernel_url, method='DELETE')
        self.log.debug("Shutdown kernel response: %d %s", response.code, response.reason)
        self.remove_kernel(kernel_id)

    async def restart_kernel(self, kernel_id, now=False, **kwargs):
        """Restart a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to restart.
        """
        kernel_url = self._get_kernel_endpoint_url(kernel_id) + '/restart'
        self.log.debug("Request restart kernel at: %s", kernel_url)
        response = await gateway_request(
            kernel_url, method='POST', headers={'Content-Type': 'application/json'}, body=json_encode({})
        )
        self.log.debug("Restart kernel response: %d %s", response.code, response.reason)

    async def interrupt_kernel(self, kernel_id, **kwargs):
        """Interrupt a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to interrupt.
        """
        kernel_url = self._get_kernel_endpoint_url(kernel_id) + '/interrupt'
        self.log.debug("Request interrupt kernel at: %s", kernel_url)
        response = await gateway_request(
            kernel_url, method='POST', headers={'Content-Type': 'application/json'}, body=json_encode({})
        )
        self.log.debug("Interrupt kernel response: %d %s", response.code, response.reason)

    def shutdown_all(self, now=False):
        """Shutdown all kernels."""
        # Note: We have to make this sync because the NotebookApp does not wait for async.
        shutdown_kernels = []
        kwargs = {'method': 'DELETE'}
        kwargs = GatewayClient.instance().load_connection_args(**kwargs)
        client = HTTPClient()
        for kernel_id in self._kernels:
            kernel_url = self._get_kernel_endpoint_url(kernel_id)
            self.log.debug("Request delete kernel at: %s", kernel_url)
            try:
                response = client.fetch(kernel_url, **kwargs)
            except HTTPError:
                pass
            else:
                self.log.debug("Delete kernel response: %d %s", response.code, response.reason)
            shutdown_kernels.append(kernel_id)  # avoid changing dict size during iteration
        client.close()
        for kernel_id in shutdown_kernels:
            self.remove_kernel(kernel_id)


class GatewayKernelSpecManager(KernelSpecManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_endpoint = url_path_join(GatewayClient.instance().url,
                                      GatewayClient.instance().kernelspecs_endpoint)

        self.base_endpoint = GatewayKernelSpecManager._get_endpoint_for_user_filter(base_endpoint)
        self.base_resource_endpoint = url_path_join(GatewayClient.instance().url,
                                                    GatewayClient.instance().kernelspecs_resource_endpoint)

    @staticmethod
    def _get_endpoint_for_user_filter(default_endpoint):
        kernel_user = os.environ.get('KERNEL_USERNAME')
        if kernel_user:
            return '?user='.join([default_endpoint, kernel_user])
        return default_endpoint

    def _get_kernelspecs_endpoint_url(self, kernel_name=None):
        """Builds a url for the kernels endpoint

        Parameters
        ----------
        kernel_name: kernel name (optional)
        """
        if kernel_name:
            return url_path_join(self.base_endpoint, url_escape(kernel_name))

        return self.base_endpoint

    async def get_all_specs(self):
        fetched_kspecs = await self.list_kernel_specs()

        # get the default kernel name and compare to that of this server.
        # If different log a warning and reset the default.  However, the
        # caller of this method will still return this server's value until
        # the next fetch of kernelspecs - at which time they'll match.
        km = self.parent.kernel_manager
        remote_default_kernel_name = fetched_kspecs.get('default')
        if remote_default_kernel_name != km.default_kernel_name:
            self.log.info("Default kernel name on Gateway server ({gateway_default}) differs from "
                          "Notebook server ({notebook_default}).  Updating to Gateway server's value.".
                          format(gateway_default=remote_default_kernel_name,
                                 notebook_default=km.default_kernel_name))
            km.default_kernel_name = remote_default_kernel_name

        remote_kspecs = fetched_kspecs.get('kernelspecs')
        return remote_kspecs

    async def list_kernel_specs(self):
        """Get a list of kernel specs."""
        kernel_spec_url = self._get_kernelspecs_endpoint_url()
        self.log.debug("Request list kernel specs at: %s", kernel_spec_url)
        response = await gateway_request(kernel_spec_url, method='GET')
        kernel_specs = json_decode(response.body)
        return kernel_specs

    async def get_kernel_spec(self, kernel_name, **kwargs):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        """
        kernel_spec_url = self._get_kernelspecs_endpoint_url(kernel_name=str(kernel_name))
        self.log.debug(f"Request kernel spec at: {kernel_spec_url}")
        try:
            response = await gateway_request(kernel_spec_url, method='GET')
        except web.HTTPError as error:
            if error.status_code == 404:
                # Convert not found to KeyError since that's what the Notebook handler expects
                # message is not used, but might as well make it useful for troubleshooting
                raise KeyError(
                    'kernelspec {kernel_name} not found on Gateway server at: {gateway_url}'.
                    format(kernel_name=kernel_name, gateway_url=GatewayClient.instance().url)
                ) from error
            else:
                raise
        else:
            kernel_spec = json_decode(response.body)

        return kernel_spec

    async def get_kernel_spec_resource(self, kernel_name, path):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        path : str
            The name of the desired resource
        """
        kernel_spec_resource_url = url_path_join(self.base_resource_endpoint, str(kernel_name), str(path))
        self.log.debug(f"Request kernel spec resource '{path}' at: {kernel_spec_resource_url}")
        try:
            response = await gateway_request(kernel_spec_resource_url, method='GET')
        except web.HTTPError as error:
            if error.status_code == 404:
                kernel_spec_resource = None
            else:
                raise
        else:
            kernel_spec_resource = response.body
        return kernel_spec_resource


class GatewaySessionManager(SessionManager):
    kernel_manager = Instance('notebook.gateway.managers.GatewayKernelManager')

    async def kernel_culled(self, kernel_id):
        """Checks if the kernel is still considered alive and returns true if its not found. """
        kernel = await self.kernel_manager.get_kernel(kernel_id)
        return kernel is None

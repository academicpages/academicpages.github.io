# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

import logging
import os
import shutil
import tempfile
import warnings

import pytest

import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
from zmq.tests import BaseZMQTestCase, SkipTest, skip_pypy


class BaseAuthTestCase(BaseZMQTestCase):
    def setUp(self):
        if zmq.zmq_version_info() < (4, 0):
            raise SkipTest("security is new in libzmq 4.0")
        try:
            zmq.curve_keypair()
        except zmq.ZMQError:
            raise SkipTest("security requires libzmq to have curve support")
        super().setUp()
        # enable debug logging while we run tests
        logging.getLogger('zmq.auth').setLevel(logging.DEBUG)
        self.auth = self.make_auth()
        self.auth.start()
        self.base_dir, self.public_keys_dir, self.secret_keys_dir = self.create_certs()

    def make_auth(self):
        raise NotImplementedError()

    def tearDown(self):
        if self.auth:
            self.auth.stop()
            self.auth = None
        self.remove_certs(self.base_dir)
        super().tearDown()

    def create_certs(self):
        """Create CURVE certificates for a test"""

        # Create temporary CURVE key pairs for this test run. We create all keys in a
        # temp directory and then move them into the appropriate private or public
        # directory.

        base_dir = tempfile.mkdtemp()
        keys_dir = os.path.join(base_dir, 'certificates')
        public_keys_dir = os.path.join(base_dir, 'public_keys')
        secret_keys_dir = os.path.join(base_dir, 'private_keys')

        os.mkdir(keys_dir)
        os.mkdir(public_keys_dir)
        os.mkdir(secret_keys_dir)

        server_public_file, server_secret_file = zmq.auth.create_certificates(
            keys_dir, "server"
        )
        client_public_file, client_secret_file = zmq.auth.create_certificates(
            keys_dir, "client"
        )

        for key_file in os.listdir(keys_dir):
            if key_file.endswith(".key"):
                shutil.move(
                    os.path.join(keys_dir, key_file), os.path.join(public_keys_dir, '.')
                )

        for key_file in os.listdir(keys_dir):
            if key_file.endswith(".key_secret"):
                shutil.move(
                    os.path.join(keys_dir, key_file), os.path.join(secret_keys_dir, '.')
                )

        return (base_dir, public_keys_dir, secret_keys_dir)

    def remove_certs(self, base_dir):
        """Remove certificates for a test"""
        shutil.rmtree(base_dir)

    def load_certs(self, secret_keys_dir):
        """Return server and client certificate keys"""
        server_secret_file = os.path.join(secret_keys_dir, "server.key_secret")
        client_secret_file = os.path.join(secret_keys_dir, "client.key_secret")

        server_public, server_secret = zmq.auth.load_certificate(server_secret_file)
        client_public, client_secret = zmq.auth.load_certificate(client_secret_file)

        return server_public, server_secret, client_public, client_secret


class TestThreadAuthentication(BaseAuthTestCase):
    """Test authentication running in a thread"""

    def make_auth(self):
        return ThreadAuthenticator(self.context)

    def can_connect(self, server, client):
        """Check if client can connect to server using tcp transport"""
        result = False
        iface = 'tcp://127.0.0.1'
        port = server.bind_to_random_port(iface)
        client.connect("%s:%i" % (iface, port))
        msg = [b"Hello World"]
        # run poll on server twice
        # to flush spurious events
        server.poll(100, zmq.POLLOUT)

        if server.poll(1000, zmq.POLLOUT):
            try:
                server.send_multipart(msg, zmq.NOBLOCK)
            except zmq.Again:
                warnings.warn("server set POLLOUT, but cannot send", RuntimeWarning)
                return False
        else:
            return False

        if client.poll(1000):
            try:
                rcvd_msg = client.recv_multipart(zmq.NOBLOCK)
            except zmq.Again:
                warnings.warn("client set POLLIN, but cannot recv", RuntimeWarning)
            else:
                assert rcvd_msg == msg
                result = True
        return result

    def test_null(self):
        """threaded auth - NULL"""
        # A default NULL connection should always succeed, and not
        # go through our authentication infrastructure at all.
        self.auth.stop()
        self.auth = None
        # use a new context, so ZAP isn't inherited
        self.context = self.Context()

        server = self.socket(zmq.PUSH)
        client = self.socket(zmq.PULL)
        assert self.can_connect(server, client)

        # By setting a domain we switch on authentication for NULL sockets,
        # though no policies are configured yet. The client connection
        # should still be allowed.
        server = self.socket(zmq.PUSH)
        server.zap_domain = b'global'
        client = self.socket(zmq.PULL)
        assert self.can_connect(server, client)

    def test_blacklist(self):
        """threaded auth - Blacklist"""
        # Blacklist 127.0.0.1, connection should fail
        self.auth.deny('127.0.0.1')
        server = self.socket(zmq.PUSH)
        # By setting a domain we switch on authentication for NULL sockets,
        # though no policies are configured yet.
        server.zap_domain = b'global'
        client = self.socket(zmq.PULL)
        assert not self.can_connect(server, client)

    def test_whitelist(self):
        """threaded auth - Whitelist"""
        # Whitelist 127.0.0.1, connection should pass"
        self.auth.allow('127.0.0.1')
        server = self.socket(zmq.PUSH)
        # By setting a domain we switch on authentication for NULL sockets,
        # though no policies are configured yet.
        server.zap_domain = b'global'
        client = self.socket(zmq.PULL)
        assert self.can_connect(server, client)

    def test_plain(self):
        """threaded auth - PLAIN"""

        # Try PLAIN authentication - without configuring server, connection should fail
        server = self.socket(zmq.PUSH)
        server.plain_server = True
        client = self.socket(zmq.PULL)
        client.plain_username = b'admin'
        client.plain_password = b'Password'
        assert not self.can_connect(server, client)

        # Try PLAIN authentication - with server configured, connection should pass
        server = self.socket(zmq.PUSH)
        server.plain_server = True
        client = self.socket(zmq.PULL)
        client.plain_username = b'admin'
        client.plain_password = b'Password'
        self.auth.configure_plain(domain='*', passwords={'admin': 'Password'})
        assert self.can_connect(server, client)

        # Try PLAIN authentication - with bogus credentials, connection should fail
        server = self.socket(zmq.PUSH)
        server.plain_server = True
        client = self.socket(zmq.PULL)
        client.plain_username = b'admin'
        client.plain_password = b'Bogus'
        assert not self.can_connect(server, client)

        # Remove authenticator and check that a normal connection works
        self.auth.stop()
        self.auth = None

        server = self.socket(zmq.PUSH)
        client = self.socket(zmq.PULL)
        assert self.can_connect(server, client)
        client.close()
        server.close()

    def test_curve(self):
        """threaded auth - CURVE"""
        self.auth.allow('127.0.0.1')
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        # Try CURVE authentication - without configuring server, connection should fail
        server = self.socket(zmq.PUSH)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PULL)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert not self.can_connect(server, client)

        # Try CURVE authentication - with server configured to CURVE_ALLOW_ANY, connection should pass
        self.auth.configure_curve(domain='*', location=zmq.auth.CURVE_ALLOW_ANY)
        server = self.socket(zmq.PUSH)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PULL)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert self.can_connect(server, client)

        # Try CURVE authentication - with server configured, connection should pass
        self.auth.configure_curve(domain='*', location=self.public_keys_dir)
        server = self.socket(zmq.PULL)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PUSH)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert self.can_connect(client, server)

        # Remove authenticator and check that a normal connection works
        self.auth.stop()
        self.auth = None

        # Try connecting using NULL and no authentication enabled, connection should pass
        server = self.socket(zmq.PUSH)
        client = self.socket(zmq.PULL)
        assert self.can_connect(server, client)

    def test_curve_callback(self):
        """threaded auth - CURVE with callback authentication"""
        self.auth.allow('127.0.0.1')
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        # Try CURVE authentication - without configuring server, connection should fail
        server = self.socket(zmq.PUSH)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PULL)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert not self.can_connect(server, client)

        # Try CURVE authentication - with callback authentication configured, connection should pass

        class CredentialsProvider:
            def __init__(self):
                self.client = client_public

            def callback(self, domain, key):
                if key == self.client:
                    return True
                else:
                    return False

        provider = CredentialsProvider()
        self.auth.configure_curve_callback(credentials_provider=provider)
        server = self.socket(zmq.PUSH)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PULL)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert self.can_connect(server, client)

        # Try CURVE authentication - with callback authentication configured with wrong key, connection should not pass

        class WrongCredentialsProvider:
            def __init__(self):
                self.client = "WrongCredentials"

            def callback(self, domain, key):
                if key == self.client:
                    return True
                else:
                    return False

        provider = WrongCredentialsProvider()
        self.auth.configure_curve_callback(credentials_provider=provider)
        server = self.socket(zmq.PUSH)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PULL)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert not self.can_connect(server, client)

    @skip_pypy
    def test_curve_user_id(self):
        """threaded auth - CURVE"""
        self.auth.allow('127.0.0.1')
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        self.auth.configure_curve(domain='*', location=self.public_keys_dir)
        server = self.socket(zmq.PULL)
        server.curve_publickey = server_public
        server.curve_secretkey = server_secret
        server.curve_server = True
        client = self.socket(zmq.PUSH)
        client.curve_publickey = client_public
        client.curve_secretkey = client_secret
        client.curve_serverkey = server_public
        assert self.can_connect(client, server)

        # test default user-id map
        client.send(b'test')
        msg = self.recv(server, copy=False)
        assert msg.bytes == b'test'
        try:
            user_id = msg.get('User-Id')
        except zmq.ZMQVersionError:
            pass
        else:
            assert user_id == client_public.decode("utf8")

        # test custom user-id map
        self.auth.curve_user_id = lambda client_key: 'custom'

        client2 = self.socket(zmq.PUSH)
        client2.curve_publickey = client_public
        client2.curve_secretkey = client_secret
        client2.curve_serverkey = server_public
        assert self.can_connect(client2, server)

        client2.send(b'test2')
        msg = self.recv(server, copy=False)
        assert msg.bytes == b'test2'
        try:
            user_id = msg.get('User-Id')
        except zmq.ZMQVersionError:
            pass
        else:
            assert user_id == 'custom'


def with_ioloop(method, expect_success=True):
    """decorator for running tests with an IOLoop"""

    def test_method(self):
        r = method(self)

        loop = self.io_loop
        if expect_success:
            self.pullstream.on_recv(self.on_message_succeed)
        else:
            self.pullstream.on_recv(self.on_message_fail)

        loop.call_later(1, self.attempt_connection)
        loop.call_later(1.2, self.send_msg)

        if expect_success:
            loop.call_later(2, self.on_test_timeout_fail)
        else:
            loop.call_later(2, self.on_test_timeout_succeed)

        loop.start()
        if self.fail_msg:
            self.fail(self.fail_msg)

        return r

    return test_method


def should_auth(method):
    return with_ioloop(method, True)


def should_not_auth(method):
    return with_ioloop(method, False)


class TestIOLoopAuthentication(BaseAuthTestCase):
    """Test authentication running in ioloop"""

    def setUp(self):
        try:
            from tornado import ioloop
        except ImportError:
            pytest.skip("Requires tornado")
        from zmq.eventloop import zmqstream

        self.fail_msg = None
        self.io_loop = ioloop.IOLoop()
        super().setUp()
        self.server = self.socket(zmq.PUSH)
        self.client = self.socket(zmq.PULL)
        self.pushstream = zmqstream.ZMQStream(self.server, self.io_loop)
        self.pullstream = zmqstream.ZMQStream(self.client, self.io_loop)

    def make_auth(self):
        from zmq.auth.ioloop import IOLoopAuthenticator

        return IOLoopAuthenticator(self.context, io_loop=self.io_loop)

    def tearDown(self):
        if self.auth:
            self.auth.stop()
            self.auth = None
        self.io_loop.close(all_fds=True)
        super().tearDown()

    def attempt_connection(self):
        """Check if client can connect to server using tcp transport"""
        iface = 'tcp://127.0.0.1'
        port = self.server.bind_to_random_port(iface)
        self.client.connect("%s:%i" % (iface, port))

    def send_msg(self):
        """Send a message from server to a client"""
        msg = [b"Hello World"]
        self.pushstream.send_multipart(msg)

    def on_message_succeed(self, frames):
        """A message was received, as expected."""
        if frames != [b"Hello World"]:
            self.fail_msg = "Unexpected message received"
        self.io_loop.stop()

    def on_message_fail(self, frames):
        """A message was received, unexpectedly."""
        self.fail_msg = 'Received messaged unexpectedly, security failed'
        self.io_loop.stop()

    def on_test_timeout_succeed(self):
        """Test timer expired, indicates test success"""
        self.io_loop.stop()

    def on_test_timeout_fail(self):
        """Test timer expired, indicates test failure"""
        self.fail_msg = 'Test timed out'
        self.io_loop.stop()

    @should_auth
    def test_none(self):
        """ioloop auth - NONE"""
        # A default NULL connection should always succeed, and not
        # go through our authentication infrastructure at all.
        # no auth should be running
        self.auth.stop()
        self.auth = None

    @should_auth
    def test_null(self):
        """ioloop auth - NULL"""
        # By setting a domain we switch on authentication for NULL sockets,
        # though no policies are configured yet. The client connection
        # should still be allowed.
        self.server.zap_domain = b'global'

    @should_not_auth
    def test_blacklist(self):
        """ioloop auth - Blacklist"""
        # Blacklist 127.0.0.1, connection should fail
        self.auth.deny('127.0.0.1')
        self.server.zap_domain = b'global'

    @should_auth
    def test_whitelist(self):
        """ioloop auth - Whitelist"""
        # Whitelist 127.0.0.1, which overrides the blacklist, connection should pass"
        self.auth.allow('127.0.0.1')

        self.server.setsockopt(zmq.ZAP_DOMAIN, b'global')

    @should_not_auth
    def test_plain_unconfigured_server(self):
        """ioloop auth - PLAIN, unconfigured server"""
        self.client.plain_username = b'admin'
        self.client.plain_password = b'Password'
        # Try PLAIN authentication - without configuring server, connection should fail
        self.server.plain_server = True

    @should_auth
    def test_plain_configured_server(self):
        """ioloop auth - PLAIN, configured server"""
        self.client.plain_username = b'admin'
        self.client.plain_password = b'Password'
        # Try PLAIN authentication - with server configured, connection should pass
        self.server.plain_server = True
        self.auth.configure_plain(domain='*', passwords={'admin': 'Password'})

    @should_not_auth
    def test_plain_bogus_credentials(self):
        """ioloop auth - PLAIN, bogus credentials"""
        self.client.plain_username = b'admin'
        self.client.plain_password = b'Bogus'
        self.server.plain_server = True

        self.auth.configure_plain(domain='*', passwords={'admin': 'Password'})

    @should_not_auth
    def test_curve_unconfigured_server(self):
        """ioloop auth - CURVE, unconfigured server"""
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        self.auth.allow('127.0.0.1')

        self.server.curve_publickey = server_public
        self.server.curve_secretkey = server_secret
        self.server.curve_server = True

        self.client.curve_publickey = client_public
        self.client.curve_secretkey = client_secret
        self.client.curve_serverkey = server_public

    @should_auth
    def test_curve_allow_any(self):
        """ioloop auth - CURVE, CURVE_ALLOW_ANY"""
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        self.auth.allow('127.0.0.1')
        self.auth.configure_curve(domain='*', location=zmq.auth.CURVE_ALLOW_ANY)

        self.server.curve_publickey = server_public
        self.server.curve_secretkey = server_secret
        self.server.curve_server = True

        self.client.curve_publickey = client_public
        self.client.curve_secretkey = client_secret
        self.client.curve_serverkey = server_public

    @should_auth
    def test_curve_configured_server(self):
        """ioloop auth - CURVE, configured server"""
        self.auth.allow('127.0.0.1')
        certs = self.load_certs(self.secret_keys_dir)
        server_public, server_secret, client_public, client_secret = certs

        self.auth.configure_curve(domain='*', location=self.public_keys_dir)

        self.server.curve_publickey = server_public
        self.server.curve_secretkey = server_secret
        self.server.curve_server = True

        self.client.curve_publickey = client_public
        self.client.curve_secretkey = client_secret
        self.client.curve_serverkey = server_public

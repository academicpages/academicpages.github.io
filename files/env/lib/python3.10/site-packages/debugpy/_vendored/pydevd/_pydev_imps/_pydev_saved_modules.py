import sys
import os

IS_PY2 = sys.version_info < (3,)


def find_in_pythonpath(module_name):
    # Check all the occurrences where we could match the given module/package in the PYTHONPATH.
    #
    # This is a simplistic approach, but probably covers most of the cases we're interested in
    # (i.e.: this may fail in more elaborate cases of import customization or .zip imports, but
    # this should be rare in general).
    found_at = []

    parts = module_name.split('.')  # split because we need to convert mod.name to mod/name
    for path in sys.path:
        target = os.path.join(path, *parts)
        target_py = target + '.py'
        if os.path.isdir(target):
            found_at.append(target)
        if os.path.exists(target_py):
            found_at.append(target_py)
    return found_at


class DebuggerInitializationError(BaseException):
    pass


class VerifyShadowedImport(object):

    def __init__(self, import_name):
        self.import_name = import_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if exc_type == DebuggerInitializationError:
                return False  # It's already an error we generated.

            # We couldn't even import it...
            found_at = find_in_pythonpath(self.import_name)

            if len(found_at) <= 1:
                # It wasn't found anywhere or there was just 1 occurrence.
                # Let's just return to show the original error.
                return False

            # We found more than 1 occurrence of the same module in the PYTHONPATH
            # (the user module and the standard library module).
            # Let's notify the user as it seems that the module was shadowed.
            msg = self._generate_shadowed_import_message(found_at)
            raise DebuggerInitializationError(msg)

    def _generate_shadowed_import_message(self, found_at):
        msg = '''It was not possible to initialize the debugger due to a module name conflict.

i.e.: the module "%(import_name)s" could not be imported because it is shadowed by:
%(found_at)s
Please rename this file/folder so that the original module from the standard library can be imported.''' % {
    'import_name': self.import_name, 'found_at': found_at[0]}

        return msg

    def check(self, module, expected_attributes):
        msg = ''
        for expected_attribute in expected_attributes:
            try:
                getattr(module, expected_attribute)
            except:
                msg = self._generate_shadowed_import_message([module.__file__])
                break

        if msg:
            raise DebuggerInitializationError(msg)


with VerifyShadowedImport('threading') as verify_shadowed:
    import threading;    verify_shadowed.check(threading, ['Thread', 'settrace', 'setprofile', 'Lock', 'RLock', 'current_thread'])

with VerifyShadowedImport('time') as verify_shadowed:
    import time;    verify_shadowed.check(time, ['sleep', 'time', 'mktime'])

with VerifyShadowedImport('socket') as verify_shadowed:
    import socket;    verify_shadowed.check(socket, ['socket', 'gethostname', 'getaddrinfo'])

with VerifyShadowedImport('select') as verify_shadowed:
    import select;    verify_shadowed.check(select, ['select'])

with VerifyShadowedImport('code') as verify_shadowed:
    import code as _code;    verify_shadowed.check(_code, ['compile_command', 'InteractiveInterpreter'])

if IS_PY2:
    with VerifyShadowedImport('thread') as verify_shadowed:
        import thread;    verify_shadowed.check(thread, ['start_new_thread', 'allocate_lock'])

    with VerifyShadowedImport('Queue') as verify_shadowed:
        import Queue as _queue;    verify_shadowed.check(_queue, ['Queue', 'LifoQueue', 'Empty', 'Full', 'deque'])

    with VerifyShadowedImport('xmlrpclib') as verify_shadowed:
        import xmlrpclib;    verify_shadowed.check(xmlrpclib, ['ServerProxy', 'Marshaller', 'Server'])

    with VerifyShadowedImport('SimpleXMLRPCServer') as verify_shadowed:
        import SimpleXMLRPCServer as _pydev_SimpleXMLRPCServer;    verify_shadowed.check(_pydev_SimpleXMLRPCServer, ['SimpleXMLRPCServer'])

    with VerifyShadowedImport('BaseHTTPServer') as verify_shadowed:
        import BaseHTTPServer;    verify_shadowed.check(BaseHTTPServer, ['BaseHTTPRequestHandler'])
else:
    with VerifyShadowedImport('_thread') as verify_shadowed:
        import _thread as thread;    verify_shadowed.check(thread, ['start_new_thread', 'start_new', 'allocate_lock'])

    with VerifyShadowedImport('queue') as verify_shadowed:
        import queue as _queue;    verify_shadowed.check(_queue, ['Queue', 'LifoQueue', 'Empty', 'Full', 'deque'])

    with VerifyShadowedImport('xmlrpclib') as verify_shadowed:
        import xmlrpc.client as xmlrpclib;    verify_shadowed.check(xmlrpclib, ['ServerProxy', 'Marshaller', 'Server'])

    with VerifyShadowedImport('xmlrpc.server') as verify_shadowed:
        import xmlrpc.server as _pydev_SimpleXMLRPCServer;    verify_shadowed.check(_pydev_SimpleXMLRPCServer, ['SimpleXMLRPCServer'])

    with VerifyShadowedImport('http.server') as verify_shadowed:
        import http.server as BaseHTTPServer;    verify_shadowed.check(BaseHTTPServer, ['BaseHTTPRequestHandler'])


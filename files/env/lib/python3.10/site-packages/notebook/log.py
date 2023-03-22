#-----------------------------------------------------------------------------
#  Copyright (c) Jupyter Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file LICENSE, distributed as part of this software.
#-----------------------------------------------------------------------------

import json
from tornado.log import access_log
from .prometheus.log_functions import prometheus_log_method


def log_request(handler, log=access_log, log_json=False):
    """log a bit more information about each request than tornado's default
    
    - move static file get success to debug-level (reduces noise)
    - get proxied IP instead of proxy IP
    - log referer for redirect and failed requests
    - log user-agent for failed requests
    """
    status = handler.get_status()
    request = handler.request
    if status < 300 or status == 304:
        # Successes (or 304 FOUND) are debug-level
        log_method = log.debug
    elif status < 400:
        log_method = log.info
    elif status < 500:
        log_method = log.warning
    else:
        log_method = log.error

    request_time = 1000.0 * request.request_time()
    ns = dict(
        status=status,
        method=request.method,
        ip=request.remote_ip,
        uri=request.uri,
        request_time=float(f'{request_time:.2f}'),
    )
    msg = "{status} {method} {uri} ({ip}) {request_time:f}ms"
    if status >= 400:
        # log bad referers
        ns['referer'] = request.headers.get('Referer', 'None')
        msg += ' referer={referer}'
    if status >= 500 and status != 502:
        # Log a subset of the headers if it caused an error.
        headers = {}
        for header in ['Host', 'Accept', 'Referer', 'User-Agent']:
            if header in request.headers:
                headers[header] = request.headers[header]
        if log_json:
            log_method("", extra=dict(props=headers))
        else:
            log_method(json.dumps(dict(headers), indent=2))
    if log_json:
        log_method("", extra=dict(props=ns))
    else:
        log_method(msg.format(**ns))
    prometheus_log_method(handler)

import unittest
from unittest import mock

from notebook import log


class TestLogRequest(unittest.TestCase):

    @mock.patch('notebook.log.prometheus_log_method')
    def test_log_request_json(self, mock_prometheus):
        headers = {'Referer': 'test'}
        request = mock.Mock(
            request_time=mock.Mock(return_value=1),
            headers=headers,
            method='GET',
            remote_ip='1.2.3.4',
            uri='/notebooks/foo/bar'
        )
        handler = mock.MagicMock(
            request=request,
            get_status=mock.Mock(return_value=500)
        )
        logger = mock.MagicMock()
        log.log_request(handler, log=logger, log_json=True)
        # Since the status was 500 there should be two calls to log.error,
        # one with the request headers and another with the other request
        # parameters.
        self.assertEqual(2, logger.error.call_count)
        logger.error.assert_has_calls([
            mock.call("", extra=dict(props=dict(headers))),
            mock.call("", extra=dict(props={
                'status': handler.get_status(),
                'method': request.method,
                'ip': request.remote_ip,
                'uri': request.uri,
                'request_time': 1000.0,
                'referer': headers['Referer']
            }))
        ])
        mock_prometheus.assert_called_once_with(handler)

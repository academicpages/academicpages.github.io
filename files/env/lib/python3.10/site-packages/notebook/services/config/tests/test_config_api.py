"""Test the config webservice API."""

import json

from notebook.utils import url_path_join
from notebook.tests.launchnotebook import NotebookTestBase


class ConfigAPI:
    """Wrapper for notebook API calls."""
    def __init__(self, request):
        self.request = request

    def _req(self, verb, section, body=None):
        response = self.request(verb,
                url_path_join('api/config', section),
                data=body,
        )
        response.raise_for_status()
        return response

    def get(self, section):
        return self._req('GET', section)

    def set(self, section, values):
        return self._req('PUT', section, json.dumps(values))

    def modify(self, section, values):
        return self._req('PATCH', section, json.dumps(values))

class APITest(NotebookTestBase):
    """Test the config web service API"""
    def setUp(self):
        self.config_api = ConfigAPI(self.request)

    def test_create_retrieve_config(self):
        sample = {'foo': 'bar', 'baz': 73}
        r = self.config_api.set('example', sample)
        self.assertEqual(r.status_code, 204)

        r = self.config_api.get('example')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), sample)

    def test_modify(self):
        sample = {'foo': 'bar', 'baz': 73,
                  'sub': {'a': 6, 'b': 7}, 'sub2': {'c': 8}}
        self.config_api.set('example', sample)

        r = self.config_api.modify('example', {'foo': None,  # should delete foo
                                               'baz': 75,
                                               'wib': [1,2,3],
                                               'sub': {'a': 8, 'b': None, 'd': 9},
                                               'sub2': {'c': None}  # should delete sub2
                                              })
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {'baz': 75, 'wib': [1,2,3],
                                    'sub': {'a': 8, 'd': 9}})

    def test_get_unknown(self):
        # We should get an empty config dictionary instead of a 404
        r = self.config_api.get('nonexistant')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {})


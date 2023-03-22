from notebook.utils import url_path_join
from notebook.tests.launchnotebook import NotebookTestBase

class NbconvertAPI:
    """Wrapper for nbconvert API calls."""
    def __init__(self, request):
        self.request = request

    def _req(self, verb, path, body=None, params=None):
        response = self.request(verb,
                url_path_join('api/nbconvert', path),
                data=body, params=params,
        )
        response.raise_for_status()
        return response

    def list_formats(self):
        return self._req('GET', '')

class APITest(NotebookTestBase):
    def setUp(self):
        self.nbconvert_api = NbconvertAPI(self.request)

    def test_list_formats(self):
        formats = self.nbconvert_api.list_formats().json()
        self.assertIsInstance(formats, dict)
        self.assertIn('python', formats)
        self.assertIn('html', formats)
        self.assertEqual(formats['python']['output_mimetype'], 'text/x-python')
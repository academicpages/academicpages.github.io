"""Test the basic /api endpoints"""

from datetime import timedelta

from notebook._tz import isoformat, utcnow
from notebook.utils import url_path_join
from notebook.tests.launchnotebook import NotebookTestBase


class APITest(NotebookTestBase):
    """Test the kernels web service API"""

    def _req(self, verb, path, **kwargs):
        r = self.request(verb, url_path_join('api', path))
        r.raise_for_status()
        return r

    def get(self, path, **kwargs):
        return self._req('GET', path)

    def test_get_spec(self):
        r = self.get('spec.yaml')
        assert r.text

    def test_get_status(self):
        r = self.get('status')
        data = r.json()
        assert data['connections'] == 0
        assert data['kernels'] == 0
        assert data['last_activity'].endswith('Z')
        assert data['started'].endswith('Z')
        assert data['started'] == isoformat(self.notebook.web_app.settings['started'])

    def test_no_track_activity(self):
        # initialize with old last api activity
        old = utcnow() - timedelta(days=1)
        settings = self.notebook.web_app.settings
        settings['api_last_activity'] = old
        # accessing status doesn't update activity
        self.get('status')
        assert settings['api_last_activity'] == old
        # accessing with ?no_track_activity doesn't update activity
        self.get('contents?no_track_activity=1')
        assert settings['api_last_activity'] == old
        # accessing without ?no_track_activity does update activity
        self.get('contents')
        assert settings['api_last_activity'] > old

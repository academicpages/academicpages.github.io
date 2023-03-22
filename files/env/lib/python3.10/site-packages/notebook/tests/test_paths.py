import re

from notebook.base.handlers import path_regex
from notebook.utils import url_path_join
from .launchnotebook import NotebookTestBase

# build regexps that tornado uses:
path_pat = re.compile(f'^/x{path_regex}$')


def test_path_regex():
    for path in (
        '/x',
        '/x/',
        '/x/foo',
        '/x/foo.ipynb',
        '/x/foo/bar',
        '/x/foo/bar.txt',
    ):
        assert re.match(path_pat, path)

def test_path_regex_bad():
    for path in (
        '/xfoo',
        '/xfoo/',
        '/xfoo/bar',
        '/xfoo/bar/',
        '/x/foo/bar/',
        '/x//foo',
        '/y',
        '/y/x/foo',
    ):
        assert not re.match(path_pat, path)


class RedirectTestCase(NotebookTestBase):
    def test_trailing_slash(self):
        for uri, expected in (
            ("/notebooks/mynotebook/", "/notebooks/mynotebook"),
            ("////foo///", "/foo"),
            ("//example.com/", "/example.com"),
            ("/has/param/?hasparam=true", "/has/param?hasparam=true"),
        ):
            r = self.request("GET", uri, allow_redirects=False)
            print(uri, expected)
            assert r.status_code == 302
            assert "Location" in r.headers
            assert r.headers["Location"] == url_path_join(self.url_prefix, expected)

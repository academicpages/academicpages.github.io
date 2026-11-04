"""Regression checks for publication matching, upgrades and outage handling."""
import copy
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sync', Path(__file__).with_name('update-publications.py'))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

PREPRINT = {'title': 'Sensing–Communication Trade-offs', 'authors': 'Adam Umra, Aydin Sezgin',
            'venue': 'arXiv', 'year': 2025, 'status': 'Preprint',
            'links': [{'label': 'arXiv', 'url': 'https://arxiv.org/abs/2511.02672'}]}
PUBLISHED = {'title': 'Sensing-Communication Trade-offs', 'authors': 'Adam Umra, Aydin Sezgin',
             'venue': 'Journal of Signals', 'year': 2026,
             'links': [{'label': 'DOI', 'url': 'https://doi.org/10.1234/test'}]}


class PublicationsTests(unittest.TestCase):
    def test_preprint_upgraded_without_duplicate_or_lost_link(self):
        result = sync.reconcile([], [PREPRINT, PUBLISHED], [PREPRINT])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], PREPRINT['title'])
        self.assertEqual(result[0]['venue'], PUBLISHED['venue'])
        self.assertEqual(result[0]['year'], 2026)
        self.assertNotIn('status', result[0])
        self.assertEqual(len(result[0]['links']), 2)

    def test_arxiv_never_downgrades_publication(self):
        result = sync.reconcile([PUBLISHED], [PREPRINT], [])
        self.assertNotIn('status', result[0])
        self.assertEqual(result[0]['venue'], 'Journal of Signals')

    def test_curated_details_win(self):
        manual = dict(PUBLISHED, venue='Journal of Signals, vol. 4, pp. 10–15')
        result = sync.reconcile([], [PUBLISHED, PREPRINT], [manual])
        self.assertEqual(result[0]['venue'], manual['venue'])
        self.assertEqual(len(result[0]['links']), 2)

    def test_changed_title_matches_shared_doi(self):
        renamed = dict(PUBLISHED, title='A new title')
        result = sync.reconcile([PUBLISHED], [renamed], [])
        self.assertEqual(len(result), 1)

    def test_doi_bridges_preprint_and_publication(self):
        bridge = copy.deepcopy(PREPRINT)
        bridge['links'] += PUBLISHED['links']
        separate = dict(PUBLISHED, title='A renamed journal paper')
        self.assertEqual(len(sync.reconcile([PREPRINT, separate], [bridge], [])), 1)

    def test_hidden_curated_record_is_not_reimported(self):
        self.assertEqual(sync.reconcile([PUBLISHED], [PREPRINT], [dict(PUBLISHED, hidden=True)]), [])

    def test_repeat_is_stable_and_preserves_records_missing_from_source(self):
        other = dict(PUBLISHED, title='Unrelated work', links=[{'label': 'DOI', 'url': 'https://doi.org/10.1234/other'}])
        first = sync.reconcile([other], [PREPRINT, PUBLISHED], [PREPRINT])
        self.assertEqual(first, sync.reconcile(first, [PREPRINT, PUBLISHED], [PREPRINT]))
        self.assertEqual(len(first), 2)

    def test_crossref_filters_author_collisions_and_extracts_metadata(self):
        item = {'title': ['<i>A paper</i>'], 'DOI': '10.1234/TEST', 'type': 'journal-article',
                'container-title': ['Signals &amp; Systems'], 'published': {'date-parts': [[2026, 4]]}}
        authors = [
            {'given': 'Adam', 'family': 'Umra'},
            {'given': 'A.', 'family': 'Umra'},
            {'given': 'Adam', 'family': 'Umra', 'ORCID': 'https://orcid.org/0000-0000-0000-0001'},
            {'given': 'A.', 'family': 'Umra', 'ORCID': 'https://orcid.org/' + sync.ORCID},
        ]
        payload = {'message': {'items': [dict(item, author=[a]) for a in authors]}}
        papers = sync.crossref_records(payload)
        self.assertEqual(len(papers), 2)
        self.assertEqual(papers[0]['venue'], 'Signals & Systems')
        self.assertEqual(papers[0]['title'], 'A paper')
        self.assertEqual(papers[0]['links'][0]['url'], 'https://doi.org/10.1234/test')

    def test_arxiv_versions_and_related_doi(self):
        feed = '''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:x="http://arxiv.org/schemas/atom">
        <entry><id>http://arxiv.org/abs/2511.02672v3</id><title> A\n paper </title>
        <author><name>Adam Umra</name></author><published>2025-11-04T00:00:00Z</published>
        <x:doi>10.1234/test</x:doi></entry></feed>'''
        papers = sync.arxiv_records(feed)
        self.assertEqual(papers[0]['links'][0]['url'], 'https://arxiv.org/abs/2511.02672')
        self.assertEqual(papers[0]['title'], 'A paper')
        self.assertEqual(papers[0]['status'], 'Preprint')
        self.assertIn('doi:10.1234/test', sync.identifiers(papers[0]))
        self.assertEqual(sync.arxiv_records(feed.replace('Adam Umra', 'Umra Adam')), [])
        with self.assertRaises(ValueError):
            sync.arxiv_records('<html>Service unavailable</html>')

    def test_outage_keeps_previous_records_and_applies_manual_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '_data').mkdir()
            (root / '_data/publications.yml').write_text(json.dumps([dict(PREPRINT, venue='Curated preprint')]))
            output = root / '_data/publications_generated.json'
            output.write_text(json.dumps([PUBLISHED]))
            with patch.object(sync, 'ROOT', root), patch.object(sync, 'OUTPUT', output), patch.object(sync, 'fetch', side_effect=urllib.error.URLError('source unavailable')):
                with contextlib.redirect_stderr(io.StringIO()) as warnings, contextlib.redirect_stdout(io.StringIO()):
                    sync.main()
                self.assertIn('refresh failed', warnings.getvalue())
            result = json.loads(output.read_text())
            self.assertEqual(len(result), 1)
            self.assertEqual(len(result[0]['links']), 2)
            self.assertEqual(result[0]['venue'], 'Journal of Signals')


if __name__ == '__main__':
    unittest.main()

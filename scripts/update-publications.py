#!/usr/bin/env python3
"""Refresh publication data without scraping Scholar or requiring API keys."""
import copy
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_data/publications_generated.json'
NAME = 'Adam Umra'
ORCID = '0009-0004-2071-2897'
NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}


def clean(value):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', '', value)).split())


def normalized(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', value).casefold() if c.isalnum())


def identifiers(paper):
    keys = {'title:' + normalized(paper['title'])}
    for link in paper.get('links', []):
        url = urllib.parse.urlsplit(link['url'])
        if url.hostname in ('doi.org', 'dx.doi.org'):
            keys.add('doi:' + urllib.parse.unquote(url.path).strip('/').lower())
        if url.hostname in ('arxiv.org', 'export.arxiv.org'):
            keys.add('arxiv:' + re.sub(r'v\d+$', '', url.path.removeprefix('/abs/')))
        if url.hostname == 'ieeexplore.ieee.org':
            keys.add('ieee:' + url.path.rstrip('/').split('/')[-1])
    return keys


def fetch(url):
    request = urllib.request.Request(url, headers={
        'User-Agent': 'AdamUmraPublications/1.0 (https://ayyou176.github.io/)',
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code != 429 and error.code < 500:
                raise
            if attempt == 2:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(4 * (attempt + 1))


def crossref_records(payload):
    records = []
    for item in payload['message']['items']:
        authors = item.get('author', [])
        def matches(author):
            orcid = author.get('ORCID', '').rstrip('/').split('/')[-1]
            if orcid:
                return orcid == ORCID
            return normalized(author.get('given', '') + ' ' + author.get('family', '')) == normalized(NAME)
        if not any(matches(a) for a in authors):
            continue
        if item.get('type') not in ('journal-article', 'proceedings-article'):
            continue
        dates = item.get('published', item.get('issued', {})).get('date-parts', [[]])[0]
        if not dates or not item.get('title') or not item.get('DOI'):
            continue
        doi = item['DOI'].lower()
        if not re.fullmatch(r'10\.\d{4,9}/\S+', doi):
            continue
        records.append({
            'title': clean(item['title'][0]),
            'authors': ', '.join(clean(a.get('given', '') + ' ' + a.get('family', '')) for a in authors),
            'venue': clean((item.get('container-title') or ['Published article'])[0]),
            'year': int(dates[0]),
            'date': '-'.join(f'{part:04d}' if i == 0 else f'{part:02d}' for i, part in enumerate(dates[:3])),
            'publisher_url': item.get('resource', {}).get('primary', {}).get('URL', ''),
            'links': [{'label': 'DOI', 'url': 'https://doi.org/' + doi}],
        })
    return records


def arxiv_records(payload):
    root = ET.fromstring(payload)
    if root.tag != '{http://www.w3.org/2005/Atom}feed':
        raise ValueError('arXiv returned an unexpected response')
    records = []
    for entry in root.findall('a:entry', NS):
        identifier = entry.findtext('a:id', '', NS)
        if '/api/errors' in identifier:
            raise ValueError('arXiv returned an API error')
        authors = [clean(a.findtext('a:name', '', NS)) for a in entry.findall('a:author', NS)]
        if normalized(NAME) not in [normalized(a) for a in authors]:
            continue
        arxiv_id = re.sub(r'v\d+$', '', identifier.split('/abs/')[-1])
        if not re.fullmatch(r'\d{4}\.\d{4,5}', arxiv_id):
            continue
        title = clean(entry.findtext('a:title', '', NS))
        year = entry.findtext('a:published', '', NS)[:4]
        if not title or not year.isdigit():
            continue
        paper = {'title': title, 'authors': ', '.join(authors), 'venue': 'arXiv',
                 'year': int(year), 'status': 'Preprint',
                 'preprint_date': entry.findtext('a:published', '', NS)[:10],
                 'links': [{'label': 'arXiv', 'url': 'https://arxiv.org/abs/' + arxiv_id}]}
        doi = entry.findtext('x:doi', '', NS).strip().lower()
        if re.fullmatch(r'10\.\d{4,9}/\S+', doi):
            paper['links'].append({'label': 'DOI', 'url': 'https://doi.org/' + doi})
        records.append(paper)
    return records


def merge(records, incoming):
    """Coalesce by DOI, arXiv ID, IEEE document ID, or normalized exact title."""
    incoming = copy.deepcopy(incoming)
    matches = []
    keys = identifiers(incoming)
    # A DOI record may bridge an earlier preprint and a separate journal record.
    while True:
        found = [p for p in records if p not in matches and keys & identifiers(p)]
        if not found:
            break
        for paper in found:
            matches.append(paper)
            keys |= identifiers(paper)
    combined = incoming
    for paper in matches:
        links = combined['links'] + paper['links']
        metadata = {key: combined.get(key) or paper.get(key) for key in ('date', 'preprint_date', 'publisher_url')}
        # A preprint response must never downgrade a known published paper.
        if combined.get('status') == 'Preprint' and paper.get('status') != 'Preprint':
            combined = copy.deepcopy(paper)
        combined.update({key: value for key, value in metadata.items() if value})
        combined['links'] = list({link['url']: link for link in links}.values())
        records.remove(paper)
    records.append(combined)


def reconcile(previous, fetched, curated):
    records = []
    for paper in previous + fetched:
        merge(records, paper)
    for paper in curated:
        matches = [p for p in records if identifiers(p) & identifiers(paper)]
        links = {link['url']: link for p in matches for link in p['links']}
        for match in matches:
            records.remove(match)
        if paper.get('hidden'):
            continue
        result = copy.deepcopy(paper)
        # Explicit editorial text wins. Only unambiguously published preprints
        # get automatic venue/year/status upgrades.
        published = next((p for p in matches if not p.get('status')), None)
        if result.get('status') == 'Preprint' and published:
            result['venue'], result['year'] = published['venue'], published['year']
            result.pop('status', None)
        for key in ('date', 'preprint_date', 'publisher_url'):
            if not result.get(key):
                value = next((p[key] for p in matches if p.get(key)), None)
                if value:
                    result[key] = value
        links.update({link['url']: link for link in result['links']})
        result['links'] = list(links.values())
        records.append(result)
    for paper in records:
        prepare_display(paper)
    return sorted(records, key=lambda p: (int(p['year']), p['sort_date'], normalized(p['title'])), reverse=True)


def prepare_display(paper):
    """Retain DOI identifiers for matching, expose only reading destinations."""
    links = []
    for link in paper['links']:
        url = urllib.parse.urlsplit(link['url'])
        if url.hostname in ('doi.org', 'dx.doi.org'):
            doi = urllib.parse.unquote(url.path).strip('/').lower()
            if doi.startswith(('10.1186/', '10.1007/')):
                links.append({'label': 'Journal', 'url': 'https://link.springer.com/article/' + doi})
            continue
        if url.scheme == 'https':
            links.append(link)
    publisher = paper.get('publisher_url', '')
    destination = urllib.parse.urlsplit(publisher)
    if destination.scheme in ('http', 'https') and destination.hostname not in ('doi.org', 'dx.doi.org'):
        publisher = urllib.parse.urlunsplit(destination._replace(scheme='https'))
        label = 'IEEE Xplore' if destination.hostname == 'ieeexplore.ieee.org' else 'Journal' if 'journal' in paper['venue'].lower() else 'Paper'
        links.append({'label': label, 'url': publisher})
    paper['display_links'] = list({link['url']: link for link in links}.values())
    paper['sort_date'] = paper.get('date') or paper.get('preprint_date') or str(paper['year'])


def main():
    curated = yaml.safe_load((ROOT / '_data/publications.yml').read_text())
    previous = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else []
    crossref_query = urllib.parse.urlencode({'query.author': NAME, 'rows': 1000})
    arxiv_query = urllib.parse.urlencode({'search_query': 'au:"Umra_Adam"', 'start': 0,
                                         'max_results': 1000, 'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    sources = [
        ('Crossref', 'https://api.crossref.org/works?' + crossref_query,
         lambda data: crossref_records(json.loads(data))),
        ('arXiv', 'https://export.arxiv.org/api/query?' + arxiv_query, arxiv_records),
    ]
    fetched = []
    successes = 0
    for name, url, parse in sources:
        try:
            papers = parse(fetch(url))
            if not papers:
                raise ValueError('No matching publications returned; retaining saved records')
            fetched.extend(papers)
            successes += 1
            print(f'{name}: {len(papers)} matching records')
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError, ET.ParseError) as error:
            print(f'::warning::{name} refresh failed: {error}', file=sys.stderr)
    # An outage cannot erase previously known publications or block a site edit.
    result = reconcile(previous, fetched, curated)
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if not OUTPUT.exists() or OUTPUT.read_text() != serialized:
        temporary = OUTPUT.with_suffix('.tmp')
        temporary.write_text(serialized)
        temporary.replace(OUTPUT)
    print(f'{len(result)} publications saved; {successes}/{len(sources)} sources refreshed.')


if __name__ == '__main__':
    main()

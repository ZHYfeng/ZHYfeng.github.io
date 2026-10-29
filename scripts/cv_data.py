"""Read the CV repository's data and adapt it for the website generators."""

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKIP = object()


def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding='utf-8')) or {}


def localize(value, lang):
    """Select en/zh text and honor visible_in on both records and fields."""
    if isinstance(value, dict):
        if lang not in value.get('visible_in', ('en', 'zh')):
            return SKIP
        if 'en' in value or 'zh' in value:
            if lang not in value:
                raise ValueError(f'Missing {lang} translation: {value!r}')
            return localize(value[lang], lang)
        result = {}
        for key, child in value.items():
            if key != 'visible_in':
                selected = localize(child, lang)
                if selected is not SKIP:
                    result[key] = selected
        return result
    if isinstance(value, list):
        return [selected for child in value
                if (selected := localize(child, lang)) is not SKIP]
    return value


def publication_year(pub):
    if pub.get('year') is not None:
        return int(pub['year'])
    # Dated CV IDs, e.g. syzspec-2025, are more reliable than venue text.
    match = re.search(r'-(\d{4})$', pub['id'])
    if match:
        return int(match[1])
    match = re.search(r'\b(\d{2}|\d{4})\b', pub.get('venue_short', ''))
    if match:
        year = int(match[1])
        return year + 2000 if year < 100 else year
    return None


def normalize_publications(source, urls):
    publications = []
    seen_ids, seen_slugs = set(), set()
    for raw in source['publications']:
        pub = localize(raw, 'en')
        if pub is SKIP:
            continue
        source_id = pub['id']
        if source_id in seen_ids:
            raise ValueError(f'Duplicate publication ID: {source_id}')
        seen_ids.add(source_id)
        slug = urls.get(source_id, source_id)
        if not re.fullmatch(r'[a-z0-9]+[a-z0-9-]*', slug):
            raise ValueError(f'Invalid publication slug: {slug!r}')
        if slug in seen_slugs:
            raise ValueError(f'Duplicate publication slug: {slug}')
        seen_slugs.add(slug)
        result = {
            'id': source_id,
            'label': pub.get('label', ''),
            'type': pub['type'],
            'title': pub['title'],
            'authors': pub.get('authors', []),
            'venue': pub.get('venue', ''),
            'venue_short': pub.get('venue_short', ''),
            'year': publication_year(pub),
            'slug': slug,
            'pdf': None,
            'github': {},
            'links': [],
            'related_links': [],
            'awards': [],
        }
        kinds = {'pdf': 'pdf', 'website': 'website',
                 'slides': 'slides', 'video': 'youtube'}
        for link in pub.get('links', []):
            kind, url = link['kind'], link['url']
            if kind in kinds:
                result[kinds[kind]] = url
            elif kind == 'github':
                result['github'][link.get('text', 'Code')] = url
            elif kind == 'named':
                result['related_links'].append({'text': link.get('text', 'Link'), 'url': url})
            elif url not in result['links']:
                result['links'].append(url)
        for annotation in pub.get('annotations', []):
            for item in annotation.get('items', []):
                if item.get('url'):
                    result['related_links'].append({'text': item.get('text', 'Link'), 'url': item['url']})
                elif item.get('text'):
                    result['awards'].append(item['text'])
        publications.append(result)
    return {'publications': publications}


def publication_catalog(path):
    return {pub['id']: pub for pub in load_yaml(path)['publications']}


def referenced_publication(record, catalog):
    source_id = record['publication']
    if source_id not in catalog:
        raise ValueError(f'Unknown publication reference: {source_id}')
    return catalog[source_id]

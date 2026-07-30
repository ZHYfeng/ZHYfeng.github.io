#!/usr/bin/env python3
"""
generate_pub_pages.py — Generate _publications/*.md from publications.yml.

Usage:
    python3 scripts/generate_pub_pages.py \
        --data _data/publications.yml \
        --output-dir _publications
"""

import argparse
import yaml
import re
from pathlib import Path


def make_filename(pub):
    """Generate a filename like YYYY-MM-DD-short-title.md"""
    year = pub.get('year', 2099)
    slug = pub.get('slug') or 'untitled'
    # Use conference month if available, otherwise default to July
    month = '07'
    day = '01'
    return f"{year}-{month}-{day}-{slug}.md"


def format_citation(pub):
    """Generate a citation string."""
    authors = pub.get('authors', [])
    title = pub.get('title', '')
    venue = pub.get('venue') or pub.get('venue_short', '')
    year = pub.get('year', '')

    # Format authors
    author_str = ', '.join(authors) if authors else ''

    # Build citation
    if author_str and title:
        citation = f'{author_str}. "{title}."'
        if venue:
            citation += f' <i>{venue}</i>'
        if year:
            citation += f' ({year}).'
    elif title:
        citation = f'"{title}."'
        if venue:
            citation += f' <i>{venue}</i>'
        if year:
            citation += f' ({year}).'
    else:
        citation = ''

    return citation


def get_category(pub_type):
    """Map publication type to collection category."""
    mapping = {
        'conference': 'conferences',
        'journal': 'manuscripts',
        'preprint': 'preprints',
    }
    return mapping.get(pub_type, 'conferences')


PUB_PAGE_TEMPLATE = """\
---
title: >-
  {title}
collection: publications
category: {category}
permalink: /publication/{slug}
excerpt: >-
  {excerpt}
date: {date}
venue: >-
  {venue}
paperurl: >-
  {paperurl}
citation: >-
  {citation}
---

{body}"""


def generate_pub_page(pub):
    """Generate a single publication markdown page."""
    year = pub.get('year', 2099)
    slug = pub.get('slug') or 'untitled'
    date = f"{year}-07-01"  # Default to July 1st

    title = pub.get('title', 'Untitled')
    # Escape quotes for YAML
    title_escaped = title.replace('"', "'")

    # Venue
    venue = pub.get('venue') or pub.get('venue_short') or ''

    # PDF URL
    paperurl = pub.get('pdf') or ''

    # Citation
    citation = format_citation(pub)
    # Escape for YAML: replace single quotes
    citation_escaped = citation.replace("'", "\\'")

    # Excerpt (first sentence of abstract or short description)
    excerpt = f"{title}"[:120]

    # Body — build rich content
    body_parts = []

    # Details paragraph
    details = []
    if pub.get('authors'):
        details.append(f"**Authors:** {', '.join(pub['authors'])}")
    if venue:
        details.append(f"**Venue:** {venue}")
    details.append(f"**Year:** {year}")

    body_parts.append('\n\n'.join(details))

    # Links section
    links = []
    if pub.get('pdf'):
        links.append(f'[📄 PDF]({pub["pdf"]})')
    if pub.get('github'):
        for name, url in pub['github'].items():
            links.append(f'[🐙 {name}]({url})')
    if pub.get('code'):
        for name, url in pub['code'].items():
            links.append(f'[💻 {name}]({url})')
    if pub.get('links'):
        for url in pub['links']:
            links.append(f'[🔗 Publisher]({url})')
    if pub.get('website'):
        links.append(f'[🌐 Website]({pub["website"]})')
    if pub.get('youtube'):
        links.append(f'[🎥 Talk]({pub["youtube"]})')
    if pub.get('slides'):
        links.append(f'[📊 Slides]({pub["slides"]})')

    if links:
        body_parts.append(' | '.join(links))

    # Awards
    if pub.get('awards') and not any(a == 'red' for a in pub['awards']):
        awards_str = '  \n'.join(f'🏆 {a}' for a in pub['awards'] if a != 'red' and a != 'red,')
        body_parts.append(f'**Awards & Recognitions:**  \n{awards_str}')

    body = '\n\n'.join(body_parts)

    return PUB_PAGE_TEMPLATE.format(
        title=title_escaped,
        category=get_category(pub.get('type', 'conferences')),
        slug=slug,
        excerpt=excerpt,
        date=date,
        venue=venue.replace("'", "\\'"),
        paperurl=paperurl,
        citation=citation_escaped,
        body=body,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, help='YAML file with publications')
    parser.add_argument('--output-dir', required=True, help='Output directory for .md files')
    args = parser.parse_args()

    with open(args.data, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    pubs = data.get('publications', [])
    if not pubs:
        print("No publications found")
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Remove existing generated files (those not starting with placeholder prefix)
    existing = list(output_dir.glob('*.md'))
    removed = 0
    for f in existing:
        # Keep only files that start with year- (our generated format)
        if re.match(r'^\d{4}-\d{2}-\d{2}-', f.name):
            f.unlink()
            removed += 1

    generated = 0
    for pub in pubs:
        filename = make_filename(pub)
        filepath = output_dir / filename
        content = generate_pub_page(pub)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        generated += 1

    print(f"✅ Generated {generated} publication pages ({removed} old files cleaned up)")


if __name__ == '__main__':
    main()

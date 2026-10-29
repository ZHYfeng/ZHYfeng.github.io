"""Regression tests for the CV repository to website data boundary."""

import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from cv_data import localize, normalize_publications
from generate_cv_md import CV_TEMPLATE_CN, CV_TEMPLATE_EN, build_context
from generate_pub_pages import generate_pub_page, make_filename
from sync_cv_data import sync_data


def paper(**fields):
    return {'id': 'example-2025', 'label': 'C1', 'type': 'conference',
            'title': 'Example: Program Analysis', 'authors': ['Yu Hao'], **fields}


class CVDataTests(unittest.TestCase):
    def test_visibility_applies_to_sections_records_and_translated_fields(self):
        data = {'sections': {
            'hidden': {'visible_in': [], 'entries': [{'text': 'hidden section'}]},
            'awards': {'entries': [
                {'text': 'hidden record', 'visible_in': []},
                {'text': {'en': 'English award', 'zh': '中文奖项'}},
                {'text': '中文专用', 'visible_in': ['zh']},
                {'text': 'shared', 'note': {'en': 'note', 'visible_in': ['en']}},
            ]},
        }}
        english = localize(data, 'en')
        chinese = localize(data, 'zh')
        self.assertNotIn('hidden', english['sections'])
        self.assertEqual(english['sections']['awards']['entries'],
                         [{'text': 'English award'}, {'text': 'shared', 'note': 'note'}])
        self.assertEqual(chinese['sections']['awards']['entries'],
                         [{'text': '中文奖项'}, {'text': '中文专用'}, {'text': 'shared'}])

    def test_missing_translation_is_reported(self):
        with self.assertRaisesRegex(ValueError, 'Missing zh translation'):
            localize({'title': {'en': 'English only'}}, 'zh')

    def test_cv_renders_translations_visibility_ongoing_dates_and_service(self):
        labels = {
            'education': {'en': 'Education', 'zh': '教育经历'},
            'experience': {'en': 'Experience', 'zh': '工作经历'},
            'awards': {'en': 'Awards', 'zh': '奖励'},
            'service': {'en': 'Service', 'zh': '学术服务'},
            'ongoing': {'en': 'present', 'zh': '至今'},
        }
        cv = {'sections': {
            'education': {'visible_in': [], 'entries': []},
            'experience': {'entries': [{
                'role': {'en': 'Researcher', 'zh': '研究员'},
                'start': '2024-10', 'end': None,
                'role_notes': [{'text': '中文附注', 'visible_in': ['zh']}],
            }]},
            'awards': {'entries': [
                {'year': 2025, 'text': 'hidden award', 'visible_in': []},
                {'year': 2024, 'text': {'en': 'Scholarship', 'zh': '奖学金'}},
            ]},
            'service': {'entries': [{
                'role': {'en': 'Reviewer', 'zh': '审稿人'}, 'year_order': 'descending',
                'activities': [{'venue': 'S&P', 'years': [2020, 2025]}],
            }]},
        }}
        english = CV_TEMPLATE_EN.render(**build_context(cv, labels, 'en'))
        chinese = CV_TEMPLATE_CN.render(**build_context(cv, labels, 'cn'))
        self.assertIn('Researcher', english)
        self.assertIn('2024&ndash;present', english)
        self.assertIn('研究员 (中文附注)', chinese)
        self.assertIn('2024&ndash;至今', chinese)
        self.assertIn('S&P 2025, 2020', english)
        self.assertIn('奖学金', chinese)
        self.assertNotIn('hidden award', english)
        self.assertNotIn('中文附注', english)
        self.assertNotIn('## Education', english)

    def test_publications_preserve_urls_and_convert_typed_links(self):
        pub = paper(links=[
            {'kind': 'pdf', 'url': 'https://example.org/paper.pdf'},
            {'kind': 'github', 'text': 'Tool', 'url': 'https://github.com/example/tool'},
            {'kind': 'pub', 'url': 'https://example.org/paper'},
            {'kind': 'pub', 'url': 'https://example.org/paper'},
        ], annotations=[{'items': [
            {'text': 'Paper Award', 'red': True},
            {'kind': 'named', 'text': 'Invited Event', 'url': 'https://example.org/event'},
        ]}])
        result = normalize_publications({'publications': [pub]},
                                        {'example-2025': 'existing-public-url'})['publications'][0]
        page = generate_pub_page(result)
        metadata = yaml.safe_load(page.split('---', 2)[1])
        self.assertEqual(metadata['permalink'], '/publication/existing-public-url/')
        self.assertEqual(metadata['redirect_from'], ['/publication/existing-public-url.html'])
        self.assertIn('[📄 PDF](https://example.org/paper.pdf)', page)
        self.assertIn('[🐙 Tool](https://github.com/example/tool)', page)
        self.assertIn('Paper Award', page)
        self.assertIn('[🔗 Invited Event](https://example.org/event)', page)
        self.assertEqual(page.count('[🔗 Publisher]'), 1)
        self.assertEqual(result['year'], 2025)
        self.assertEqual(result['type'], 'conference')

    def test_undated_same_title_papers_get_distinct_urls_without_fake_year(self):
        pubs = [paper(id='example-journal', type='journal'), paper(id='example-2025')]
        normalized = normalize_publications({'publications': pubs}, {})['publications']
        journal, conference = normalized
        self.assertNotEqual(journal['slug'], conference['slug'])
        self.assertEqual(make_filename(journal), '2099-07-01-example-journal.md')
        front_matter, body = generate_pub_page(journal).split('---', 2)[1:]
        self.assertIn('category: manuscripts', front_matter)
        self.assertNotIn('2099', body)
        self.assertNotIn('(2099)', front_matter)

    def test_duplicate_ids_and_urls_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate publication ID'):
            normalize_publications({'publications': [paper(), paper()]}, {})
        with self.assertRaisesRegex(ValueError, 'Duplicate publication slug'):
            normalize_publications({'publications': [paper(), paper(id='other-2024')]},
                                   {'example-2025': 'same', 'other-2024': 'same'})

    def test_sync_uses_custom_source_and_preserves_snapshots_on_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / 'source', root / 'output'
            source.mkdir()
            (source / 'cv.yml').write_text('sections: {}\n', encoding='utf-8')
            (source / 'i18n.yml').write_text('education: {en: Education, zh: 教育}\n', encoding='utf-8')
            pubs = {'publications': [paper()]}
            (source / 'publications.yml').write_text(yaml.safe_dump(pubs), encoding='utf-8')
            urls = root / 'urls.yml'
            urls.write_text('{}\n', encoding='utf-8')
            sync_data(source, output, urls)
            self.assertEqual(yaml.safe_load((output / 'cv.yml').read_text()), {'sections': {}})
            snapshots = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in output.iterdir()}
            sync_data(source, output, urls)
            self.assertEqual(snapshots, {p.name: (p.read_bytes(), p.stat().st_mtime_ns)
                                         for p in output.iterdir()})
            with self.assertRaises(FileNotFoundError):
                sync_data(root / 'missing', output, urls)
            pubs['publications'].append(copy.deepcopy(pubs['publications'][0]))
            (source / 'publications.yml').write_text(yaml.safe_dump(pubs), encoding='utf-8')
            with self.assertRaises(ValueError):
                sync_data(source, output, urls)
            self.assertEqual(snapshots, {p.name: (p.read_bytes(), p.stat().st_mtime_ns)
                                         for p in output.iterdir()})

    def test_talks_and_projects_use_updated_paper_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pub = paper(title='Updated: New Paper Title', year=2025, pdf='https://example.org/new.pdf',
                        github={'Tool': 'https://github.com/example/new'})
            pubs = root / 'publications.yml'
            pubs.write_text(yaml.safe_dump({'publications': [pub]}), encoding='utf-8')
            for collection, script, template, record in (
                ('talks', 'generate_talks.py', 'talk.md.j2', {
                    'publication': pub['id'], 'date': '2025-10-01', 'slug': 'existing-talk',
                    'venue': 'Event', 'location': 'City', 'type': 'Talk', 'excerpt': 'Details',
                }),
                ('projects', 'generate_projects.py', 'project.md.j2', {
                    'publication': pub['id'], 'title': 'Tool', 'slug': 'existing-project',
                    'excerpt': 'Summary', 'description': 'Description', 'features': [], 'tech': [],
                }),
            ):
                data = root / f'{collection}.yml'
                data.write_text(yaml.safe_dump({collection: [record]}), encoding='utf-8')
                output = root / collection
                subprocess.run([sys.executable, str(ROOT / 'scripts' / script),
                                '--data', str(data), '--pubs', str(pubs),
                                '--template', str(ROOT / 'templates' / template),
                                '--output-dir', str(output)], check=True, capture_output=True)
                page = next(output.glob('*.md')).read_text(encoding='utf-8')
                self.assertIn('New Paper Title', page)
                self.assertIn('https://example.org/new.pdf', page)
                if collection == 'projects':
                    self.assertIn('https://github.com/example/new', page)


if __name__ == '__main__':
    unittest.main()

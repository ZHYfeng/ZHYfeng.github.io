#!/usr/bin/env python3
"""
generate_cv_md.py — Generate _pages/cv.md from _data/cv.yml using Jinja2.
"""

import argparse
from pathlib import Path
from jinja2 import Template

from cv_data import load_yaml, localize


def build_context(data, labels, lang):
    lang = 'zh' if lang == 'cn' else lang
    data = localize(data, lang)
    labels = localize(labels, lang)
    sections = data.get('sections', {})
    context = {'labels': labels, 'education': [], 'experience': [],
               'awards': [], 'service': {}}

    def period(entry):
        return {'period_start': entry['start'][:4],
                'period_end': entry['end'][:4] if entry.get('end') else labels['ongoing']}

    for entry in sections.get('education', {}).get('entries', []):
        advisor = entry.get('advisor', {})
        context['education'].append({
            **period(entry), 'degree': entry.get('degree', ''),
            'institution': (', ' if lang == 'en' else '，').join(
                entry[key] for key in ('field', 'institution', 'country', 'location')
                if entry.get(key)),
            'advisor': advisor.get('name', ''), 'advisor_url': advisor.get('url', ''),
            'keywords': [item['text'] for item in entry.get('keywords', [])],
        })
    for entry in sections.get('experience', {}).get('entries', []):
        mentor = entry.get('mentor', {})
        title = entry['role']
        for note in entry.get('role_notes', []):
            title += f" ({note['text']})"
        context['experience'].append({
            **period(entry), 'title': title, 'organization': entry.get('organization', ''),
            'mentor': mentor.get('name', ''), 'mentor_url': mentor.get('url', ''),
            'role': labels.get(mentor.get('kind', ''), '').rstrip(':： '),
            'keywords': [item['text'] for item in entry.get('keywords', [])],
        })
    awards = {}
    for entry in sections.get('awards', {}).get('entries', []):
        awards.setdefault(entry['year'], []).append(entry['text'])
    context['awards'] = [{'year': year, 'items': items} for year, items in awards.items()]
    for entry in sections.get('service', {}).get('entries', []):
        description = ''
        for activity in entry.get('activities', []):
            years = activity.get('years', [])
            if entry.get('year_order'):
                years = sorted(years, reverse=entry['year_order'] == 'descending')
            if description:
                description += activity.get('separator', '. ')
            description += activity['venue'] + ' ' + ', '.join(map(str, years))
            if activity.get('note'):
                description += f" ({activity['note']})"
        context['service'][entry['role']] = description
    return context


CV_TEMPLATE_EN = Template("""---
layout: archive
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<div class="cv-download-links">
  <a href="/files/cv.pdf" class="btn btn--primary">Download CV (EN)</a>
  <a href="/files/cv-cn.pdf" class="btn btn--primary">Download CV (CN)</a>
</div>

{% if education %}
## {{ labels.education }}

{% for edu in education %}
- {% if edu.degree %}**{{ edu.degree }}**{% if edu.institution %}, {% endif %}{% endif %}{% if edu.institution %}{{ edu.institution }}{% endif %} ({{ edu.period_start.split('/')[-1] if edu.period_start and '/' in edu.period_start else edu.period_start }}&ndash;{{ edu.period_end.split('/')[-1] if edu.period_end and '/' in edu.period_end else edu.period_end }})
  {% if edu.advisor %}<br>  {{ labels.advisor }}{% if edu.advisor_url %}[{{ edu.advisor }}]({{ edu.advisor_url }}){% else %}{{ edu.advisor }}{% endif %}{% endif %}
  {% if edu.keywords %}<br>  Focus: {{ edu.keywords | join(', ') }}{% endif %}
{% endfor %}
{% endif %}

{% if experience %}
## {{ labels.experience }}

{% for exp in experience %}
- **{{ exp.title }}**{% if exp.mentor %}, {{ exp.role }}: {% if exp.mentor_url %}[{{ exp.mentor }}]({{ exp.mentor_url }}){% else %}{{ exp.mentor }}{% endif %}{% endif %}{% if exp.organization %}, {{ exp.organization }}{% endif %} ({{ exp.period_start.split('/')[-1] if exp.period_start and '/' in exp.period_start else exp.period_start }}&ndash;{{ exp.period_end.split('/')[-1] if exp.period_end and '/' in exp.period_end else exp.period_end }}){% if exp.keywords %}<br>  Focus: {{ exp.keywords | join(', ') }}{% endif %}
{% endfor %}
{% endif %}

{% if awards %}
## {{ labels.awards }}

{% for award_group in awards %}
- **{{ award_group.year }}**{% for item in award_group['items'] %}
  - {{ item }}{% endfor %}
{% endfor %}
{% endif %}

{% if service %}
## {{ labels.service }}

{% for role, desc in service.items() %}
- **{{ role }}**: {{ desc }}
{% endfor %}
{% endif %}
""")

CV_TEMPLATE_CN = Template("""---
layout: archive
permalink: /cv-cn/
author_profile: true
---

<div class="cv-download-links">
  <a href="/files/cv.pdf" class="btn btn--primary">下载英文简历 (EN)</a>
  <a href="/files/cv-cn.pdf" class="btn btn--primary">下载中文简历 (CN)</a>
</div>

{% if education %}
## {{ labels.education }}

{% for edu in education %}
- {% if edu.degree %}**{{ edu.degree }}**{% if edu.institution %}，{% endif %}{% endif %}{% if edu.institution %}{{ edu.institution }}{% endif %}（{{ edu.period_start.split('/')[-1] if edu.period_start and '/' in edu.period_start else edu.period_start }}&ndash;{{ edu.period_end.split('/')[-1] if edu.period_end and '/' in edu.period_end else edu.period_end }}）
  {% if edu.advisor %}<br>  {{ labels.advisor }}{% if edu.advisor_url %}[{{ edu.advisor }}]({{ edu.advisor_url }}){% else %}{{ edu.advisor }}{% endif %}{% endif %}
  {% if edu.keywords %}<br>  关键词：{{ edu.keywords | join('、') }}{% endif %}
{% endfor %}
{% endif %}

{% if experience %}
## {{ labels.experience }}

{% for exp in experience %}
- **{{ exp.title }}**{% if exp.mentor %}，{{ exp.role }}：{% if exp.mentor_url %}[{{ exp.mentor }}]({{ exp.mentor_url }}){% else %}{{ exp.mentor }}{% endif %}{% endif %}{% if exp.organization %}，{{ exp.organization }}{% endif %}（{{ exp.period_start.split('/')[-1] if exp.period_start and '/' in exp.period_start else exp.period_start }}&ndash;{{ exp.period_end.split('/')[-1] if exp.period_end and '/' in exp.period_end else exp.period_end }}）{% if exp.keywords %}<br>  关键词：{{ exp.keywords | join('、') }}{% endif %}
{% endfor %}
{% endif %}

{% if awards %}
## {{ labels.awards }}

{% for award_group in awards %}
- **{{ award_group.year }}**{% for item in award_group['items'] %}
  - {{ item }}{% endfor %}
{% endfor %}
{% endif %}

{% if service %}
## {{ labels.service }}

{% for role, desc in service.items() %}
- **{{ role }}**：{{ desc }}
{% endfor %}
{% endif %}
""")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, help='Combined cv.yml')
    parser.add_argument('--labels', help='i18n.yml (defaults to the data directory)')
    parser.add_argument('--output', required=True)
    parser.add_argument('--lang', default='en', choices=['en', 'cn'])
    args = parser.parse_args()

    data = load_yaml(args.data)
    labels = load_yaml(args.labels or Path(args.data).with_name('i18n.yml'))
    ctx = build_context(data, labels, args.lang)

    template = CV_TEMPLATE_EN if args.lang == 'en' else CV_TEMPLATE_CN
    md = '\n'.join(line.rstrip() for line in template.render(**ctx).splitlines()) + '\n'

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(md, encoding='utf-8')

    print(f"Generated {args.output} ({args.lang})")


if __name__ == '__main__':
    main()

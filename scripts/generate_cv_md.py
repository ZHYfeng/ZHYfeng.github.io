#!/usr/bin/env python3
"""
generate_cv_md.py — Generate _pages/cv.md from _data/cv.yml using Jinja2.
"""

import argparse
import re
import yaml
from pathlib import Path
from jinja2 import Template


def pick_lang(data, lang):
    if isinstance(data, dict):
        if 'en' in data and 'cn' in data:
            return data.get(lang, data.get('en', ''))
        return {k: pick_lang(v, lang) for k, v in data.items()}
    elif isinstance(data, list):
        return [pick_lang(item, lang) for item in data]
    return data


def clean_md(val):
    """Remove LaTeX escaping for Markdown output."""
    if isinstance(val, str):
        val = val.replace('\\&', '&')
        val = re.sub(r'\\(?:textbf|textit)\{([^}]*)\}', r'\1', val)
        val = val.replace('\\_', '_')
        return val
    if isinstance(val, dict):
        return {k: clean_md(v) for k, v in val.items()}
    if isinstance(val, list):
        return [clean_md(v) for v in val]
    return val


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

<div class="cv-card">

## Education

{% for edu in education %}
- {% if edu.degree %}**{{ edu.degree }}**{% if edu.institution %}, {% endif %}{% endif %}{% if edu.institution %}{{ edu.institution }}{% endif %} ({{ edu.period_start.split('/')[-1] if edu.period_start and '/' in edu.period_start else edu.period_start }}&ndash;{{ edu.period_end.split('/')[-1] if edu.period_end and '/' in edu.period_end else edu.period_end }})
  {% if edu.advisor %}<br>  Advisor: {% if edu.advisor_url %}[{{ edu.advisor }}]({{ edu.advisor_url }}){% else %}{{ edu.advisor }}{% endif %}{% endif %}
  {% if edu.keywords %}<br>  Focus: {{ edu.keywords | join(', ') }}{% endif %}
{% endfor %}

## Professional Experience

{% for exp in experience %}
- **{{ exp.title }}**{% if exp.mentor %}, {{ exp.role }}: {% if exp.mentor_url %}[{{ exp.mentor }}]({{ exp.mentor_url }}){% else %}{{ exp.mentor }}{% endif %}{% endif %}{% if exp.organization %}, {{ exp.organization }}{% endif %} ({{ exp.period_start.split('/')[-1] if exp.period_start and '/' in exp.period_start else exp.period_start }}&ndash;{{ exp.period_end.split('/')[-1] if exp.period_end and '/' in exp.period_end else exp.period_end }}){% if exp.keywords %}<br>  Focus: {{ exp.keywords | join(', ') }}{% endif %}
{% endfor %}

{% if awards %}
## Awards and Honors

{% for award_group in awards %}
- **{{ award_group.year }}**{% for item in award_group['items'] %}
  - {{ item }}{% endfor %}
{% endfor %}
{% endif %}

{% if service %}
## Academic Service

{% for role, desc in service.items() %}
- **{{ role }}**: {{ desc }}
{% endfor %}
{% endif %}
</div>
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

<div class="cv-card">

## 教育经历

{% for edu in education %}
- {% if edu.degree %}**{{ edu.degree }}**{% if edu.institution %}，{% endif %}{% endif %}{% if edu.institution %}{{ edu.institution }}{% endif %}（{{ edu.period_start.split('/')[-1] if edu.period_start and '/' in edu.period_start else edu.period_start }}&ndash;{{ edu.period_end.split('/')[-1] if edu.period_end and '/' in edu.period_end else edu.period_end }}）
  {% if edu.advisor %}<br>  导师：{% if edu.advisor_url %}[{{ edu.advisor }}]({{ edu.advisor_url }}){% else %}{{ edu.advisor }}{% endif %}{% endif %}
{% endfor %}

## 工作经历

{% for exp in experience %}
- **{{ exp.title }}**{% if exp.mentor %}，{{ exp.role }}：{% if exp.mentor_url %}[{{ exp.mentor }}]({{ exp.mentor_url }}){% else %}{{ exp.mentor }}{% endif %}{% endif %}{% if exp.organization %}，{{ exp.organization }}{% endif %}（{{ exp.period_start.split('/')[-1] if exp.period_start and '/' in exp.period_start else exp.period_start }}&ndash;{{ exp.period_end.split('/')[-1] if exp.period_end and '/' in exp.period_end else exp.period_end }}）{% if exp.keywords %}<br>  关键词：{{ exp.keywords | join('、') }}{% endif %}
{% endfor %}

{% if awards %}
## 获奖情况

{% for award_group in awards %}
- **{{ award_group.year }}**{% for item in award_group['items'] %}
  - {{ item }}{% endfor %}
{% endfor %}
{% endif %}

{% if service %}
## 学术服务

{% for role, desc in service.items() %}
- **{{ role }}**：{{ desc }}
{% endfor %}
{% endif %}
</div>
""")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, help='Combined cv.yml')
    parser.add_argument('--output', required=True)
    parser.add_argument('--lang', default='en', choices=['en', 'cn'])
    args = parser.parse_args()

    with open(args.data, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data:
        print(f"Warning: No data in {args.data}")
        return

    # Pick language
    ctx = pick_lang(data, args.lang)

    # Strip LaTeX escaping for Markdown
    ctx = clean_md(ctx)

    template = CV_TEMPLATE_EN if args.lang == 'en' else CV_TEMPLATE_CN
    md = template.render(**ctx)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(md, encoding='utf-8')

    print(f"Generated {args.output} ({args.lang})")


if __name__ == '__main__':
    main()

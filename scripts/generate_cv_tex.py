#!/usr/bin/env python3
"""
generate_cv_tex.py — Generate Yu_Hao-CV.tex from _data/cv.yml + Jinja2 template.

Usage:
    python3 scripts/generate_cv_tex.py \
        --data _data/cv.yml \
        --pubs _data/publications.yml \
        --template templates/cv_en.tex.j2 --lang en \
        --output ../CV/Yu_Hao-CV.tex

    python3 scripts/generate_cv_tex.py \
        --data _data/cv.yml \
        --pubs _data/publications.yml \
        --template templates/cv_cn.tex.j2 --lang cn \
        --output ../CV/Yu_Hao-CV-CN.tex
"""

import argparse
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def pick_lang(data, lang):
    """Walk the data structure and pick language-specific fields.

    For dicts with 'en'/'cn' keys, pick the matching language.
    For lists, recurse into each element.
    Otherwise, return the value as-is.
    """
    if isinstance(data, dict):
        if 'en' in data and 'cn' in data:
            # This is a language-specific field
            return data.get(lang, data.get('en', ''))
        return {k: pick_lang(v, lang) for k, v in data.items()}
    elif isinstance(data, list):
        return [pick_lang(item, lang) for item in data]
    return data


def build_context(sections, publications, lang):
    """Build rendering context with language selected."""
    ctx = pick_lang(sections, lang)
    ctx['publications'] = publications.get('publications', [])
    return ctx


def clean_context(ctx):
    """Remove stray {{ }} from string values (leftover LaTeX artifacts)."""
    if isinstance(ctx, dict):
        return {k: clean_context(v) for k, v in ctx.items()}
    elif isinstance(ctx, list):
        return [clean_context(item) for item in ctx]
    elif isinstance(ctx, str):
        return ctx.replace('{{', '').replace('}}', '')
    return ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, help='Combined cv.yml')
    parser.add_argument('--pubs', required=True, help='Publications YAML')
    parser.add_argument('--template', required=True, help='Jinja2 template')
    parser.add_argument('--lang', default='en', choices=['en', 'cn'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    sections = load_yaml(args.data)
    publications = load_yaml(args.pubs)

    ctx = build_context(sections, publications, args.lang)
    ctx = clean_context(ctx)

    template_path = Path(args.template)
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)

    output = template.render(**ctx)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(output, encoding='utf-8')

    print(f"Generated {args.output} ({args.lang})")


if __name__ == '__main__':
    main()

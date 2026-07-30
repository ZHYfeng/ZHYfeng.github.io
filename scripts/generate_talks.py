"""Generate talk pages from YAML data using Jinja2 template."""

import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def load_yaml(path):
    import yaml
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def clean_latex(text):
    if not text:
        return text
    import re
    text = text.replace('\\&', '&')
    text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textit\{([^}]*)\}', r'\1', text)
    text = text.replace('\\_', '_')
    return text


def main():
    parser = argparse.ArgumentParser(description='Generate talk pages')
    parser.add_argument('--data', required=True, help='Talks YAML file')
    parser.add_argument('--template', required=True, help='Jinja2 template file')
    parser.add_argument('--output-dir', required=True, help='Output directory for talk pages')
    args = parser.parse_args()

    data = load_yaml(args.data)
    talks = data.get('talks', [])

    template_path = Path(args.template)
    env = Environment(loader=FileSystemLoader(template_path.parent))
    env.filters['clean_latex'] = clean_latex
    template = env.get_template(template_path.name)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clean old talk files
    for old in out_dir.glob('*.md'):
        old.unlink()

    for talk in talks:
        # Clean LaTeX-escaped fields
        for field in ('title', 'venue', 'location'):
            if talk.get(field):
                talk[field] = clean_latex(talk[field])

        slug = talk['slug']
        # Look up paper URL from publications if available
        talk['paper'] = talk.get('paper', '')
        talk['slides'] = talk.get('slides', '')
        talk['video'] = talk.get('video', '')

        output = template.render(talk=talk)
        filename = f"{talk['date']}-{slug}.md"
        out_path = out_dir / filename
        out_path.write_text(output, encoding='utf-8')

    print(f"✅ Generated {len(talks)} talk files in {out_dir}")


if __name__ == '__main__':
    main()

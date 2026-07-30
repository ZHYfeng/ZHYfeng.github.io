"""Generate publications listing page from YAML data using Jinja2 template.

Usage:
    python3 generate_pub_list.py --data publications.yml --template template.j2 --output _pages/publications.md
"""

import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def load_yaml(path):
    import yaml
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def bold_self(text, name='Yu Hao'):
    """Bold the given name in a string (Markdown formatting)."""
    if not text:
        return text
    return text.replace(name, f'**{name}**')


def main():
    parser = argparse.ArgumentParser(description='Generate publications listing page')
    parser.add_argument('--data', required=True, help='Publications YAML file')
    parser.add_argument('--template', required=True, help='Jinja2 template file')
    parser.add_argument('--output', required=True, help='Output file path')
    args = parser.parse_args()

    data = load_yaml(args.data)
    publications = data.get('publications', [])

    template_path = Path(args.template)
    env = Environment(loader=FileSystemLoader(template_path.parent))
    env.filters['bold_self'] = bold_self
    template = env.get_template(template_path.name)

    output = template.render(publications=publications)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(output, encoding='utf-8')

    print(f"Generated {args.output}")


if __name__ == '__main__':
    main()

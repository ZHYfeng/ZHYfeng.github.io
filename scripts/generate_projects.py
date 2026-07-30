"""Generate portfolio/project pages from YAML data using Jinja2 template."""

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
    parser = argparse.ArgumentParser(description='Generate project/portfolio pages')
    parser.add_argument('--data', required=True, help='Projects YAML file')
    parser.add_argument('--template', required=True, help='Jinja2 template file')
    parser.add_argument('--output-dir', required=True, help='Output directory for project pages')
    args = parser.parse_args()

    data = load_yaml(args.data)
    projects = data.get('projects', [])

    template_path = Path(args.template)
    env = Environment(loader=FileSystemLoader(template_path.parent))
    env.filters['clean_latex'] = clean_latex
    template = env.get_template(template_path.name)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clean old project files
    for old in out_dir.glob('*.md'):
        old.unlink()

    for project in projects:
        for field in ('title', 'tagline', 'excerpt', 'description', 'award'):
            if project.get(field):
                project[field] = clean_latex(project[field])

        output = template.render(project=project)
        filename = f"{project['year']}-07-01-{project['slug']}.md"
        out_path = out_dir / filename
        out_path.write_text(output, encoding='utf-8')

    print(f"✅ Generated {len(projects)} project files in {out_dir}")


if __name__ == '__main__':
    main()

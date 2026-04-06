---
name: copilot-instructions
description: Workspace instructions for Academic Pages Jekyll site. Use when: working with Jekyll content (posts, publications, talks), configuring the site, building or running locally, generating markdown from structured data, or customizing layouts and styling.
---

# ZHYfeng.github.io – Copilot Instructions

This is a Jekyll-based academic portfolio site built with the [Academic Pages](https://academicpages.github.io/) template.

## Quick Start

**Run locally:**
```bash
# Option 1: Ruby + Bundler (Linux/macOS)
bundle install
jekyll serve -l -H localhost  # or: bundle exec jekyll serve -l -H localhost

# Option 2: Docker
chmod -R 777 .
docker compose up
```
Site will be available at `http://localhost:4000` with live reload.

**Build JavaScript assets:**
```bash
npm run build:js      # Production build (minified)
npm run watch:js      # Watch for changes during development
```

## Project Structure

### Content Directories (What to Edit)

| Path | Purpose | File Naming |
|------|---------|-------------|
| `_posts/` | Blog posts | `YYYY-MM-DD-slug.md` |
| `_publications/` | Academic papers & publications | `YYYY-MM-DD-slug.md` |
| `_talks/` | Conference talks & tutorials | `YYYY-MM-DD-slug.md` |
| `_portfolio/` | Portfolio projects | `slug.md` (no date) |
| `_pages/` | Static pages (about, CV, archive views) | `slug.md` or `.html` |
| `_drafts/` | Draft posts (not published) | Any naming convention |
| `files/` | Downloadable resources (PDFs, code, etc.) | Any naming; accessible at `/files/filename` |

### Configuration & Data Files (Site Config)

| File | Purpose |
|------|---------|
| `_config.yml` | **Main site config** – title, URL, author profile, theme, publication categories, disqus/utterances, google analytics |
| `_config_docker.yml` | Docker-specific overrides (merged with `_config.yml`) |
| `_data/navigation.yml` | Site navigation menu links |
| `_data/authors.yml` | Author profiles (if multi-author site) |
| `_data/cv.json` | Structured CV data |
| `_data/ui-text.yml` | Customizable UI text strings |

### Template & Layout Files (Advanced)

| Path | Purpose |
|------|---------|
| `_layouts/` | Page templates (default, single, cv-layout, talk, splash) |
| `_includes/` | Reusable template partials (header, footer, sidebar, comment providers) |
| `_sass/` | SCSS stylesheets (themes, syntax highlighting, layouts) |
| `assets/` | Images, JavaScript, CSS (generated from SCSS) |

## Content Front Matter

### Blog Post (`_posts/YYYY-MM-DD-slug.md`)
```yaml
---
title: 'Post Title Here'
date: YYYY-MM-DD
permalink: /posts/YYYY/MM/slug/
tags:
  - tag1
  - tag2
excerpt: 'Optional excerpt'
---
```

### Publication (`_publications/YYYY-MM-DD-slug.md`)
```yaml
---
title: "Paper Title"
collection: publications
category: manuscripts  # or: conferences, books
permalink: /publication/YYYY-MM-DD-slug
excerpt: 'Brief summary'
date: YYYY-MM-DD
venue: 'Journal or Conference Name'
paperurl: 'https://...'  # DOI or direct link
citation: 'Citation as it should appear'
---
```

### Talk (`_talks/YYYY-MM-DD-slug.md`)
```yaml
---
title: "Talk Title"
collection: talks
type: "Talk"  # or: Tutorial
permalink: /talks/YYYY-MM-DD-slug
venue: "Conference or Organization Name"
date: YYYY-MM-DD
location: "City, Country"
---
```

### Page (`_pages/slug.md`)
```yaml
---
permalink: /path/
author_profile: true   # Show sidebar with author info
title: "Page Title"
---
```

## Bulk Content Generation

Use markdown generators in `markdown_generator/` to convert structured data into Jekyll-formatted content:

- **`publications.py`** – Convert CSV/TSV to publication markdown (with Python or Jupyter notebook)
- **`talks.py`** – Convert TSV to talk markdown
- **`PubsFromBib.ipynb`** – Convert BibTeX to publication markdown
- **`OrcidToBib.ipynb`** – Convert ORCID profile to BibTeX then publications

Example:
```bash
python3 markdown_generator/publications.py markdown_generator/publications.tsv
```

## Site Configuration (Key Settings in `_config.yml`)

**Essential to customize:**
- `site_title` – Your name/site title
- `url` – Must match your GitHub Pages URL: `https://[username].github.io`
- `repository` – Must be correct for GitHub Pages: `[username]/[username].github.io`
- `author.name`, `author.bio`, `author.avatar` – Your profile info
- `author.social_links` – Links to your social/academic profiles
- `site_theme` – Visual theme (default, air, sunrise, mint, dirt, contrast)

**Content settings:**
- `collections_dir` – Default: `. (root)`
- `collections.publications.output`, `.talks.output`, `.portfolio.output` – Set to `true` to generate pages
- `google_analytics_id` – Add analytics tracking (optional)
- `comments.provider` – Choose disqus, utterances, etc. (optional)

See [Academic Pages docs](https://academicpages.github.io/) for full reference.

## Common Workflows

### Creating a new post/publication/talk
1. Create file in appropriate directory with correct naming: `YYYY-MM-DD-slug.md`
2. Add front matter with `title`, `date`, `collection` (if not post), and any other metadata
3. Write content in Markdown
4. Run `jekyll serve` and preview at `localhost:4000`
5. Commit and push to GitHub

### Updating site title, theme, or config
1. Edit `_config.yml`
2. **Restart Jekyll** (changes to config require restart, unlike `.md` files)
3. Preview at `localhost:4000`

### Customizing author profile or navigation
1. Edit `_config.yml` (author section) or `_data/navigation.yml` (menu links)
2. Restart Jekyll if needed
3. Changes appear in sidebar and header

### Adding downloadable resources
1. Place file (PDF, code, etc.) in `files/` directory
2. Reference in your content as `/files/filename`
3. Files are automatically accessible via GitHub Pages

## Deployment & CI

- **Hosting**: GitHub Pages (automatic)
- **Repository**: Must be named `[your-username].github.io`
- **Auto-deploy**: Push to `master` branch → GitHub Actions builds and deploys
- **Status**: Check in repo settings → GitHub Pages section

## Local Development Tips

- **Live reload**: Markdown and HTML files auto-refresh; CSS/JS rebuild typically within seconds
- **Full rebuild needed** when: changing `_config.yml`, modifying layouts, or major SCSS changes
- **Docker advantage**: Isolated environment, no local Ruby/Bundler setup needed
- **Dev Container**: VS Code auto-detects and offers containerization (F1 → DevContainer: Reopen in Container)

## References & Resources

- [Academic Pages Documentation](https://academicpages.github.io/) – Complete template guide
- [Jekyll Documentation](https://jekyllrb.com/) – Jekyll core features and Liquid templating
- [README.md](../README.md) – Setup instructions (Ruby, macOS, WSL, Docker, Dev Container)
- [CONTRIBUTING.md](../CONTRIBUTING.md) – Contribution guidelines for template improvements

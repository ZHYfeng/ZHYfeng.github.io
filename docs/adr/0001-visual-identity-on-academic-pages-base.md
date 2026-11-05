---
status: accepted
---

# Build the visual identity on top of the Academic Pages base, not a new theme

The site looked like every other Academic Pages deployment (Source Serif + Libre Franklin, teal accent, shadowed cards). We decided to keep the Academic Pages base and express a site-wide visual identity by overriding the Sass tokens (type, colour, radius, shadow) in `_sass` and owning the homepage layout in `_layouts/home.html`, rather than switching to or writing a custom theme. GitHub Pages' built-in Jekyll build, the light/dark toggle, Font Awesome and the CV-to-site data sync (`Makefile`, `scripts/`) are all wired to this base; a theme swap would cost a week for no gain in identity.

## Consequences

- Identity lives in tokens plus the homepage: every new token must be defined for both light and dark themes.
- Other pages keep their structure and change only through tokens.
- Direction chosen: code/kernel texture (monospace labels) and a bilingual signature (郝宇 as the hero's visual anchor) on an editorial-minimal base; dark-first was rejected.

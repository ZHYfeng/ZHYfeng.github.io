# Makefile — YAML-as-source CV + Website pipeline
# =================================================
# Source of truth:  _data/cv_sections.yml, _data/cv_sections_cn.yml, _data/publications.yml
# Generated:        ../CV/Yu_Hao-CV.tex → PDF, _pages/cv.md, _publications/*.md
#
# Usage:
#   make all         Full pipeline (YAML → LaTeX → PDF → web pages)
#   make web         Web only (skip LaTeX/PDF)
#   make cv          LaTeX + PDF only
#   make quick       Regenerate web from existing YAML (1s)
#   make serve       Local Jekyll preview
#   make deploy      Git commit + push
#   make migrate     First-time: extract LaTeX CV → YAML (one-time)

CV_DIR = ../CV

# ── Source YAML (the truth) ──
CV_YML            = _data/cv.yml
PUBS_YML          = _data/publications.yml

# ── Generated files ──
CV_TEX_OUT      = $(CV_DIR)/Yu_Hao-CV.tex
CV_TEX_CN_OUT   = $(CV_DIR)/Yu_Hao-CV-CN.tex
CV_PDF          = $(CV_DIR)/Yu_Hao-CV.pdf
CV_PDF_CN       = $(CV_DIR)/Yu_Hao-CV-CN.pdf
CV_PAGE         = _pages/cv.md
CV_PAGE_CN      = _pages/cv-cn.md
PUB_PAGE        = _pages/publications.md
PUB_DIR         = _publications

# ── Templates ──
PUB_MD_TMPL      = $(TEMPLATE_DIR)/publications.md.j2
TEMPLATE_DIR     = templates
CV_TEX_TMPL      = $(TEMPLATE_DIR)/cv_en.tex.j2
CV_TEX_CN_TMPL   = $(TEMPLATE_DIR)/cv_cn.tex.j2

# ── Scripts ──
GEN_CV_TEX       = scripts/generate_cv_tex.py
GEN_CV_MD        = scripts/generate_cv_md.py
GEN_PUB_PAGES    = scripts/generate_pub_pages.py
GEN_PUB_LIST     = scripts/generate_pub_list.py
EXTRACT_SECTIONS = scripts/extract_cv_sections.py
EXTRACT_PUBS     = scripts/extract_publications.py

.PHONY: all web cv quick migrate serve deploy clean help

all: web cv-pdf
	@echo ""
	@echo "╔══════════════════════════════════════════════════════╗"
	@echo "║  ✅  全部同步完成（YAML → LaTeX → PDF → Web）      ║"
	@echo "╚══════════════════════════════════════════════════════╝"

# ── Web content (always available, no LaTeX needed) ──
web: sync-web-pages
	@echo "✅ Web content generated from YAML"

sync-web-pages: $(CV_PAGE) $(CV_PAGE_CN) $(PUB_PAGE) sync-pub-pages

$(CV_PAGE): $(CV_YML) $(GEN_CV_MD)
	python3 $(GEN_CV_MD) --data $(CV_YML) --lang en --output $@

$(CV_PAGE_CN): $(CV_YML) $(GEN_CV_MD)
	python3 $(GEN_CV_MD) --data $(CV_YML) --lang cn --output $@

$(PUB_PAGE): $(PUBS_YML) $(PUB_MD_TMPL) $(GEN_PUB_LIST)
	python3 $(GEN_PUB_LIST) --data $(PUBS_YML) --template $(PUB_MD_TMPL) --output $@

.PHONY: sync-pub-pages
sync-pub-pages: $(PUBS_YML) $(GEN_PUB_PAGES)
	rm -f $(PUB_DIR)/*.md
	python3 $(GEN_PUB_PAGES) --data $(PUBS_YML) --output-dir $(PUB_DIR)

$(PUB_DIR): sync-pub-pages

# ── LaTeX CV → PDF ──
cv: $(CV_TEX_OUT) $(CV_TEX_CN_OUT)
	@echo "✅ LaTeX sources generated from YAML"

cv-pdf: cv
	@echo "📄 Compiling LaTeX CV (xelatex)..."
	@cd $(CV_DIR) && xelatex -interaction=nonstopmode Yu_Hao-CV.tex > /dev/null 2>&1; \
	  if [ -f Yu_Hao-CV.pdf ]; then cp Yu_Hao-CV.pdf ../ZHYfeng.github.io/files/cv.pdf; echo "✅ EN PDF"; \
	  else echo "⚠️  EN PDF failed"; grep "^!" Yu_Hao-CV.log 2>/dev/null | head -5; fi
	@cd $(CV_DIR) && xelatex -interaction=nonstopmode Yu_Hao-CV-CN.tex > /dev/null 2>&1; \
	  if [ -f Yu_Hao-CV-CN.pdf ]; then cp Yu_Hao-CV-CN.pdf ../ZHYfeng.github.io/files/cv-cn.pdf; echo "✅ CN PDF"; \
	  else echo "⚠️  CN PDF failed"; grep "^!" Yu_Hao-CV-CN.log 2>/dev/null | head -5; fi

$(CV_TEX_OUT): $(CV_YML) $(PUBS_YML) $(CV_TEX_TMPL) $(GEN_CV_TEX)
	python3 $(GEN_CV_TEX) --data $(CV_YML) --pubs $(PUBS_YML) --template $(CV_TEX_TMPL) --lang en --output $@

$(CV_TEX_CN_OUT): $(CV_YML) $(PUBS_YML) $(CV_TEX_CN_TMPL) $(GEN_CV_TEX)
	python3 $(GEN_CV_TEX) --data $(CV_YML) --pubs $(PUBS_YML) --template $(CV_TEX_CN_TMPL) --lang cn --output $@

# ── Quick: regenerate web from existing YAML (fastest) ──
quick: sync-web-pages
	@echo "✅ Quick sync (1s)"

# ── One-time migration: extract existing LaTeX CV → YAML ──
migrate:
	@echo "📋 Extracting existing LaTeX CV into YAML..."
	python3 $(EXTRACT_SECTIONS) --tex $(CV_DIR)/Yu_Hao-CV.tex --output /tmp/_cv_en.yml
	python3 $(EXTRACT_SECTIONS) --tex $(CV_DIR)/Yu_Hao-CV-CN.tex --lang cn --output /tmp/_cv_cn.yml
	python3 $(EXTRACT_PUBS) --tex $(CV_DIR)/Yu_Hao-CV.tex --output $(PUBS_YML)
	python3 scripts/merge_cv_langs.py --en /tmp/_cv_en.yml --cn /tmp/_cv_cn.yml --output $(CV_YML)
	rm -f /tmp/_cv_en.yml /tmp/_cv_cn.yml
	@echo ""
	@echo "✅ Migration complete. YAML files created."
	@echo "   From now on, edit _data/cv.yml and run 'make all'."

# ── Local preview ──
serve:
	bundle exec jekyll serve -l -H localhost

# ── Deploy ──
deploy:
	git add -A
	git status
	@read -p "Commit message: " msg; \
	git commit -m "$$msg" && git push
	@echo "✅ Pushed to GitHub Pages"

# ── Clean ──
clean:
	rm -rf $(PUB_DIR)/*.md $(CV_PAGE) $(CV_PAGE_CN) $(PUB_PAGE)
	rm -f $(CV_DIR)/Yu_Hao-CV.tex $(CV_DIR)/Yu_Hao-CV-CN.tex _data/cv.json

# ── Help ──
help:
	@echo "Usage:"
	@echo "  make all           Full pipeline (YAML → LaTeX → PDF → web)"
	@echo "  make web           Web only (skip LaTeX/PDF)"
	@echo "  make cv            Generate LaTeX .tex from YAML"
	@echo "  make cv-pdf        Generate + compile PDF"
	@echo "  make quick         Regenerate web from existing YAML (1s)"
	@echo "  make migrate       One-time: extract LaTeX CV → YAML"
	@echo "  make serve         Local Jekyll preview"
	@echo "  make deploy        Git commit + push"
	@echo "  make clean         Remove generated web files"

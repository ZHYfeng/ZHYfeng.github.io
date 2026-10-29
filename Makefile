# CV/data is the source of truth; _data/cv.yml, i18n.yml and publications.yml
# are committed snapshots so GitHub Pages can build without the CV checkout.
PYTHON ?= python3
CV_DIR ?= ../CV
CV_DATA_DIR ?= $(CV_DIR)/data

CV_YML = _data/cv.yml
PUBS_YML = _data/publications.yml
I18N_YML = _data/i18n.yml
CV_PAGE = _pages/cv.md
CV_PAGE_CN = _pages/cv-cn.md
PUB_PAGE = _pages/publications.md
PUB_DIR = _publications
TALK_DIR = _talks
PROJ_DIR = _portfolio
TEMPLATE_DIR = templates
SHARED_DATA = scripts/cv_data.py

.PHONY: all web quick sync-data sync-web-pages generated-web sync-pub-pages \
        sync-talks sync-projects cv cv-pdf serve deploy clean help test

all: web cv-pdf

web quick: sync-web-pages

# Read snapshot timestamps after synchronization completes, even with make -j.
sync-web-pages: sync-data
	$(MAKE) generated-web

sync-data:
	$(PYTHON) scripts/sync_cv_data.py --data-dir "$(CV_DATA_DIR)"

generated-web: $(CV_PAGE) $(CV_PAGE_CN) $(PUB_PAGE) sync-pub-pages sync-talks sync-projects

$(CV_PAGE): $(CV_YML) $(I18N_YML) scripts/generate_cv_md.py $(SHARED_DATA)
	$(PYTHON) scripts/generate_cv_md.py --data $(CV_YML) --lang en --output $@

$(CV_PAGE_CN): $(CV_YML) $(I18N_YML) scripts/generate_cv_md.py $(SHARED_DATA)
	$(PYTHON) scripts/generate_cv_md.py --data $(CV_YML) --lang cn --output $@

$(PUB_PAGE): $(PUBS_YML) $(TEMPLATE_DIR)/publications.md.j2 scripts/generate_pub_list.py
	$(PYTHON) scripts/generate_pub_list.py --data $(PUBS_YML) --template $(TEMPLATE_DIR)/publications.md.j2 --output $@

sync-pub-pages: $(PUBS_YML) scripts/generate_pub_pages.py
	$(PYTHON) scripts/generate_pub_pages.py --data $(PUBS_YML) --output-dir $(PUB_DIR)

sync-talks: _data/talks.yml $(PUBS_YML) scripts/generate_talks.py $(SHARED_DATA) $(TEMPLATE_DIR)/talk.md.j2
	$(PYTHON) scripts/generate_talks.py --data _data/talks.yml --pubs $(PUBS_YML) --template $(TEMPLATE_DIR)/talk.md.j2 --output-dir $(TALK_DIR)

sync-projects: _data/projects.yml $(PUBS_YML) scripts/generate_projects.py $(SHARED_DATA) $(TEMPLATE_DIR)/project.md.j2
	$(PYTHON) scripts/generate_projects.py --data _data/projects.yml --pubs $(PUBS_YML) --template $(TEMPLATE_DIR)/project.md.j2 --output-dir $(PROJ_DIR)

# Let the CV repository own its LaTeX generation and PDF compilation.
cv:
	$(MAKE) -C "$(CV_DIR)" tex PYTHON="$(PYTHON)"

cv-pdf:
	$(MAKE) -C "$(CV_DIR)" pdf PYTHON="$(PYTHON)"
	cp "$(CV_DIR)/Yu_Hao-CV.pdf" files/cv.pdf
	cp "$(CV_DIR)/Yu_Hao-CV-CN.pdf" files/cv-cn.pdf

test:
	$(PYTHON) -m unittest discover -s tests -v

serve:
	bundle exec jekyll serve -l -H localhost

deploy:
	git add -A
	git status
	@read -p "Commit message: " msg; \
	git commit -m "$$msg" && git push

clean:
	rm -f $(PUB_DIR)/*.md $(TALK_DIR)/*.md $(PROJ_DIR)/*.md $(CV_PAGE) $(CV_PAGE_CN) $(PUB_PAGE)

help:
	@echo "make quick / web   Sync CV/data and regenerate website pages"
	@echo "make sync-data     Update committed data snapshots only"
	@echo "make all           Generate website and compile/copy CV PDFs"
	@echo "make cv            Generate LaTeX using the CV repository"
	@echo "make cv-pdf        Compile and copy both CV PDFs"
	@echo "make test          Check CV data synchronization and rendering"
	@echo "make serve         Local Jekyll preview"
	@echo "make clean         Remove generated website pages"
	@echo "Override source:   make quick CV_DATA_DIR=/path/to/CV/data"

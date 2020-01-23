CONDA_ENV = open-life-science-website

CONDA = $(shell which conda)
ifeq ($(CONDA),)
	CONDA=${HOME}/miniconda3/bin/conda
endif

default: help

clean: ## cleanup the project
	@rm -rf _site
	@rm -rf .sass-cache
	@rm -rf .bundle
	@rm -rf vendor
.PHONY: clean

create-env: ## create conda environment
	if ${CONDA} env list | grep '^${CONDA_ENV}'; then \
	    ${CONDA} env update -f environment.yml; \
	else \
	    ${CONDA} env create -f environment.yml; \
	fi
.PHONY: create-env

ACTIVATE_ENV = source $(dir ${CONDA})activate ${CONDA_ENV}
install: clean ## install dependencies
	$(ACTIVATE_ENV) && \
		gem install bundler && \
		bundle install
.PHONY: install

serve: ## run a local server
	$(ACTIVATE_ENV) && \
		bundle exec jekyll serve
.PHONY: serve

build: clean ## build files but do not run a server (You can specify FLAGS= to pass additional flags to Jekyll)
	$(ACTIVATE_ENV) && \
		bundle exec jekyll build --strict_front_matter
.PHONY: build

check-html: build ## validate HTML
	$(ACTIVATE_ENV) && \
	  	htmlproofer \
	      	--assume-extension \
	      	--http-status-ignore 405,503,999 \
	      	--url-ignore "/.*localhost.*/","/.*gitter\.im.*/" \
	      	--allow-hash-href \
			--empty_alt_ignore \
	      	./_site
.PHONY: check-html

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

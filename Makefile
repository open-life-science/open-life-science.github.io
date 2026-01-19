CONDA_ENV=ols-website
SHELL=bash
UNAME := $(shell uname)

ifeq ($(UNAME),Darwin)
	ENV_FILE=environment-osx.yml
else
	ENV_FILE=environment.yml
endif

CONDA = $(shell which conda)
ifeq ($(CONDA),)
	CONDA=${HOME}/miniconda3/bin/conda
endif
CONDA_BASE ?= $(shell ${CONDA} info --base)

default: help

clean: ## cleanup the project
	@rm -rf _site
	@rm -rf .sass-cache
	@rm -rf .bundle
	@rm -rf vendor
.PHONY: clean

create-env: ## create conda environment
	if ${CONDA} env list | grep '^${CONDA_ENV}'; then \
	    ${CONDA} env update -f ${ENV_FILE}; \
	else \
	    ${CONDA} env create -f ${ENV_FILE}; \
	fi
.PHONY: create-env

ACTIVATE_ENV = source $(CONDA_BASE)/etc/profile.d/conda.sh && conda activate ${CONDA_ENV} && export PATH="$(CONDA_BASE)/envs/$(CONDA_ENV)/bin:$$PATH"
install: clean ## install dependencies
	$(ACTIVATE_ENV) && \
		bundle install
.PHONY: install

install-codespaces: clean ## install dependencies for GitHub Codespaces (fixes nokogiri compilation)
	$(ACTIVATE_ENV) && \
		export LDFLAGS="-L$$CONDA_PREFIX/lib -Wl,-rpath,$$CONDA_PREFIX/lib" && \
		export CPPFLAGS="-I$$CONDA_PREFIX/include" && \
		export LIBS="-liconv" && \
		bundle install
.PHONY: install-codespaces

bundle-install: clean  ## install gems if Ruby is already present (e.g. on gitpod.io)
	bundle install
.PHONY: bundle-install

serve: ## run a local server
	$(ACTIVATE_ENV) && \
		bundle exec jekyll serve
.PHONY: serve

serve-gitpod: ## run a server on a gitpod.io environment
	bundle exec jekyll serve
.PHONY: serve-gitpod

serve-codespaces: ## run a local server in GitHub Codespaces
	$(ACTIVATE_ENV) && \
		bundle exec jekyll serve --host 0.0.0.0
.PHONY: serve-codespaces

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
	      	--disable-external \
	      	./_site
.PHONY: check-html

check-links: build ## check all links
	$(ACTIVATE_ENV) && \
	  	htmlproofer \
	      	--assume-extension \
			--allow-hash-href \
			--ignore_empty_alt \
			--disable-external \
			--ignore_status_codes 405,429,503,999 \
			--allow_missing_href \
			--no-enforce_https \
			--no-check-internal-hash \
			./_site
.PHONY: check-html

update-schedule: ## update schedule
	$(ACTIVATE_ENV) && \
		bash bin/update_schedule.sh
.PHONY: build

lint: clean ## lint python script
	$(ACTIVATE_ENV) && \
		tox -e lint
.PHONY: build

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

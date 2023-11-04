.PHONY: help

build-env: ## Build the virtual environment
	poetry env use python3 && poetry install

exit:
	exit

help: 
	@fgrep -h '##' $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
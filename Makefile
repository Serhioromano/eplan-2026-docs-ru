.PHONY: deploy init serve gitc log

serve:
	@echo "Starting the MkDocs server..."
	@source .env && mkdocs serve

log:
	@echo "Starting the MkDocs server..."
	@source ./.env && mkdocs serve 2>&1 | tee mkdocs.log

init: gitc
	@echo "Start PIP configuration"
	@pip install --upgrade pip
	@pip3 install mkdocs
	@pip3 install mkdocs-material
	@pip3 install mkdocs-git-authors-plugin
	@pip3 install mkdocs-git-revision-date-localized-plugin
	@pip3 install mkdocs-git-committers-plugin
	@echo "Configuration is done"

gitc:
	git config pull.rebase false
	git config --global user.name "Serhioromano"
	git config --global user.email "Serhioromano@outlook.com"

deploy:
	@echo "Deploying the application..."
	@mkdocs gh-deploy
	@echo "Deployment complete."
SEMESTER=2020sp

BLUE=\033[0;34m
NOCOLOR=\033[0m

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  build         to build locally."
	@echo "  serve         to serve locally (assumes OS X)."
	@echo "  deploy        to deploy the website into production."
	@echo "  clean         to remove all generated files."

build:
	bundle exec jekyll build

serve:
	sleep 5 && open http://localhost:4000 &
	bundle exec jekyll serve -l --config _config.yml,_config.dev.yml

clean:
	rm -rf _site

deploy:
	@echo "${BLUE}REMINDER: always 'make build' or 'make serve' before deploying.${NOCOLOR}"
	@echo ""
	@echo "${BLUE}Deploying to production.${NOCOLOR}"
	@echo "${BLUE}=================================${NOCOLOR}"
	./deploy.sh
	@echo ""
	@echo "${BLUE}Done.${NOCOLOR}"

reopen:
	open http://127.0.0.1:4000/courses/cs3110/${SEMESTER}/


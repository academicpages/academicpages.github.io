_config.local.yml: _config.yml
	./build-local-yml.py

build: _config.local.yml
	bundle exec jekyll build -I --config _config.local.yml

lserve: _config.local.yml
	bundle exec jekyll liveserve -I --config _config.local.yml

serve:
	bundle exec jekyll liveserve

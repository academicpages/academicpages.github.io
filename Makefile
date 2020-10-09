build:
	bundle exec jekyll build -I --config _config.local.yml

lserve:
	bundle exec jekyll liveserve -I --config _config.local.yml

serve:
	bundle exec jekyll liveserve

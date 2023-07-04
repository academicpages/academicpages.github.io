ARG RUBY_VERSION
FROM ruby:$RUBY_VERSION-slim
RUN set -ex \
  && gem update --system --silent --quiet \
  && apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y \
    build-essential \
    git \
    libcurl4-openssl-dev \
  && apt-get clean
WORKDIR /app/github-pages-health-check
COPY Gemfile .
COPY github-pages-health-check.gemspec .
COPY lib/github-pages-health-check/version.rb lib/github-pages-health-check/version.rb
RUN bundle install
COPY . .
ENTRYPOINT [ "/bin/bash" ]

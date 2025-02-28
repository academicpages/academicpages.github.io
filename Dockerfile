# Base image: Ruby with necessary dependencies for Jekyll
FROM ruby:3.2

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy all files into the container (necessary for `bundle install`)
COPY . .

# Install bundler and dependencies
RUN gem install bundler:2.3.26 && bundle install

# expose the port 4000
EXPOSE 4000

# Command to serve the Jekyll site
CMD ["jekyll", "serve", "-H", "0.0.0.0", "-w", "--config", "_config.dev.yml,_config.yml"]
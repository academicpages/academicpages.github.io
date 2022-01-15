# frozen_string_literal: true

require "fileutils"
require "net/http"
require "uri"
require "ostruct"
require "json"
require "digest"

##
# A Liquid tag plugin for Jekyll that renders Tweets from Twitter API.
# https://github.com/rob-murray/jekyll-twitter-plugin
#
module TwitterJekyll
  VERSION = "2.0.0".freeze
  REFER_TO_README   = "Please see 'https://github.com/rob-murray/jekyll-twitter-plugin' for usage.".freeze
  LIBRARY_VERSION   = "jekyll-twitter-plugin-v#{VERSION}".freeze
  REQUEST_HEADERS   = { "User-Agent" => LIBRARY_VERSION }.freeze

  # TODO: remove after deprecation cycle
  CONTEXT_API_KEYS  = %w(consumer_key consumer_secret access_token access_token_secret).freeze
  ENV_API_KEYS      = %w(TWITTER_CONSUMER_KEY TWITTER_CONSUMER_SECRET TWITTER_ACCESS_TOKEN TWITTER_ACCESS_TOKEN_SECRET).freeze

  # Cache class that writes to filesystem
  # TODO: Do i really need to cache?
  # @api private
  class FileCache
    def initialize(path)
      @cache_folder = File.expand_path path
      FileUtils.mkdir_p @cache_folder
    end

    def read(key)
      file_to_read = cache_file(key)
      JSON.parse(File.read(file_to_read)) if File.exist?(file_to_read)
    end

    def write(key, data)
      file_to_write = cache_file(key)

      File.open(file_to_write, "w") do |f|
        f.write(JSON.generate(data.to_h))
      end
    end

    private

    def cache_file(key)
      File.join(@cache_folder, cache_filename(key))
    end

    def cache_filename(cache_key)
      "#{cache_key}.cache"
    end
  end

  # Cache class that does nothing
  # @api private
  class NullCache
    def initialize(*_args); end

    def read(_key); end

    def write(_key, _data); end
  end

  # Wrapper around an API
  # @api private
  class ApiClient
    # Perform API request; return hash with html content
    def fetch(api_request)
      uri = api_request.to_uri
      response = Net::HTTP.start(uri.host, use_ssl: api_request.ssl?) do |http|
        http.read_timeout = 5
        http.open_timeout = 5
        http.get uri.request_uri, REQUEST_HEADERS
      end

      handle_response(api_request, response)
    rescue Timeout::Error => e
      ErrorResponse.new(api_request, e.class.name).to_h
    end

    private

    def handle_response(api_request, response)
      case response
      when Net::HTTPSuccess
        JSON.parse(response.body)
      else
        ErrorResponse.new(api_request, response.message).to_h
      end
    end
  end

  # @api private
  ErrorResponse = Struct.new(:request, :message) do
    def html
      "<p>There was a '#{message}' error fetching URL: '#{request.entity_url}'</p>"
    end

    def to_h
      { html: html }
    end
  end

  # Holds the URI were going to request with any parameters
  # @api private
  ApiRequest = Struct.new(:entity_url, :params) do
    TWITTER_API_URL = "https://publish.twitter.com/oembed".freeze

    # Always;
    def ssl?
      true
    end

    # Return a URI for Twitter API with query params
    def to_uri
      URI.parse(TWITTER_API_URL).tap do |uri|
        uri.query = URI.encode_www_form url_params
      end
    end

    # A cache key applicable to the current request with params
    def cache_key
      Digest::MD5.hexdigest("#{self.class.name}-#{unique_request_key}")
    end

    private

    def url_params
      params.merge(url: entity_url)
    end

    def unique_request_key
      format("%s-%s", entity_url, params.to_s)
    end
  end

  # Class to respond to Jekyll tag; entry point to library
  # @api public
  class TwitterTag < Liquid::Tag
    ERROR_BODY_TEXT = "<p>Tweet could not be processed</p>".freeze
    OEMBED_ARG      = "oembed".freeze

    URL_OR_STRING_PARAM = /^("|')?(http|https):\/\//i

    attr_writer :cache # for testing

    def initialize(_name, params, _tokens)
      super

      # Test if first arg is a URL or starts with oembed,
      # otherwise its a Jekyll variable. TODO: remove oembed after deprecation cycle
      if params =~ URL_OR_STRING_PARAM || params.to_s.start_with?(OEMBED_ARG)
        @fetch_from_context = false
        @api_request = parse_params_from_string(params)
      else
        @fetch_from_context = true
        @variable_params = normalize_string_params(params)
      end
    end

    # Class that implements caching strategy
    # @api private
    def self.cache_klass
      FileCache
    end

    # Return html string for Jekyll engine
    # @api public
    def render(context)
      if fetch_from_context?
        variable_name, *params = @variable_params
        tweet_url = context[variable_name]
        @api_request = parse_params_from_array [tweet_url, *params]
      end

      api_secrets_deprecation_warning(context) # TODO: remove after deprecation cycle
      response = cached_response || live_response
      html_output_for(response)
    end

    private

    def fetch_from_context?
      @fetch_from_context
    end

    def cache
      @cache ||= self.class.cache_klass.new("./.tweet-cache")
    end

    def api_client
      @api_client ||= ApiClient.new
    end

    # Return Twitter response or error html
    # @api private
    def html_output_for(response)
      body = (response.html if response) || ERROR_BODY_TEXT

      "<div class='jekyll-twitter-plugin'>#{body}</div>"
    end

    # Return response from API and write to cache
    # @api private
    def live_response
      if response = api_client.fetch(@api_request)
        cache.write(@api_request.cache_key, response)
        build_response(response)
      end
    end

    # Return response cache if present, otherwise nil
    # @api private
    def cached_response
      response = cache.read(@api_request.cache_key)
      build_response(response) unless response.nil?
    end

    def parse_params_from_string(str)
      args = normalize_string_params(str)
      parse_params(args)
    end

    def parse_params_from_array(arr)
      parse_params(arr)
    end

    # Return an `ApiRequest` with the url and arguments
    # @api private
    def parse_params(args)
      invalid_args!(args) unless args.compact.any?

      if args[0].to_s == OEMBED_ARG # TODO: remove after deprecation cycle
        arguments_deprecation_warning(args)
        args.shift
      end

      url, *api_args = args
      ApiRequest.new(url, hash_from_args(api_args))
    end

    # Take input arguments, remove quotes & return array of argument values
    # @api private
    def normalize_string_params(str)
      str.to_s.gsub(/"|'/, "").split(/\s+/).map(&:strip)
    end

    # Transform 'a=b x=y' tag arguments into { "a" => "b", "x" => "y" }
    # @api private
    def hash_from_args(args)
      args.each_with_object({}) do |arg, results|
        k, v = arg.split("=").map(&:strip)
        if k && v
          v = Regexp.last_match[1] if v =~ /^'(.*)'$/
          results[k] = v
        end
      end
    end

    # Format a response hash
    # @api private
    def build_response(response_hash)
      OpenStruct.new(response_hash)
    end

    # TODO: remove after deprecation cycle
    def arguments_deprecation_warning(args)
      warn "#{LIBRARY_VERSION}: Passing '#{OEMBED_ARG}' as the first argument is not required anymore. This will result in an error in future versions.\nCalled with #{args.inspect}"
    end

    # TODO: remove after deprecation cycle
    def api_secrets_deprecation_warning(context)
      warn_if_twitter_secrets_in_context(context) || warn_if_twitter_secrets_in_env
    end

    # TODO: remove after deprecation cycle
    def warn_if_twitter_secrets_in_context(context)
      twitter_secrets = context.registers[:site].config.fetch("twitter", {})
      return unless store_has_keys?(twitter_secrets, CONTEXT_API_KEYS)

      warn_secrets_in_project("Jekyll _config.yml")
    end

    # TODO: remove after deprecation cycle
    def warn_if_twitter_secrets_in_env
      return unless store_has_keys?(ENV, ENV_API_KEYS)

      warn_secrets_in_project("ENV")
    end

    # TODO: remove after deprecation cycle
    def warn_secrets_in_project(source)
      warn "#{LIBRARY_VERSION}: Found Twitter API keys in #{source}, this library does not require these keys anymore. You can remove these keys, if used for another library then ignore this message."
    end

    # TODO: remove after deprecation cycle
    def store_has_keys?(store, keys)
      keys.all? { |required_key| store.key?(required_key) }
    end

    # Raise error for invalid arguments
    # @api private
    def invalid_args!(arguments)
      formatted_args = Array(arguments).join(" ")
      raise ArgumentError, "Invalid arguments '#{formatted_args}' passed to 'jekyll-twitter-plugin'. #{REFER_TO_README}"
    end
  end

  # Specialization of TwitterTag without any caching
  # @api public
  class TwitterTagNoCache < TwitterTag
    def self.cache_klass
      NullCache
    end
  end
end

Liquid::Template.register_tag("twitter", TwitterJekyll::TwitterTag)
Liquid::Template.register_tag("twitternocache", TwitterJekyll::TwitterTagNoCache)

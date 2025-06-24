# frozen_string_literal: true

require "digest/md5"

module JekyllIncludeCache
  class Tag < Jekyll::Tags::IncludeTag
    def self.digest_cache
      @digest_cache ||= {}
    end

    def render(context)
      path   = path(context)
      params = parse_params(context) if @params
      key = key(path, params)
      return unless path

      if JekyllIncludeCache.cache.key?(key)
        Jekyll.logger.debug "Include cache hit:", path
        JekyllIncludeCache.cache[key]
      else
        Jekyll.logger.debug "Include cache miss:", path
        JekyllIncludeCache.cache[key] = super
      end
    end

    private

    def path(context)
      site   = context.registers[:site]
      file   = render_variable(context) || @file
      locate_include_file(context, file, site.safe)
    end

    def key(path, params)
      path_hash   = path.hash
      params_hash = quick_hash(params)
      self.class.digest_cache[path_hash] ||= {}
      self.class.digest_cache[path_hash][params_hash] ||= digest(path_hash, params_hash)
    end

    def quick_hash(params)
      return params.hash unless params

      md5 = Digest::MD5.new

      params.sort.each do |_, value|
        # Using the fact that Jekyll documents don't change during a build.
        # Instead of calculating the hash of an entire document (expensive!)
        # we just use its object id.
        if value.is_a? Jekyll::Drops::Drop
          md5.update value.object_id.to_s
        else
          md5.update value.hash.to_s
        end
      end

      md5.hexdigest
    end

    def digest(path_hash, params_hash)
      md5 = Digest::MD5.new
      md5.update path_hash.to_s
      md5.update params_hash.to_s
      md5.hexdigest
    end
  end
end

# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    class Owner
      extend Forwardable

      # Defines an instance method that delegates to a hash's key
      #
      # hash   - a symbol representing the instance method to delegate to. The
      #          instance method should return a hash or respond to #[]
      # key    - the key to call within the hash
      # method - (optional) the instance method the key should be aliased to.
      #          If not specified, defaults to the hash key
      #
      # Returns a symbol representing the instance method
      def self.def_hash_delegators(hash, *methods)
        content_methods.concat(methods)
        methods.each do |method|
          define_method(method) do
            send(hash)[method.to_s]
          end
        end
      end

      def self.content_methods
        @content_methods ||= []
      end

      # List of whitelisted keys.
      def_hash_delegators :owner_info,
                          :avatar_url,
                          :bio,
                          :blog,
                          :collaborators,
                          :company,
                          :created_at,
                          :description,
                          :email,
                          :followers,
                          :following,
                          :has_organization_projects,
                          :has_repository_projects,
                          :hireable,
                          :html_url,
                          :id,
                          :is_verified,
                          :location,
                          :login,
                          :name,
                          :node_id,
                          :public_gists,
                          :public_gists,
                          :public_repos,
                          :public_repos,
                          :type,
                          :updated_at

      attr_reader :owner_login

      def initialize(owner_login)
        @owner_login = owner_login
      end

      def to_h
        @to_h ||= self.class.content_methods
          .each_with_object({}) { |method, hash| hash[method.to_s] = public_send(method) }
      end
      alias_method :to_hash, :to_h
      def_delegator :to_h, :to_json, :to_json
      def_delegator :to_h, :to_liquid, :to_liquid

      def_delegator :to_h, :to_s, :to_s
      alias_method :to_str, :to_s

      private

      def owner_info
        @owner_info ||= begin
          Value.new(
            "owner",
            proc do |c|
              (c.organization(owner_login) || c.user(owner_login) || {}).to_h
            end
          ).render || {}
        end
      end
    end
  end
end

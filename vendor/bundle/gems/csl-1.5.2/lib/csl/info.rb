module CSL
  #
  # {Info} nodes contain a {Style} (or {Locale}) metadata. Their XML structure
  # is based on the Atom Syndication Format. For independent styles an {Info}
  # node typically has the following child elements:
  #
  # * {Author} and {Contributor}: used to respectively acknowledge
  #   style authors and contributors, may each be used multiple times.
  # * {Category}: styles may be assigned one or more categories. One
  #   {Category} node may be used once to describe how in-text citations
  #   are rendered, using its citation-format attribute.
  # * {Id}: Must appear once. The element should contain a URI to establish
  #   the identity of the style. A stable, unique and dereferenceable URI
  #   is desired for publicly available styles.
  # * {Link}: Multiple links can be added to an {Info} node: self,
  #   documentation, and template links all have dedicated accessors.
  # * {Title}: Must appear once. The contents of this node should be the
  #   name of the style as shown to users.
  # * {TitleShort}: May appear once. The contents of this node should be a
  #   shortened style name (e.g. "APA").
  # * {Summary}: This node gives a description of the style.
  # * {Rights}: This node specifies the license under which the style file
  #   is released. The element may carry a license attribute to specify the
  #   URI of the license.
  # * {Updated}: Must appear once. This node must contain a timestamp that
  #   shows when the style was last updated.
  #
  # In dependent styles, the {Info} node must contain a {Link} with rel set
  # to "independent-parent", with the URI of the independent parent style
  # set on href. This link is also accessible as a string using the
  # {#independent_parent} accessors. In addition, dependent styles should
  # not contain template links.
  #
  # In a {Locale} node the {Info} node typically carries only {Translator},
  # {Rights} and {Updated} nodes.
  class Info < Node

    attr_children :title, :'title-short', :id, :issn, :eissn, :issnl,
      :link, :author, :contributor, :translator, :category, :published,
      :summary, :updated, :rights, :'link-dependent-style'

    alias_child :contributors, :contributor
    alias_child :authors, :author
    alias_child :translators, :translator
    alias_child :links, :link
    alias_child :categories, :category

    def initialize(attributes = {})
      super(attributes, &nil)
      children[:link], children[:category] = [], []

      yield self if block_given?
    end

    # @!attribute self_link
    # @return [String,nil] the style's URI

    # @!attribute template_link
    # @return [String,nil] URI of the style from which the current style is derived

    # @!attribute documentation_link
    # @return [String,nil] URI of style documentation

    # @!attribute independent_parent_link
    # @return [String,nil] URI of independent-parent
    %w{ self template documentation independent-parent }.each do |type|
      method_id = "#{type.tr('-', '_')}_link"

      define_method method_id do
        link = links.detect { |l| l.match? :rel => type }
        link.nil? ? nil : link[:href]
      end

      alias_method "has_#{method_id}?", method_id

      define_method "#{method_id}=" do |value|
        link = links.detect { |l| l.match? :rel => type }

        if link.nil?
          set_child_link :href => value.to_s, :rel => type
        else
          link[:href] = value.to_s
          link
        end
      end
    end

    # Ruby 1.8 still has Object#id methods so the attr_children generator
    # may not have created those; since #id is deprecated in 1.8.7 we're
    # forcing the override anyway. Live dangerously!
    remove_method :id

    # @return [Id] the id text node
    def id
      children[:id]
    end

    alias id= set_child_id

    def self_link!
      return unless has_id?
      self.self_link = id
    end

    # @return [Time,nil] when the info node's parent was last updated
    def updated_at
      return unless has_updated?
      updated.to_time
    end

    # Sets the updated_at timestamp.
    # @return [self]
    def update!(timestamp = Time.now)
      ts = timestamp.respond_to?(:xmlschema) ? timestamp.xmlschema : timestamp.to_s

      if has_updated?
        updated.text = ts
      else
        add_child Updated.new { |u| u.text = ts }
      end

      self
    end

    # @return [Time,nil] when the info node's parent was published
    def published_at
      return unless has_published?
      published.to_time
    end

    # Sets the updated_at timestamp.
    # @return [self]
    def publish!(timestamp = Time.now)
      ts = timestamp.respond_to?(:xmlschema) ? timestamp.xmlschema : timestamp.to_s

      if has_published?
        published.text = ts
      else
        add_child Published.new { |u| u.text = ts }
      end

      self
    end

    def license
      return unless has_rights?
      rights[:license] || rights.to_s
    end

    def license=(license)
      if has_rights?
        rights[:license] = license
      else
        add_child Rights.new(:license => license)
      end
    end

    def default_license?
      has_rights? && rights[:license] == Schema.default_license &&
        rights.text == Schema.default_rights_string
    end

    def default_license!
      if has_rights?
        rights[:license] = Schema.default_license
        rights.text = Schema.default_rights_string
      else
        add_child Rights.new(:license => Schema.default_license) { |r|
          r.text = Schema.default_rights_string
        }
      end
    end

    # @return [Symbol] the parent style's citation format
    def citation_format
      return unless has_categories?

      cat = categories.detect { |c| c.attribute? :'citation-format' }
      return if cat.nil?

      cat[:'citation-format'].to_sym
    end

    def citation_format=(new_format)
      cat = categories.detect { |c| c.attribute? :'citation-format' }
      cat = add_child Info::Category.new if cat.nil?

      cat[:'citation-format'] = new_format.to_s
    end

    #
    # Info Child Nodes
    #

    class Contributor < Node
      attr_children :name, :email, :uri
      def_delegators :name, *Namae::Name.members
    end

    class Author < Node
      attr_children :name, :email, :uri
      def_delegators :name, *Namae::Name.members
    end

    class Translator < Node
      attr_children :name, :email, :uri
      def_delegators :name, *Namae::Name.members
    end

    class Link < Node
      has_language
      attr_struct :href, :rel
    end

    class DependentStyle < TextNode
      attr_struct :href, :rel
    end


    class Category < Node
      attr_struct :field, :'citation-format'
    end

    class Id < TextNode
    end

    class Name < TextNode

      def_delegators :namae, *Namae::Name.members

      private

      def namae
        @namae || namae!
      end

      def namae!
        @namae = Namae::Name.parse to_s
      end
    end

    class Email < TextNode
    end

    class URI < TextNode
    end

    class Title < TextNode
      has_language
    end

    class TitleShort < TextNode
      has_language
    end

    class Summary < TextNode
      has_language
    end

    class Rights < TextNode
      has_language
      attr_struct :license
    end

    class Updated < TextNode
      def to_time
        return if empty?
        Time.parse(to_s)
      end
      alias to_date to_time
    end

    class Published < TextNode
      def to_time
        return if empty?
        Time.parse(to_s)
      end
      alias to_date to_time
    end

  end


end

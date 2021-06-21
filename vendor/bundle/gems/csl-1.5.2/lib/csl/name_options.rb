module CSL
  module InheritableNameOptions
    def inheritable_name_options
      options = attributes_for(*Schema.attr(:name))

      if attribute?(:'name-delimiter')
        options[:delimiter] = attributes[:'name-delimiter']
      end

      if attribute?(:'name-form')
        options[:form] = attributes[:'name-form']
      end

      options
    end

    def inheritable_names_options
      return {} unless attribute? :'names-delimiter'
      { :delimiter => attributes[:'names-delimiter'] }
    end
  end

  module InheritsNameOptions
    def inherits(name)
      inheritable_options = "inheritable_#{name}".to_sym

      define_method("inherited_#{name}") do |node, style|
        options = {}

        if node.respond_to?(inheritable_options)
          options = node.send(inheritable_options).merge(options)
        end

        style ||= root

        if !style.equal?(self) && style.respond_to?(inheritable_options)
          options = style.send(inheritable_options).merge(options)
        end

        options
      end
    end
  end
end

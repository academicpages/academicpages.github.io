module CSL
  module DatePart

    def range_delimiter
      attributes.fetch(:'range-delimiter', '')
    end

    def has_name?
      attribute?(:name)
    end

    def name
      attributes[:name].to_s
    end

    def has_form?
      attribute?(:form)
    end

    def form
      case
      when has_form?
        attributes[:form].to_s
      when day?
        'numeric'
      else
        'long'
      end
    end

    Schema.values[:date_part][:form].each do |type|
      pattern = Regexp.new("^#{type}$", true)

      define_method("#{type}?".tr('-', '_')) do
        form =~ pattern
      end
    end

    def year?
      name =~ /year/i
    end

    def month?
      name =~ /month/i
    end

    def day?
      name =~ /day/i
    end

  end
end
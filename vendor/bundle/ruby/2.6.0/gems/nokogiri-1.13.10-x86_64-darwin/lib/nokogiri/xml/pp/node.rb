# frozen_string_literal: true

module Nokogiri
  module XML
    # :nodoc: all
    module PP
      module Node
        def inspect
          attributes = inspect_attributes.reject do |x|
            attribute = send(x)
            !attribute || (attribute.respond_to?(:empty?) && attribute.empty?)
          rescue NoMethodError
            true
          end.map do |attribute|
            "#{attribute.to_s.sub(/_\w+/, "s")}=#{send(attribute).inspect}"
          end.join(" ")
          "#<#{self.class.name}:#{format("0x%x", object_id)} #{attributes}>"
        end

        def pretty_print(pp)
          nice_name = self.class.name.split("::").last
          pp.group(2, "#(#{nice_name}:#{format("0x%x", object_id)} {", "})") do
            pp.breakable
            attrs = inspect_attributes.map do |t|
              [t, send(t)] if respond_to?(t)
            end.compact.find_all do |x|
              if x.last
                if [:attribute_nodes, :children].include?(x.first)
                  !x.last.empty?
                else
                  true
                end
              end
            end

            pp.seplist(attrs) do |v|
              if [:attribute_nodes, :children].include?(v.first)
                pp.group(2, "#{v.first.to_s.sub(/_\w+$/, "s")} = [", "]") do
                  pp.breakable
                  pp.seplist(v.last) do |item|
                    pp.pp(item)
                  end
                end
              else
                pp.text("#{v.first} = ")
                pp.pp(v.last)
              end
            end
            pp.breakable
          end
        end
      end
    end
  end
end

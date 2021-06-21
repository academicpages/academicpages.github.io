# frozen_string_literal: true

require 'pp'

module CommonMarker
  class Node
    module Inspect
      PP_INDENT_SIZE = 2

      def inspect
        PP.pp(self, String.new, Float::INFINITY)
      end

      # @param [PrettyPrint] pp
      def pretty_print(pp)
        pp.group(PP_INDENT_SIZE, "#<#{self.class}(#{type}):", '>') do
          pp.breakable

          attrs = %i[
            sourcepos
            string_content
            url
            title
            header_level
            list_type
            list_start
            list_tight
            fence_info
          ].map do |name|
            begin
              [name, __send__(name)]
            rescue NodeError
              nil
            end
          end.compact

          pp.seplist(attrs) do |name, value|
            pp.text "#{name}="
            pp.pp value
          end

          if first_child
            pp.breakable
            pp.group(PP_INDENT_SIZE) do
              children = []
              node = first_child
              while node
                children << node
                node = node.next
              end
              pp.text 'children='
              pp.pp children
            end
          end
        end
      end
    end
  end
end

# coding: utf-8
# frozen_string_literal: true

require "pathname"

module Nokogiri
  module HTML4
    class Document < Nokogiri::XML::Document
      ###
      # Get the meta tag encoding for this document.  If there is no meta tag,
      # then nil is returned.
      def meta_encoding
        if (meta = at_xpath("//meta[@charset]"))
          meta[:charset]
        elsif (meta = meta_content_type)
          meta["content"][/charset\s*=\s*([\w-]+)/i, 1]
        end
      end

      ###
      # Set the meta tag encoding for this document.
      #
      # If an meta encoding tag is already present, its content is
      # replaced with the given text.
      #
      # Otherwise, this method tries to create one at an appropriate
      # place supplying head and/or html elements as necessary, which
      # is inside a head element if any, and before any text node or
      # content element (typically <body>) if any.
      #
      # The result when trying to set an encoding that is different
      # from the document encoding is undefined.
      #
      # Beware in CRuby, that libxml2 automatically inserts a meta tag
      # into a head element.
      def meta_encoding=(encoding)
        if (meta = meta_content_type)
          meta["content"] = format("text/html; charset=%s", encoding)
          encoding
        elsif (meta = at_xpath("//meta[@charset]"))
          meta["charset"] = encoding
        else
          meta = XML::Node.new("meta", self)
          if (dtd = internal_subset) && dtd.html5_dtd?
            meta["charset"] = encoding
          else
            meta["http-equiv"] = "Content-Type"
            meta["content"] = format("text/html; charset=%s", encoding)
          end

          if (head = at_xpath("//head"))
            head.prepend_child(meta)
          else
            set_metadata_element(meta)
          end
          encoding
        end
      end

      def meta_content_type
        xpath("//meta[@http-equiv and boolean(@content)]").find do |node|
          node["http-equiv"] =~ /\AContent-Type\z/i
        end
      end
      private :meta_content_type

      ###
      # Get the title string of this document.  Return nil if there is
      # no title tag.
      def title
        (title = at_xpath("//title")) && title.inner_text
      end

      ###
      # Set the title string of this document.
      #
      # If a title element is already present, its content is replaced
      # with the given text.
      #
      # Otherwise, this method tries to create one at an appropriate
      # place supplying head and/or html elements as necessary, which
      # is inside a head element if any, right after a meta
      # encoding/charset tag if any, and before any text node or
      # content element (typically <body>) if any.
      def title=(text)
        tnode = XML::Text.new(text, self)
        if (title = at_xpath("//title"))
          title.children = tnode
          return text
        end

        title = XML::Node.new("title", self) << tnode
        if (head = at_xpath("//head"))
          head << title
        elsif (meta = (at_xpath("//meta[@charset]") || meta_content_type))
          # better put after charset declaration
          meta.add_next_sibling(title)
        else
          set_metadata_element(title)
        end
      end

      def set_metadata_element(element) # rubocop:disable Naming/AccessorMethodName
        if (head = at_xpath("//head"))
          head << element
        elsif (html = at_xpath("//html"))
          head = html.prepend_child(XML::Node.new("head", self))
          head.prepend_child(element)
        elsif (first = children.find do |node|
                 case node
                 when XML::Element, XML::Text
                   true
                 end
               end)
          # We reach here only if the underlying document model
          # allows <html>/<head> elements to be omitted and does not
          # automatically supply them.
          first.add_previous_sibling(element)
        else
          html = add_child(XML::Node.new("html", self))
          head = html.add_child(XML::Node.new("head", self))
          head.prepend_child(element)
        end
      end
      private :set_metadata_element

      ####
      # Serialize Node using +options+. Save options can also be set using a block.
      #
      # See also Nokogiri::XML::Node::SaveOptions and Node@Serialization+and+Generating+Output.
      #
      # These two statements are equivalent:
      #
      #  node.serialize(:encoding => 'UTF-8', :save_with => FORMAT | AS_XML)
      #
      # or
      #
      #   node.serialize(:encoding => 'UTF-8') do |config|
      #     config.format.as_xml
      #   end
      #
      def serialize(options = {})
        options[:save_with] ||= XML::Node::SaveOptions::DEFAULT_HTML
        super
      end

      ####
      # Create a Nokogiri::XML::DocumentFragment from +tags+
      def fragment(tags = nil)
        DocumentFragment.new(self, tags, root)
      end

      # :call-seq:
      #   xpath_doctype() → Nokogiri::CSS::XPathVisitor::DoctypeConfig
      #
      # [Returns] The document type which determines CSS-to-XPath translation.
      #
      # See XPathVisitor for more information.
      def xpath_doctype
        Nokogiri::CSS::XPathVisitor::DoctypeConfig::HTML4
      end

      class << self
        ###
        # Parse HTML.  +string_or_io+ may be a String, or any object that
        # responds to _read_ and _close_ such as an IO, or StringIO.
        # +url+ is resource where this document is located.  +encoding+ is the
        # encoding that should be used when processing the document. +options+
        # is a number that sets options in the parser, such as
        # Nokogiri::XML::ParseOptions::RECOVER.  See the constants in
        # Nokogiri::XML::ParseOptions.
        def parse(string_or_io, url = nil, encoding = nil, options = XML::ParseOptions::DEFAULT_HTML)
          options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
          yield options if block_given?

          url ||= string_or_io.respond_to?(:path) ? string_or_io.path : nil

          if string_or_io.respond_to?(:encoding)
            unless string_or_io.encoding.name == "ASCII-8BIT"
              encoding ||= string_or_io.encoding.name
            end
          end

          if string_or_io.respond_to?(:read)
            if string_or_io.is_a?(Pathname)
              # resolve the Pathname to the file and open it as an IO object, see #2110
              string_or_io = string_or_io.expand_path.open
              url ||= string_or_io.path
            end

            unless encoding
              # Libxml2's parser has poor support for encoding
              # detection.  First, it does not recognize the HTML5
              # style meta charset declaration.  Secondly, even if it
              # successfully detects an encoding hint, it does not
              # re-decode or re-parse the preceding part which may be
              # garbled.
              #
              # EncodingReader aims to perform advanced encoding
              # detection beyond what Libxml2 does, and to emulate
              # rewinding of a stream and make Libxml2 redo parsing
              # from the start when an encoding hint is found.
              string_or_io = EncodingReader.new(string_or_io)
              begin
                return read_io(string_or_io, url, encoding, options.to_i)
              rescue EncodingFound => e
                encoding = e.found_encoding
              end
            end
            return read_io(string_or_io, url, encoding, options.to_i)
          end

          # read_memory pukes on empty docs
          if string_or_io.nil? || string_or_io.empty?
            return encoding ? new.tap { |i| i.encoding = encoding } : new
          end

          encoding ||= EncodingReader.detect_encoding(string_or_io)

          read_memory(string_or_io, url, encoding, options.to_i)
        end
      end

      class EncodingFound < StandardError # :nodoc: all
        attr_reader :found_encoding

        def initialize(encoding)
          @found_encoding = encoding
          super(format("encoding found: %s", encoding))
        end
      end

      # :nodoc: all
      class EncodingReader
        class SAXHandler < Nokogiri::XML::SAX::Document
          attr_reader :encoding

          def initialize
            @encoding = nil
            super()
          end

          def start_element(name, attrs = [])
            return unless name == "meta"

            attr = Hash[attrs]
            (charset = attr["charset"]) &&
              (@encoding = charset)
            (http_equiv = attr["http-equiv"]) &&
              http_equiv.match(/\AContent-Type\z/i) &&
              (content = attr["content"]) &&
              (m = content.match(/;\s*charset\s*=\s*([\w-]+)/)) &&
              (@encoding = m[1])
          end
        end

        class JumpSAXHandler < SAXHandler
          def initialize(jumptag)
            @jumptag = jumptag
            super()
          end

          def start_element(name, attrs = [])
            super
            throw(@jumptag, @encoding) if @encoding
            throw(@jumptag, nil) if /\A(?:div|h1|img|p|br)\z/.match?(name)
          end
        end

        def self.detect_encoding(chunk)
          (m = chunk.match(/\A(<\?xml[ \t\r\n][^>]*>)/)) &&
            (return Nokogiri.XML(m[1]).encoding)

          if Nokogiri.jruby?
            (m = chunk.match(/(<meta\s)(.*)(charset\s*=\s*([\w-]+))(.*)/i)) &&
              (return m[4])
            catch(:encoding_found) do
              Nokogiri::HTML4::SAX::Parser.new(JumpSAXHandler.new(:encoding_found)).parse(chunk)
              nil
            end
          else
            handler = SAXHandler.new
            parser = Nokogiri::HTML4::SAX::PushParser.new(handler)
            begin
              parser << chunk
            rescue
              Nokogiri::SyntaxError
            end
            handler.encoding
          end
        end

        def initialize(io)
          @io = io
          @firstchunk = nil
          @encoding_found = nil
        end

        # This method is used by the C extension so that
        # Nokogiri::HTML4::Document#read_io() does not leak memory when
        # EncodingFound is raised.
        attr_reader :encoding_found

        def read(len)
          # no support for a call without len

          unless @firstchunk
            (@firstchunk = @io.read(len)) || (return nil)

            # This implementation expects that the first call from
            # htmlReadIO() is made with a length long enough (~1KB) to
            # achieve advanced encoding detection.
            if (encoding = EncodingReader.detect_encoding(@firstchunk))
              # The first chunk is stored for the next read in retry.
              raise @encoding_found = EncodingFound.new(encoding)
            end
          end
          @encoding_found = nil

          ret = @firstchunk.slice!(0, len)
          if (len -= ret.length) > 0
            (rest = @io.read(len)) && ret << (rest)
          end
          if ret.empty?
            nil
          else
            ret
          end
        end
      end
    end
  end
end

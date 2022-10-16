## Liquid tag 'maincolumn-figure' used to add image data that fits within the
## main column area of the layout
## Usage {% maincolumn 'path/to/image' 'This is the caption' %}
#
module Jekyll
  class RenderMainColumnTag < Liquid::Tag

  	require "shellwords"
    require "kramdown"

    def initialize(tag_name, text, tokens)
      super
      @text = text.shellsplit
    end

    def render(context)

      # Gather settings
      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

      baseurl = context.registers[:site].config['baseurl']
      label = Kramdown::Document.new(@text[1],{remove_span_html_tags:true}).to_html # render markdown in caption
      label = converter.convert(label).gsub(/<\/?p[^>]*>/, "").chomp # remove <p> tags from render output

      if @text[0].start_with?('http://', 'https://','//')
        "<figure><img src='#{@text[0]}'/><figcaption class='maincolumn-figure'>#{label}</figcaption></figure>"
      else
        "<figure><img src='#{baseurl}/#{@text[0]}'/><figcaption class='maincolumn-figure'>#{label}</figcaption></figure>"
      end
    end
  end
end

Liquid::Template.register_tag('maincolumn', Jekyll::RenderMainColumnTag)

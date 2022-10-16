module Jekyll
  class MathJaxBlockTag < Liquid::Tag
    def render(context)
      '<div class="mathblock"><script type="math/tex; mode=display">'
    end
  end
class MathJaxInlineTag < Liquid::Tag
    def render(context)
      '<span>&#8203;<script type="math/tex">'
    end
  end
class MathJaxEndBlockTag < Liquid::Tag
    def render(context)
      '</script></div>'
    end
  end
class MathJaxEndInlineTag < Liquid::Tag
    def render(context)
      '</script></span>'
    end
  end  
end
 
Liquid::Template.register_tag('math', Jekyll::MathJaxBlockTag)
Liquid::Template.register_tag('m', Jekyll::MathJaxInlineTag)
Liquid::Template.register_tag('endmath', Jekyll::MathJaxEndBlockTag)
Liquid::Template.register_tag('em', Jekyll::MathJaxEndInlineTag)
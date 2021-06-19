module CSL
  class Locale

    class StyleOptions < Node
      has_no_children
      attr_defaults :'punctuation-in-quote' => false,
        :'limit-day-ordinals-to-day-1' => false
    end

  end
end
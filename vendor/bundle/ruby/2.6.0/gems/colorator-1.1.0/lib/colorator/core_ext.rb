class String
  Colorator::CORE_METHODS.each do |method|
    define_method method do |*args|
      Colorator.public_send(method,
        self, *args
      )
    end
  end
end

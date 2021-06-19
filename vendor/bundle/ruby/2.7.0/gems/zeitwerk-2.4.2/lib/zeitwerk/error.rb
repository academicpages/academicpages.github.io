module Zeitwerk
  class Error < StandardError
  end

  class ReloadingDisabledError < Error
  end

  class NameError < ::NameError
  end
end

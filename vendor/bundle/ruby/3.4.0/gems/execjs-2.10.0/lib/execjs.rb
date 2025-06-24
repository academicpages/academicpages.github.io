require "execjs/module"
require "execjs/runtimes"

module ExecJS
  def self.runtime
    @runtime ||= Runtimes.autodetect
  end
end

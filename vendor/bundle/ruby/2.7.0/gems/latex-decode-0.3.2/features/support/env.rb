begin
  case
  when defined?(RUBY_ENGINE) && RUBY_ENGINE == 'rbx'
    require 'rubinius/debugger'
  when RUBY_VERSION > '2.0'
    require 'byebug'
  else
    require 'debugger'
  end
rescue LoadError
  # ignore
end

require 'latex/decode'

HERE = File.dirname(__FILE__) unless defined?(HERE)
ROOT = File.join(HERE, "..") unless defined?(ROOT)

$LOAD_PATH << File.join(ROOT, "lib")
$LOAD_PATH << File.join(HERE, "support")

require "yaml"
if ENV["YAMLER"] && defined?(YAML::ENGINE)
  YAML::ENGINE.yamler = ENV["YAMLER"]
end

ruby_version = defined?(JRUBY_VERSION) ? "JRuby #{JRUBY_VERSION} in #{RUBY_VERSION} mode" : "Ruby #{RUBY_VERSION}"
yaml_engine = defined?(YAML::ENGINE) ? YAML::ENGINE.yamler : "syck"
libyaml_version = yaml_engine == "psych" && Psych.const_defined?("LIBYAML_VERSION", false) ? Psych::LIBYAML_VERSION : "N/A"

env_info = [
  ruby_version,
  "YAML: #{yaml_engine} (#{YAML::VERSION}) (libyaml: #{libyaml_version})",
  "Monkeypatch: #{ENV['MONKEYPATCH_YAML']}"
]

puts env_info.join(", ")

# Caching references to these methods before loading safe_yaml in order to test
# that they aren't touched unless you actually require safe_yaml (see yaml_spec.rb).
ORIGINAL_YAML_LOAD      = YAML.method(:load)
ORIGINAL_YAML_LOAD_FILE = YAML.method(:load_file)

require "safe_yaml/load"
require "ostruct"
require "hashie"
require "heredoc_unindent"

# Stolen from Rails:
# https://github.com/rails/rails/blob/3-2-stable/activesupport/lib/active_support/core_ext/kernel/reporting.rb#L10-25
def silence_warnings
  $VERBOSE = nil; yield
ensure
  $VERBOSE = true
end

require File.join(HERE, "resolver_specs")

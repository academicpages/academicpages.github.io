$LOAD_PATH.unshift File.expand_path("../../lib", __FILE__)

require "memory_profiler"
require "public_suffix"

PublicSuffix::List.default

report = MemoryProfiler.report do
  PublicSuffix.domain("www.example.com")
  PublicSuffix.domain("a.b.ide.kyoto.jp")
end

report.pretty_print
# report.pretty_print(to_file: 'profiler-%s-%d.txt' % [ARGV[0], Time.now.to_i])

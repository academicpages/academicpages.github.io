# Frozen-string-literal: true
# Copyright: 2017 - 2018 - MIT License
# Source: https://github.com/envygeeks/devfiles
# Author: Jordon Bedwell
# Encoding: utf-8

task default: [:spec]
task(:spec) { exec "script/test" }
task(:test) { exec "script/test" }
Dir.glob("script/rake.d/*.rake").each do |v|
  load v
end

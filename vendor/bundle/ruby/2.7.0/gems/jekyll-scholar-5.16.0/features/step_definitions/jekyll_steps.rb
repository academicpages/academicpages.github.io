
# Like "I have a foo file" but gives a yaml front matter so jekyll actually processes it
Given(/^I have an? "(.*)" page(?: with (.*) "(.*)")? that contains "(.*)"$/) do |file, key, value, text|
  File.open(file, 'w') do |f|
    f.write <<EOF
---
#{key || 'layout'}: #{value || 'nil'}
---
#{text}
EOF
    f.close
  end
end

Given(/^I have an? "(.*)" file that contains "(.*)"$/) do |file, text|
  File.open(file, 'w') do |f|
    f.write(text)
    f.close
  end
end

Given(/^I have a configuration file with "(.*)" set to "(.*)"$/) do |key, value|
  File.open('_config.yml', 'a') do |f|
    f.write("#{key}: #{value}\n")
    f.close
  end
end

Given(/^I have a configuration file with:$/) do |table|
  File.open('_config.yml', 'a') do |f|
    table.hashes.each do |row|
      f.write("#{row["key"]}: #{row["value"]}\n")
    end
    f.close
  end
end

When(/^I run jekyll$/) do
  run_jekyll
end

Then(/^the (.*) directory should exist$/) do |dir|
  assert File.directory?(dir)
end

Then(/^I should see "(.*)" in "(.*)"$/) do |pattern, file|
  text = File.open(file).readlines.join

  assert_match Regexp.new(pattern), text,
    "Pattern /#{pattern}/ not found in: #{text}"
end

Then(/^I should not see "(.*)" in "(.*)"$/) do |pattern, file|
  text = File.open(file).readlines.join

  assert !text.match(Regexp.new(pattern)),
    "Did not exptect /#{pattern}/ in: #{text}"
end


Then(/^the "(.*)" file should exist$/) do |file|
  assert File.file?(file)
end

Then(/^the "(.*)" file should not exist$/) do |file|
  assert !File.exists?(file)
end

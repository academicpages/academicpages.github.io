# coding: utf-8
require 'commonmarker'
require 'minitest/autorun'
require 'minitest/pride'

include CommonMarker

FIXTURES_DIR = File.join(File.dirname(__FILE__), 'fixtures')

def open_spec_file(filename)
  line_number = 0
  start_line = 0
  end_line = 0
  example_number = 0
  markdown_lines = []
  html_lines = []
  state = 0 # 0 regular text, 1 markdown example, 2 html output
  headertext = ''
  tests = []
  extensions = []

  header_re = Regexp.new('#+ ')
  filepath = File.join('ext', 'commonmarker', 'cmark-upstream', 'test', filename)

  File.readlines(filepath, encoding: "utf-8").each do |line|
    line_number += 1

    l = line.strip
    if l =~ /^`{32} example(.*)$/
      state = 1
      extensions = $1.split
    elsif l == '`' * 32
      state = 0
      example_number += 1
      end_line = line_number
      tests << {
        :markdown => markdown_lines.join('').tr('→', "\t"),
        :html => html_lines.join('').tr('→', "\t").rstrip,
        :example => example_number,
        :start_line => start_line,
        :end_line => end_line,
        :section => headertext,
        :extensions => extensions.map(&:to_sym),
      }
      start_line = 0
      markdown_lines = []
      html_lines = []
    elsif l == '.'
      state = 2
    elsif state == 1
      start_line = line_number - 1 if start_line == 0
      markdown_lines << "#{line}"
    elsif state == 2
      html_lines << "#{line}"
    elsif state == 0 && header_re.match(line)
      headertext = line.sub(header_re, '').strip
    end
  end

  tests
end

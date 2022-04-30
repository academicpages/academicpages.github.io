# frozen_string_literal: true

require 'benchmark/ips'
require 'commonmarker'
require 'redcarpet'
require 'kramdown'
require 'benchmark'

benchinput = File.read('test/benchinput.md').freeze

printf("input size = %<bytes>d bytes\n\n", { bytes: benchinput.bytesize })

Benchmark.ips do |x|
  x.report('redcarpet') do
    Redcarpet::Markdown.new(Redcarpet::Render::HTML, autolink: false, tables: false).render(benchinput)
  end

  x.report('commonmarker with to_html') do
    CommonMarker.render_html(benchinput)
  end

  x.report('commonmarker with to_xml') do
    CommonMarker.render_html(benchinput)
  end

  x.report('commonmarker with ruby HtmlRenderer') do
    CommonMarker::HtmlRenderer.new.render(CommonMarker.render_doc(benchinput))
  end

  x.report('commonmarker with render_doc.to_html') do
    CommonMarker.render_doc(benchinput, :DEFAULT, [:autolink]).to_html(:DEFAULT, [:autolink])
  end

  x.report('kramdown') do
    Kramdown::Document.new(benchinput).to_html(benchinput)
  end

  x.compare!
end

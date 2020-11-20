# frozen_string_literal: true

require "spec_helper"

describe(Jekyll::Converters::Markdown::CommonMark) do
  let(:options) { [] }
  let(:extensions) { [] }
  let(:config) do
    {
      "commonmark" => {
        "options"    => options,
        "extensions" => extensions,
      },
    }
  end
  let(:commonmark) { described_class.new(config) }
  let(:output) { commonmark.convert(content) }

  context "with default configuration" do
    it "produces the correct script tag" do
      actual = commonmark.convert("# Heading")
      expected = "<h1>Heading</h1>"
      expect(actual).to match(expected)
    end

    it "does not treat newlines as hardbreaks" do
      actual = commonmark.convert("a\nb")
      expected = "<p>a\nb</p>"
      expect(actual).to match(expected)
    end

    it "treats double linebreaks as a new paragraph" do
      actual = commonmark.convert("a\n\nb")
      expected = "<p>a</p>\n<p>b</p>"
      expect(actual).to match(expected)
    end

    it "escapes quotes" do
      actual = commonmark.convert('"SmartyPants"')
      expected = "<p>&quot;SmartyPants&quot;</p>"
      expect(actual).to match(expected)
    end

    it "does not link urls" do
      actual = commonmark.convert("https://example.com")
      expected = "https://example.com"
      expect(actual).to match(expected)
    end
  end

  context "with SmartyPants enabled" do
    let(:options) { ["SMART"] }

    it "makes quotes curly" do
      actual = commonmark.convert('"SmartyPants"')
      expected = "<p>“SmartyPants”</p>"
      expect(actual).to match(expected)
    end
  end

  context "with hardbreaks enabled" do
    let(:options) { ["HARDBREAKS"] }

    it "treats newlines as hardbreaks" do
      actual = commonmark.convert("a\nb")
      expected = "<p>a<br />\nb</p>"
      expect(actual).to match(expected)
    end
  end

  context "with nobreaks enabled" do
    let(:options) { ["NOBREAKS"] }

    it "treats newlines as a single space" do
      actual = commonmark.convert("a\nb")
      expected = "<p>a b</p>"
      expect(actual).to match(expected)
    end
  end

  context "with autolink enabled" do
    let(:extensions) { ["autolink"] }

    it "links urls" do
      actual = commonmark.convert("https://example.com")
      expected = '<p><a href="https://example.com">https://example.com</a></p>'
      expect(actual).to match(expected)
    end
  end
end

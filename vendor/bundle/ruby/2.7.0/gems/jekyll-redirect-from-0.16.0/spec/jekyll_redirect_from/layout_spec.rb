# frozen_string_literal: true

RSpec.describe JekyllRedirectFrom::Layout do
  subject { described_class.new(@site) }

  it "exposes the site" do
    expect(subject.site).to eql(@site)
  end

  it "exposes the name" do
    expect(subject.name).to eql("redirect.html")
  end

  it "exposes the path" do
    expected = File.expand_path "../../lib/jekyll-redirect-from/redirect.html", __dir__
    expect(subject.path).to eql(expected)
  end

  it "exposes the relative path" do
    expect(subject.relative_path).to eql("_layouts/redirect.html")
  end

  it "exposes the ext" do
    expect(subject.ext).to eql("html")
  end

  it "exposes data" do
    expect(subject.data).to eql({})
  end

  it "exposes content" do
    expect(subject.content).to match("Redirecting...")
  end
end

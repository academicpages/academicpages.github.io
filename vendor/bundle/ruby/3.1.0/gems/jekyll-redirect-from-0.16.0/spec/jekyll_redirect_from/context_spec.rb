# frozen_string_literal: true

RSpec.describe JekyllRedirectFrom::Context do
  subject { described_class.new(site) }

  it "stores the site" do
    expect(subject.site).to be_a(Jekyll::Site)
  end

  it "returns the register" do
    expect(subject.registers).to have_key(:site)
    expect(subject.registers[:site]).to be_a(Jekyll::Site)
  end
end

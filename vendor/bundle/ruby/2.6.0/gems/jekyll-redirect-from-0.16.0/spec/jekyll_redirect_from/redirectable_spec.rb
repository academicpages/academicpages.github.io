# frozen_string_literal: true

class RedirectableTestHelper
  include JekyllRedirectFrom::Redirectable
  attr_reader :to_liquid

  def initialize(data)
    @to_liquid = data
  end
end

RSpec.describe JekyllRedirectFrom::Redirectable do
  let(:data) { "" }
  subject { RedirectableTestHelper.new(data) }

  context "with strings" do
    let(:data) { { "redirect_from" => "/foo", "redirect_to" => "/bar" } }

    it "returns redirect_from" do
      expect(subject.redirect_from).to eql(["/foo"])
    end

    it "returns redirect_to" do
      expect(subject.redirect_to).to eql("/bar")
    end
  end

  context "with arrays" do
    let(:data) { { "redirect_from" => ["/foo"], "redirect_to" => ["/bar"] } }

    it "returns redirect_from" do
      expect(subject.redirect_from).to eql(["/foo"])
    end

    it "returns redirect_to" do
      expect(subject.redirect_to).to eql("/bar")
    end
  end

  context "with fields missing" do
    let(:data) { {} }

    it "returns an empty array for redirect_from" do
      expect(subject.redirect_from).to eql([])
    end

    it "returns nil for redirect_to" do
      expect(subject.redirect_to).to be_nil
    end
  end

  context "with nils" do
    let(:data) { { "redirect_from" => nil, "redirect_to" => nil } }

    it "returns an empty array for redirect_from" do
      expect(subject.redirect_from).to eql([])
    end

    it "returns nil for redirect_to" do
      expect(subject.redirect_to).to be_nil
    end
  end
end

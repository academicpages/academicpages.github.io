require 'spec_helper'

describe(Mercenary::Option) do
  let(:config_key)  { "largo" }
  let(:description) { "This is a description" }
  let(:switches)    { ['-l', '--largo'] }
  let(:option)      { described_class.new(config_key, [switches, description].flatten.reject(&:nil?)) }

  it "knows its config key" do
    expect(option.config_key).to eql(config_key)
  end

  it "knows its description" do
    expect(option.description).to eql(description)
  end

  it "knows its switches" do
    expect(option.switches).to eql(switches)
  end

  it "knows how to present itself" do
    expect(option.to_s).to eql("        -l, --largo        #{description}")
  end

  it "has an OptionParser representation" do
    expect(option.for_option_parser).to eql([switches, description].flatten)
  end

  it "compares itself with other options well" do
    new_option = described_class.new(config_key, ['-l', '--largo', description])
    expect(option.eql?(new_option)).to be(true)
    expect(option.hash.eql?(new_option.hash)).to be(true)
  end

  it "has a custom #hash" do
    expect(option.hash.to_s).to match(/\d+/)
  end

  context "with just the long switch" do
    let(:switches) { ['--largo'] }

    it "adds an empty string in place of the short switch" do
      expect(option.switches).to eql(['', '--largo'])
    end

    it "sets its description properly" do
      expect(option.description).to eql(description)
    end

    it "knows how to present the switch" do
      expect(option.formatted_switches).to eql("            --largo      ")
    end
  end

  context "with just the short switch" do
    let(:switches) { ['-l'] }

    it "adds an empty string in place of the long switch" do
      expect(option.switches).to eql(['-l', ''])
    end

    it "sets its description properly" do
      expect(option.description).to eql(description)
    end

    it "knows how to present the switch" do
      expect(option.formatted_switches).to eql("        -l               ")
    end
  end

  context "without a description" do
    let(:description) { nil }

    it "knows there is no description" do
      expect(option.description).to be(nil)
    end

    it "knows both inputs are switches" do
      expect(option.switches).to eql(switches)
    end
  end

end

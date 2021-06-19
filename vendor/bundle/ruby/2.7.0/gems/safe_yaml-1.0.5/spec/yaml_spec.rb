# See https://github.com/dtao/safe_yaml/issues/47

require "spec_helper"

describe YAML do
  context "when you've only required safe_yaml/load", :libraries => true do
    it "YAML.load doesn't get monkey patched" do
      expect(YAML.method(:load)).to eq(ORIGINAL_YAML_LOAD)
    end

    it "YAML.load_file doesn't get monkey patched" do
      expect(YAML.method(:load_file)).to eq(ORIGINAL_YAML_LOAD_FILE)
    end
  end
end

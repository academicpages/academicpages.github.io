require "spec_helper"

describe SafeYAML::Transform do
  it "should return the same encoding when decoding Base64" do
    value = "c3VyZS4="
    decoded = SafeYAML::Transform.to_proper_type(value, false, "!binary")

    expect(decoded).to eq("sure.")
    expect(decoded.encoding).to eq(value.encoding) if decoded.respond_to?(:encoding)
  end
end

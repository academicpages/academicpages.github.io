require "spec_helper"

describe SafeYAML::Transform::ToSymbol do
  def with_symbol_deserialization_value(value)
    symbol_deserialization_flag = SafeYAML::OPTIONS[:deserialize_symbols]
    SafeYAML::OPTIONS[:deserialize_symbols] = value

    yield

  ensure
    SafeYAML::OPTIONS[:deserialize_symbols] = symbol_deserialization_flag
  end

  def with_symbol_deserialization(&block)
    with_symbol_deserialization_value(true, &block)
  end

  def without_symbol_deserialization(&block)
    with_symbol_deserialization_value(false, &block)
  end

  it "returns true when the value matches a valid Symbol" do
    with_symbol_deserialization { expect(subject.transform?(":foo")[0]).to be_truthy }
  end

  it "returns true when the value matches a valid String+Symbol" do
    with_symbol_deserialization { expect(subject.transform?(':"foo"')[0]).to be_truthy }
  end

  it "returns true when the value matches a valid String+Symbol with 's" do
    with_symbol_deserialization { expect(subject.transform?(":'foo'")[0]).to be_truthy }
  end

  it "returns true when the value has special characters and is wrapped in a String" do
    with_symbol_deserialization { expect(subject.transform?(':"foo.bar"')[0]).to be_truthy }
  end

  it "returns false when symbol deserialization is disabled" do
    without_symbol_deserialization { expect(subject.transform?(":foo")).to be_falsey }
  end

  it "returns false when the value does not match a valid Symbol" do
    with_symbol_deserialization { expect(subject.transform?("foo")).to be_falsey }
  end

  it "returns false when the symbol does not begin the line" do
    with_symbol_deserialization do
      expect(subject.transform?("NOT A SYMBOL\n:foo")).to be_falsey
    end
  end
end

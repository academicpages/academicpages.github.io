require "spec_helper"

describe SafeYAML::Transform::ToInteger do
  it "returns true when the value matches a valid Integer" do
    expect(subject.transform?("10")).to eq([true, 10])
  end

  it "returns false when the value does not match a valid Integer" do
    expect(subject.transform?("foobar")).to be_falsey
  end

  it "returns false when the value spans multiple lines" do
    expect(subject.transform?("10\nNOT AN INTEGER")).to be_falsey
  end

  it "allows commas in the number" do
    expect(subject.transform?("1,000")).to eq([true, 1000])
  end

  it "correctly parses numbers in octal format" do
    expect(subject.transform?("010")).to eq([true, 8])
  end

  it "correctly parses numbers in hexadecimal format" do
    expect(subject.transform?("0x1FF")).to eq([true, 511])
  end

  it "defaults to a string for a number that resembles octal format but is not" do
    expect(subject.transform?("09")).to be_falsey
  end

  it "correctly parses 0 in decimal" do
    expect(subject.transform?("0")).to eq([true, 0])
  end

  it "defaults to a string for a number that resembles hexadecimal format but is not" do
    expect(subject.transform?("0x1G")).to be_falsey
  end

  it "correctly parses all formats in the YAML spec" do
    # canonical
    expect(subject.transform?("685230")).to eq([true, 685230])

    # decimal
    expect(subject.transform?("+685_230")).to eq([true, 685230])

    # octal
    expect(subject.transform?("02472256")).to eq([true, 685230])

    # hexadecimal:
    expect(subject.transform?("0x_0A_74_AE")).to eq([true, 685230])

    # binary
    expect(subject.transform?("0b1010_0111_0100_1010_1110")).to eq([true, 685230])

    # sexagesimal
    expect(subject.transform?("190:20:30")).to eq([true, 685230])
  end

  # see https://github.com/dtao/safe_yaml/pull/51
  it "strips out underscores before parsing decimal values" do
    expect(subject.transform?("_850_")).to eq([true, 850])
  end
end

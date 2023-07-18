require "spec_helper"

describe SafeYAML::Transform::ToFloat do
  it "returns true when the value matches a valid Float" do
    expect(subject.transform?("20.00")).to eq([true, 20.0])
  end

  it "returns false when the value does not match a valid Float" do
    expect(subject.transform?("foobar")).to be_falsey
  end

  it "returns false when the value spans multiple lines" do
    expect(subject.transform?("20.00\nNOT A FLOAT")).to be_falsey
  end

  it "correctly parses all formats in the YAML spec" do
    # canonical
    expect(subject.transform?("6.8523015e+5")).to eq([true, 685230.15])

    # exponentioal
    expect(subject.transform?("685.230_15e+03")).to eq([true, 685230.15])

    # fixed
    expect(subject.transform?("685_230.15")).to eq([true, 685230.15])

    # sexagesimal
    expect(subject.transform?("190:20:30.15")).to eq([true, 685230.15])

    # infinity
    expect(subject.transform?("-.inf")).to eq([true, (-1.0 / 0.0)])

    # not a number
    # NOTE: can't use == here since NaN != NaN
    success, result = subject.transform?(".NaN")
    expect(success).to be_truthy; expect(result).to be_nan
  end

  # issue 29
  it "returns false for the string '.'" do
    expect(subject.transform?(".")).to be_falsey
  end
end

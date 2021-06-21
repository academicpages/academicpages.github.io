require 'spec_helper'

require 'safe_yaml/store'

describe SafeYAML::Store do

  let(:file)    { 'spec/store.yaml' }
  let(:content) { "--- \nfoo: 42\n:bar: \"party\"\n" }

  before do
    # Rewrite file on every test, as its contents are potentially modified by
    # SafeYAML::Store#transaction
    File.open(file, 'w') { |f| f.write(content) }
  end

  def expect_safe_load(options = {})
    load_args = [content, options]
    load_args.insert(1, nil) if SafeYAML::YAML_ENGINE == 'psych'

    expect(SafeYAML).to receive(:load).with(*load_args).and_call_original
    expect(YAML).not_to receive(:load)
  end

  let(:init_args) { [file] }
  subject { described_class.new(*init_args) }

  it 'should be a YAML::Store' do
    expect(subject).to be_a(YAML::Store)
  end

  it 'should be a SafeYAML::Store' do
    expect(subject).to be_a(SafeYAML::Store)
  end

  it 'should use SafeYAML.load instead of YAML.load' do
    expect_safe_load
    expect(subject.transaction { subject['foo'] }).to eq(42)
  end

  it 'preserves default SafeYAML behavior' do
    expect(subject.transaction { subject[:bar] }).to eq(nil)
    expect(subject.transaction { subject[':bar'] }).to eq('party')
  end


  describe 'with options' do

    let(:init_args) { super().insert(2, :deserialize_symbols => true) }

    it 'should accept options for SafeYAML.load' do
      expect_safe_load(:deserialize_symbols => true)
      expect(subject.transaction { subject[:bar] }).to eq('party')
    end

  end

end

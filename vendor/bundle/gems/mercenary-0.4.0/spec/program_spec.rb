# frozen_string_literal: true

require "spec_helper"

describe(Mercenary::Program) do
  context "a basic program" do
    let(:program) { Mercenary::Program.new(:my_name) }

    it "can be created with just a name" do
      expect(program.name).to eql(:my_name)
    end

    it "can set its version" do
      version = Mercenary::VERSION
      program.version version
      expect(program.version).to eq(version)
    end
  end
end

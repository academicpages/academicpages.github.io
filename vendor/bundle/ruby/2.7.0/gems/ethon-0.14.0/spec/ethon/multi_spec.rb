# frozen_string_literal: true
require 'spec_helper'

describe Ethon::Multi do
  describe ".new" do
    it "inits curl" do
      expect(Ethon::Curl).to receive(:init)
      Ethon::Multi.new
    end

    context "when options not empty" do
      context "when pipelining is set" do
        let(:options) { { :pipelining => true } }

        it "sets pipelining" do
          expect_any_instance_of(Ethon::Multi).to receive(:pipelining=).with(true)
          Ethon::Multi.new(options)
        end
      end
    end
  end
end

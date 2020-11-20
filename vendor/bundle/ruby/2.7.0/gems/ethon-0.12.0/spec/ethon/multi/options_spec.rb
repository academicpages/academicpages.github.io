require 'spec_helper'

describe Ethon::Multi::Options do
  let(:multi) { Ethon::Multi.new }

  [
    :maxconnects, :pipelining, :socketdata, :socketfunction,
    :timerdata, :timerfunction, :max_total_connections
  ].each do |name|
    describe "#{name}=" do
      it "responds_to" do
        expect(multi).to respond_to("#{name}=")
      end

      it "sets option" do
        expect(Ethon::Curl).to receive(:set_option).with(name, anything, anything, anything)
        multi.method("#{name}=").call(1)
      end
    end
  end

  describe "#value_for" do
    context "when option in bool" do
      context "when value true" do
        let(:value) { true }

        it "returns 1" do
          expect(multi.method(:value_for).call(value, :bool)).to eq(1)
        end
      end

      context "when value false" do
        let(:value) { false }

        it "returns 0" do
          expect(multi.method(:value_for).call(value, :bool)).to eq(0)
        end
      end
    end


    context "when value in int" do
      let(:value) { "2" }

      it "returns value casted to int" do
        expect(multi.method(:value_for).call(value, :int)).to eq(2)
      end
    end

    context "when value in unspecific_options" do
      context "when value a string" do
        let(:value) { "www.example.\0com" }

        it "returns zero byte escaped string" do
          expect(multi.method(:value_for).call(value, nil)).to eq("www.example.\\0com")
        end
      end

      context "when value not a string" do
        let(:value) { 1 }

        it "returns value" do
          expect(multi.method(:value_for).call(value, nil)).to eq(1)
        end
      end
    end
  end
end

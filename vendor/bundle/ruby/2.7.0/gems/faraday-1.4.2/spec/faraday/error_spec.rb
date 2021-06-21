# frozen_string_literal: true

RSpec.describe Faraday::ClientError do
  describe '.initialize' do
    subject { described_class.new(exception, response) }
    let(:response) { nil }

    context 'with exception only' do
      let(:exception) { RuntimeError.new('test') }

      it { expect(subject.wrapped_exception).to eq(exception) }
      it { expect(subject.response).to be_nil }
      it { expect(subject.message).to eq(exception.message) }
      it { expect(subject.backtrace).to eq(exception.backtrace) }
      it { expect(subject.inspect).to eq('#<Faraday::ClientError wrapped=#<RuntimeError: test>>') }
      it { expect(subject.response_status).to be_nil }
    end

    context 'with response hash' do
      let(:exception) { { status: 400 } }

      it { expect(subject.wrapped_exception).to be_nil }
      it { expect(subject.response).to eq(exception) }
      it { expect(subject.message).to eq('the server responded with status 400') }
      it { expect(subject.inspect).to eq('#<Faraday::ClientError response={:status=>400}>') }
      it { expect(subject.response_status).to eq(400) }
    end

    context 'with string' do
      let(:exception) { 'custom message' }

      it { expect(subject.wrapped_exception).to be_nil }
      it { expect(subject.response).to be_nil }
      it { expect(subject.message).to eq('custom message') }
      it { expect(subject.inspect).to eq('#<Faraday::ClientError #<Faraday::ClientError: custom message>>') }
      it { expect(subject.response_status).to be_nil }
    end

    context 'with anything else #to_s' do
      let(:exception) { %w[error1 error2] }

      it { expect(subject.wrapped_exception).to be_nil }
      it { expect(subject.response).to be_nil }
      it { expect(subject.message).to eq('["error1", "error2"]') }
      it { expect(subject.inspect).to eq('#<Faraday::ClientError #<Faraday::ClientError: ["error1", "error2"]>>') }
      it { expect(subject.response_status).to be_nil }
    end

    context 'with exception string and response hash' do
      let(:exception) { 'custom message' }
      let(:response) { { status: 400 } }

      it { expect(subject.wrapped_exception).to be_nil }
      it { expect(subject.response).to eq(response) }
      it { expect(subject.message).to eq('custom message') }
      it { expect(subject.inspect).to eq('#<Faraday::ClientError response={:status=>400}>') }
      it { expect(subject.response_status).to eq(400) }
    end
  end
end

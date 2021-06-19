# frozen_string_literal: true

RSpec.describe Faraday::Adapter::Test do
  let(:stubs) do
    described_class::Stubs.new do |stub|
      stub.get('http://domain.test/hello') do
        [200, { 'Content-Type' => 'text/html' }, 'domain: hello']
      end

      stub.get('http://wrong.test/hello') do
        [200, { 'Content-Type' => 'text/html' }, 'wrong: hello']
      end

      stub.get('http://wrong.test/bait') do
        [404, { 'Content-Type' => 'text/html' }]
      end

      stub.get('/hello') do
        [200, { 'Content-Type' => 'text/html' }, 'hello']
      end

      stub.get('/method-echo') do |env|
        [200, { 'Content-Type' => 'text/html' }, env[:method].to_s]
      end

      stub.get(%r{\A/resources/\d+(?:\?|\z)}) do
        [200, { 'Content-Type' => 'text/html' }, 'show']
      end

      stub.get(%r{\A/resources/(specified)\z}) do |_env, meta|
        [200, { 'Content-Type' => 'text/html' }, "show #{meta[:match_data][1]}"]
      end
    end
  end

  let(:connection) do
    Faraday.new do |builder|
      builder.adapter :test, stubs
    end
  end

  let(:response) { connection.get('/hello') }

  context 'with simple path sets status' do
    subject { response.status }

    it { is_expected.to eq 200 }
  end

  context 'with simple path sets headers' do
    subject { response.headers['Content-Type'] }

    it { is_expected.to eq 'text/html' }
  end

  context 'with simple path sets body' do
    subject { response.body }

    it { is_expected.to eq 'hello' }
  end

  context 'with host points to the right stub' do
    subject { connection.get('http://domain.test/hello').body }

    it { is_expected.to eq 'domain: hello' }
  end

  describe 'can be called several times' do
    subject { connection.get('/hello').body }

    it { is_expected.to eq 'hello' }
  end

  describe 'can handle regular expression path' do
    subject { connection.get('/resources/1').body }

    it { is_expected.to eq 'show' }
  end

  describe 'can handle single parameter block' do
    subject { connection.get('/method-echo').body }

    it { is_expected.to eq 'get' }
  end

  describe 'can handle regular expression path with captured result' do
    subject { connection.get('/resources/specified').body }

    it { is_expected.to eq 'show specified' }
  end

  context 'with get params' do
    subject { connection.get('/param?a=1').body }

    before do
      stubs.get('/param?a=1') { [200, {}, 'a'] }
    end

    it { is_expected.to eq 'a' }
  end

  describe 'ignoring unspecified get params' do
    before do
      stubs.get('/optional?a=1') { [200, {}, 'a'] }
    end

    context 'with multiple params' do
      subject { connection.get('/optional?a=1&b=1').body }

      it { is_expected.to eq 'a' }
    end

    context 'with single param' do
      subject { connection.get('/optional?a=1').body }

      it { is_expected.to eq 'a' }
    end

    context 'without params' do
      subject(:request) { connection.get('/optional') }

      it do
        expect { request }.to raise_error(
          Faraday::Adapter::Test::Stubs::NotFound
        )
      end
    end
  end

  context 'with http headers' do
    before do
      stubs.get('/yo', 'X-HELLO' => 'hello') { [200, {}, 'a'] }
      stubs.get('/yo') { [200, {}, 'b'] }
    end

    context 'with header' do
      subject do
        connection.get('/yo') { |env| env.headers['X-HELLO'] = 'hello' }.body
      end

      it { is_expected.to eq 'a' }
    end

    context 'without header' do
      subject do
        connection.get('/yo').body
      end

      it { is_expected.to eq 'b' }
    end
  end

  describe 'different outcomes for the same request' do
    def make_request
      connection.get('/foo')
    end

    subject(:request) { make_request.body }

    before do
      stubs.get('/foo') { [200, { 'Content-Type' => 'text/html' }, 'hello'] }
      stubs.get('/foo') { [200, { 'Content-Type' => 'text/html' }, 'world'] }
    end

    context 'the first request' do
      it { is_expected.to eq 'hello' }
    end

    context 'the second request' do
      before do
        make_request
      end

      it { is_expected.to eq 'world' }
    end
  end

  describe 'yielding env to stubs' do
    subject { connection.get('http://foo.com/foo?a=1').body }

    before do
      stubs.get '/foo' do |env|
        expect(env[:url].path).to eq '/foo'
        expect(env[:url].host).to eq 'foo.com'
        expect(env[:params]['a']).to eq '1'
        expect(env[:request_headers]['Accept']).to eq 'text/plain'
        [200, {}, 'a']
      end

      connection.headers['Accept'] = 'text/plain'
    end

    it { is_expected.to eq 'a' }
  end

  describe 'params parsing' do
    subject { connection.get('http://foo.com/foo?a[b]=1').body }

    context 'with default encoder' do
      before do
        stubs.get '/foo' do |env|
          expect(env[:params]['a']['b']).to eq '1'
          [200, {}, 'a']
        end
      end

      it { is_expected.to eq 'a' }
    end

    context 'with nested encoder' do
      before do
        stubs.get '/foo' do |env|
          expect(env[:params]['a']['b']).to eq '1'
          [200, {}, 'a']
        end

        connection.options.params_encoder = Faraday::NestedParamsEncoder
      end

      it { is_expected.to eq 'a' }
    end

    context 'with flat encoder' do
      before do
        stubs.get '/foo' do |env|
          expect(env[:params]['a[b]']).to eq '1'
          [200, {}, 'a']
        end

        connection.options.params_encoder = Faraday::FlatParamsEncoder
      end

      it { is_expected.to eq 'a' }
    end
  end

  describe 'raising an error if no stub was found' do
    describe 'for request' do
      subject(:request) { connection.get('/invalid') { [200, {}, []] } }

      it { expect { request }.to raise_error described_class::Stubs::NotFound }
    end

    describe 'for specified host' do
      subject(:request) { connection.get('http://domain.test/bait') }

      it { expect { request }.to raise_error described_class::Stubs::NotFound }
    end

    describe 'for request without specified header' do
      subject(:request) { connection.get('/yo') }

      before do
        stubs.get('/yo', 'X-HELLO' => 'hello') { [200, {}, 'a'] }
      end

      it { expect { request }.to raise_error described_class::Stubs::NotFound }
    end
  end
end

# frozen_string_literal: true

# Requires Ruby with rspec and faraday gems.
# rspec client_spec.rb

require 'faraday'
require 'json'

# Example API client
class Client
  def initialize(conn)
    @conn = conn
  end

  def sushi(jname, params: {})
    res = @conn.get("/#{jname}", params)
    data = JSON.parse(res.body)
    data['name']
  end
end

RSpec.describe Client do
  let(:stubs)  { Faraday::Adapter::Test::Stubs.new }
  let(:conn)   { Faraday.new { |b| b.adapter(:test, stubs) } }
  let(:client) { Client.new(conn) }

  it 'parses name' do
    stubs.get('/ebi') do |env|
      # optional: you can inspect the Faraday::Env
      expect(env.url.path).to eq('/ebi')
      [
        200,
        { 'Content-Type': 'application/javascript' },
        '{"name": "shrimp"}'
      ]
    end

    # uncomment to trigger stubs.verify_stubbed_calls failure
    # stubs.get('/unused') { [404, {}, ''] }

    expect(client.sushi('ebi')).to eq('shrimp')
    stubs.verify_stubbed_calls
  end

  it 'handles 404' do
    stubs.get('/ebi') do
      [
        404,
        { 'Content-Type': 'application/javascript' },
        '{}'
      ]
    end
    expect(client.sushi('ebi')).to be_nil
    stubs.verify_stubbed_calls
  end

  it 'handles exception' do
    stubs.get('/ebi') do
      raise Faraday::ConnectionFailed, nil
    end

    expect { client.sushi('ebi') }.to raise_error(Faraday::ConnectionFailed)
    stubs.verify_stubbed_calls
  end

  context 'When the test stub is run in strict_mode' do
    let(:stubs) { Faraday::Adapter::Test::Stubs.new(strict_mode: true) }

    it 'verifies the all parameter values are identical' do
      stubs.get('/ebi?abc=123') do
        [
          200,
          { 'Content-Type': 'application/javascript' },
          '{"name": "shrimp"}'
        ]
      end

      # uncomment to raise Stubs::NotFound
      # expect(client.sushi('ebi', params: { abc: 123, foo: 'Kappa' })).to eq('shrimp')
      expect(client.sushi('ebi', params: { abc: 123 })).to eq('shrimp')
      stubs.verify_stubbed_calls
    end
  end

  context 'When the Faraday connection is configured with FlatParamsEncoder' do
    let(:conn) { Faraday.new(request: { params_encoder: Faraday::FlatParamsEncoder }) { |b| b.adapter(:test, stubs) } }

    it 'handles the same multiple URL parameters' do
      stubs.get('/ebi?a=x&a=y&a=z') { [200, { 'Content-Type' => 'application/json' }, '{"name": "shrimp"}'] }

      # uncomment to raise Stubs::NotFound
      # expect(client.sushi('ebi', params: { a: %w[x y] })).to eq('shrimp')
      expect(client.sushi('ebi', params: { a: %w[x y z] })).to eq('shrimp')
      stubs.verify_stubbed_calls
    end
  end
end

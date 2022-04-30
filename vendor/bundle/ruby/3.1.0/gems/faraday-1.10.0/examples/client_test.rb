# frozen_string_literal: true

# Requires Ruby with test-unit and faraday gems.
# ruby client_test.rb

require 'faraday'
require 'json'
require 'test/unit'

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

# Example API client test
class ClientTest < Test::Unit::TestCase
  def test_sushi_name
    stubs = Faraday::Adapter::Test::Stubs.new
    stubs.get('/ebi') do |env|
      # optional: you can inspect the Faraday::Env
      assert_equal '/ebi', env.url.path
      [
        200,
        { 'Content-Type': 'application/javascript' },
        '{"name": "shrimp"}'
      ]
    end

    # uncomment to trigger stubs.verify_stubbed_calls failure
    # stubs.get('/unused') { [404, {}, ''] }

    cli = client(stubs)
    assert_equal 'shrimp', cli.sushi('ebi')
    stubs.verify_stubbed_calls
  end

  def test_sushi_404
    stubs = Faraday::Adapter::Test::Stubs.new
    stubs.get('/ebi') do
      [
        404,
        { 'Content-Type': 'application/javascript' },
        '{}'
      ]
    end

    cli = client(stubs)
    assert_nil cli.sushi('ebi')
    stubs.verify_stubbed_calls
  end

  def test_sushi_exception
    stubs = Faraday::Adapter::Test::Stubs.new
    stubs.get('/ebi') do
      raise Faraday::ConnectionFailed, nil
    end

    cli = client(stubs)
    assert_raise Faraday::ConnectionFailed do
      cli.sushi('ebi')
    end
    stubs.verify_stubbed_calls
  end

  def test_strict_mode
    stubs = Faraday::Adapter::Test::Stubs.new(strict_mode: true)
    stubs.get('/ebi?abc=123') do
      [
        200,
        { 'Content-Type': 'application/javascript' },
        '{"name": "shrimp"}'
      ]
    end

    cli = client(stubs)
    assert_equal 'shrimp', cli.sushi('ebi', params: { abc: 123 })

    # uncomment to raise Stubs::NotFound
    # assert_equal 'shrimp', cli.sushi('ebi', params: { abc: 123, foo: 'Kappa' })
    stubs.verify_stubbed_calls
  end

  def test_non_default_params_encoder
    stubs = Faraday::Adapter::Test::Stubs.new(strict_mode: true)
    stubs.get('/ebi?a=x&a=y&a=z') do
      [
        200,
        { 'Content-Type': 'application/javascript' },
        '{"name": "shrimp"}'
      ]
    end
    conn = Faraday.new(request: { params_encoder: Faraday::FlatParamsEncoder }) do |builder|
      builder.adapter :test, stubs
    end

    cli = Client.new(conn)
    assert_equal 'shrimp', cli.sushi('ebi', params: { a: %w[x y z] })

    # uncomment to raise Stubs::NotFound
    # assert_equal 'shrimp', cli.sushi('ebi', params: { a: %w[x y] })
    stubs.verify_stubbed_calls
  end

  def client(stubs)
    conn = Faraday.new do |builder|
      builder.adapter :test, stubs
    end
    Client.new(conn)
  end
end

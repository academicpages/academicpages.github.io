require 'helper.rb'

class Upcase < BibTeX::Filter
  def apply(value)
    value.is_a?(::String) ? value.upcase : value
  end
end

class SuffixA < BibTeX::Filter
  def apply(value)
    value.is_a?(::String) ? "#{value}a" : value
  end
end

module BibTeX
  class ValueTest < Minitest::Spec
    describe '::create' do
      it 'should return a duplicate when called with a Value subclass' do
        val   = Value.new('value')
        names = Names.new(Name.new(first: 'first_name'))

        assert_equal val.dup,   Value.create(val)
        assert_equal names.dup, Value.create(names)
      end

      it 'should return a new Value object when called with other arguments' do
        assert_equal Value.new('value'), Value.create('value')
      end
    end

    describe 'when empty' do
      it 'should be equal to an empty string' do
        assert Value.new == ''
        assert Value.new('') == ''
      end
      it 'should be empty' do
        assert Value.new.empty?
        assert Value.new('').empty?
      end
      it 'should match an empty pattern' do
        assert Value.new =~ //
        assert Value.new('') =~ //
      end
    end

    describe '#join' do
      it 'should return empty string when empty' do
        assert_equal '', Value.new.join.to_s
        assert_equal '', Value.new('').join.to_s
      end
      it 'should return the string if atomic' do
        assert_equal 'foo', Value.new('foo').join.to_s
      end
      it 'should return a string concatenation of all strings when containing only strings' do
        assert_equal 'foobar', Value.new('foo', 'bar').join.to_s
        assert_equal 'foobar', Value.new(%w[foo bar]).join.to_s
      end
      it 'should should be atomic after join when containing only strings' do
        refute Value.new('foo', 'bar').atomic?
        assert Value.new('foo', 'bar').join.atomic?
      end
      it 'should do nothing when containing only symbols' do
        value = Value.new(:foo)
        assert_equal value, value.join
        value = Value.new(:foo, :bar)
        assert_equal value, value.join
      end
      it 'should do nothing when containing only symbols and a single string' do
        value = Value.new(:foo, 'bar')
        assert_equal value, value.join
        value = Value.new('foo', :bar)
        assert_equal value, value.join
      end
    end

    describe '#merge!' do
      it 'merges two strings by combining them' do
        assert_equal '"foo" # "bar"', Value.new('foo').merge!(Value.new('bar')).to_s
      end

      it 'does not duplicate existing tokens' do
        assert_equal 'foo', Value.new('foo').merge!(Value.new('foo')).to_s
      end
    end

    describe '#to_s' do
      it 'should return the string if atomic' do
        assert_equal 'foo bar', Value.new('foo bar').to_s
      end
      it 'should return the symbol as string when containing only a single symbol' do
        assert_equal 'foo', Value.new(:foo).to_s
      end
      it 'should return all string tokens concatenated by #' do
        assert_equal '"foo" # "bar"', Value.new('foo', 'bar').to_s
      end
      it 'should return all symbol tokens concatenated by #' do
        assert_equal 'foo # bar', Value.new(:foo, :bar).to_s
      end
      it 'should return all symbol and string tokens concatenated by #' do
        assert_equal 'foo # "bar"', Value.new(:foo, 'bar').to_s
        assert_equal '"foo" # bar', Value.new('foo', :bar).to_s
      end
    end

    describe 'conversions' do
      before do
        @values = [Value.new('foo'), Value.new('foo', :bar)]
      end

      describe '#convert' do
        it 'converts the value when given a filter instance' do
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert(Upcase.instance).to_s }
        end

        it 'converts the value when given a filter class' do
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert(Upcase).to_s }
        end

        it 'converts the value when given the name of a filter' do
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert(:upcase).to_s }
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert('upcase').to_s }
          assert_equal ['fooa', '"fooa" # bar'], @values.map { |v| v.convert('suffixa').to_s }
        end

        it 'applies multiple filters in the order passed' do
          @values.map { |v| v.convert(:upcase, :suffixa).to_s }.must_equal ['FOOa', '"FOOa" # bar']
          @values.map { |v| v.convert(:suffixa, :upcase).to_s }.must_equal ['FOOA', '"FOOA" # bar']
        end

        it 'converts the value when using a ghost method' do
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert_upcase.to_s }
        end

        it 'does not alter the value when using a filter name' do
          @values.each { |v| v.convert(:upcase) }
          assert_equal ['foo', '"foo" # bar'], @values.map(&:to_s)
        end

        it 'does not alter the value when using a ghost method' do
          @values.each(&:convert_upcase)
          assert_equal ['foo', '"foo" # bar'], @values.map(&:to_s)
        end

        it 'raises argument error when a filter cannot be resolved' do
          assert_raises ArgumentError do
            @values[0].convert(:foo)
          end

          assert_raises ArgumentError do
            @values[0].convert(:upcase, :foo)
          end
        end
      end

      describe '#convert!' do
        it 'converts the value when given the name of a filter' do
          assert_equal ['FOO', '"FOO" # bar'], @values.map { |v| v.convert!(:upcase).to_s }
        end

        it 'alters the value when given the name of a filter' do
          @values.each { |v| v.convert!(:upcase) }
          assert_equal ['FOO', '"FOO" # bar'], @values.map(&:to_s)
        end

        it 'alters the value when using a ghost method' do
          @values.each(&:convert_upcase!)
          assert_equal ['FOO', '"FOO" # bar'], @values.map(&:to_s)
        end
      end

      describe 'value' do
        it 'returns numbers as strings' do
          assert Value.new(42).v.is_a?(::String)
          assert Value.new(-42).v.is_a?(::String)
          assert Value.new('a42').v.is_a?(::String)
        end
      end

      describe '#to_s' do
        it 'accepts a :filter option and convert the values accordingly without changing the value' do
          assert_equal '"FOO" # bar', @values[1].to_s(filter: :upcase)
          assert_equal '"foo" # bar', @values[1].to_s
        end
      end
    end
  end
end

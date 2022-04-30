# frozen_string_literal: true

require 'test_helper'
require 'minitest/benchmark' if ENV['BENCH']

def markdown(str)
  CommonMarker.render_doc(str).to_html
end

# list of pairs consisting of input and a regex that must match the output.
pathological = {
  'nested strong emph' =>
              ["#{'*a **a ' * 65_000}b#{' a** a*' * 65_000}",
               Regexp.compile('(<em>a <strong>a ){65_000}b( a</strong> a</em>){65_000}')],
  'many emph closers with no openers' =>
               [('a_ ' * 65_000),
                Regexp.compile('(a[_] ){64999}a_')],
  'many emph openers with no closers' =>
               [('_a ' * 65_000),
                Regexp.compile('(_a ){64999}_a')],
  'many link closers with no openers' =>
               [('a]' * 65_000),
                Regexp.compile('(a\]){65_000}')],
  'many link openers with no closers' =>
               [('[a' * 65_000),
                Regexp.compile('(\[a){65_000}')],
  'mismatched openers and closers' =>
               [('*a_ ' * 50_000),
                Regexp.compile('([*]a[_] ){49999}[*]a_')],
  'link openers and emph closers' =>
               [('[ a_' * 50_000),
                Regexp.compile('(\[ a_){50000}')],
  'hard link/emph case' =>
               ['**x [a*b**c*](d)',
                Regexp.compile('\\*\\*x <a href=\'d\'>a<em>b</em><em>c</em></a>')],
  'nested brackets' =>
               ["#{'[' * 50_000}a#{']' * 50_000}",
                Regexp.compile('\[{50000}a\]{50000}')],
  'nested block quotes' =>
               ["#{'> ' * 50_000}a",
                Regexp.compile('(<blockquote>\n){50000}')],
  'U+0000 in input' =>
               ['abc\u0000de\u0000',
                Regexp.compile('abc\ufffd?de\ufffd?')]
}

pathological.each_pair do |name, description|
  define_method("test_#{name}") do
    input, = description
    assert markdown(input)
  end
end

if ENV['BENCH']
  class PathologicalInputsPerformanceTest < Minitest::Benchmark
    def test_bench_pathological_one
      assert_performance_linear 0.99 do |n|
        star = '*' * (n * 10)
        markdown("#{star}#{star}hi#{star}#{star}")
      end
    end

    def test_bench_pathological_two
      assert_performance_linear 0.99 do |n|
        c = '`t`t`t`t`t`t' * (n * 10)
        markdown(c)
      end
    end

    def test_bench_pathological_three
      assert_performance_linear 0.99 do |n|
        markdown(" [a]: #{'A' * n}\n\n#{'[a][]' * n}\n")
      end
    end

    def test_bench_pathological_four
      assert_performance_linear 0.5 do |n|
        markdown("#{'[' * n}a#{']' * n}")
      end
    end

    def test_bench_pathological_five
      assert_performance_linear 0.99 do |n|
        markdown("#{'**a *a ' * n}#{'a* a**' * n}")
      end
    end

    def test_bench_unbound_recursion
      assert_performance_linear 0.99 do |n|
        markdown("#{'[' * n}foo#{'](bar)' * n}")
      end
    end
  end
end

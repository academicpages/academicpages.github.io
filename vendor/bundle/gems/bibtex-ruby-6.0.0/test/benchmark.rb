# ruby -Ilib -rrubygems test/benchmark.rb

require 'benchmark'
include Benchmark

require 'bibtex'

# data = File.open(BibTeX::Test.fixtures(:benchmark)).read

input = <<~END
  @book{pickaxe,
  	Address = {Raleigh, North Carolina},
  	Author = {Thomas, Dave, and Fowler, Chad, and Hunt, Andy},
  	Date-Added = {2010-08-05 09:54:07 +0200},
  	Date-Modified = {2010-08-05 10:07:01 +0200},
  	Keywords = {ruby},
  	Publisher = {The Pragmatic Bookshelf},
  	Series = {The Facets of Ruby},
  	Title = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
  	Year = {2009}
  }
END

n = 31
k = 10
lexer = BibTeX::Lexer.new
# parser = BibTeX::Parser.new

f = []
g = []

# Ruby 1.9.3
format = Benchmark.const_defined?(:FMTSTR) ? Benchmark::FMTSTR : Benchmark::FORMAT

Benchmark.benchmark((' ' * 15) + CAPTION, 7, format, format('%14s:', 'sum(f)'), format('%14s:', 'sum(g)')) do |b|
  1.step(n, k) do |i|
    f << b.report(format('%14s:', "f(#{i})")) do
      i.times do
        lexer.data = input
        lexer.analyse
        # BibTeX::Parser.new.parse(input)
      end
    end

    data = input * i

    g << b.report(format('%14s:', "g(#{i})")) do
      lexer.data = data
      lexer.analyse
      # BibTeX::Parser.new.parse(data)
    end
  end

  [f.inject(:+), g.inject(:+)]
end

# require 'gnuplot'
#
# f = f.map(&:total)
# g = g.map(&:total)
#
# x = 1.step(n,k).to_a
#
# Gnuplot.open do |gp|
#   Gnuplot::Plot.new(gp) do |plot|
#
#     plot.title  'BibTeX-Ruby Benchmark'
#     plot.ylabel 't'
#     plot.xlabel 'n'
#
#     plot.data << Gnuplot::DataSet.new([x,f]) do |ds|
#       ds.with = 'linespoints'
#       ds.title = 'f'
#     end
#
#     plot.data << Gnuplot::DataSet.new([x,g]) do |ds|
#       ds.with = 'linespoints'
#       ds.title = 'g'
#     end
#
#   end
# end

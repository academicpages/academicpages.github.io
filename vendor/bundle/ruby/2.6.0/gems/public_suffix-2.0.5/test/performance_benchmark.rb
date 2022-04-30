require_relative "benchmark_helper"

iterations = 100_000

# force load
list = PublicSuffix::List.default

Benchmark.bmbm do |bm|
  bm.report "Top level TLD" do
    iterations.times do
      PublicSuffix.domain("example.com", list)
    end
  end

  bm.report "Top level TLD (subdomain)" do
    iterations.times do
      PublicSuffix.domain("www.example.com", list)
    end
  end

  bm.report "Unlisted TLD" do
    iterations.times do
      PublicSuffix.domain("example.example", list)
    end
  end

  bm.report "Unlisted TLD (subdomain)" do
    iterations.times do
      PublicSuffix.domain("www.example.example", list)
    end
  end

  bm.report "Crazy suffix" do
    iterations.times do
      PublicSuffix.domain("a.b.ide.kyoto.jp", list)
    end
  end
end

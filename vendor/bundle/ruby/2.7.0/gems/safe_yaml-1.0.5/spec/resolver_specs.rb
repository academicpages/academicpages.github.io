module ResolverSpecs
  def self.included(base)
    base.module_eval do
      let(:resolver) { nil }
      let(:result) { @result }

      before :each do
        # See the comment in the first before :each block in safe_yaml_spec.rb.
        require "safe_yaml"
      end

      def parse(yaml)
        tree = YAML.parse(yaml.unindent)
        @result = resolver.resolve_node(tree)
      end

      # Isn't this how I should've been doing it all along?
      def parse_and_test(yaml)
        safe_result = parse(yaml)

        exception_thrown = nil

        unsafe_result = begin
          YAML.unsafe_load(yaml)
        rescue Exception => e
          exception_thrown = e
        end

        if exception_thrown
          # If the underlying YAML parser (e.g. Psych) threw an exception, I'm
          # honestly not sure what the right thing to do is. For now I'll just
          # print a warning. Should SafeYAML fail when Psych fails?
          Kernel.warn "\n"
          Kernel.warn "Discrepancy between SafeYAML and #{SafeYAML::YAML_ENGINE} on input:\n"
          Kernel.warn "#{yaml.unindent}\n"
          Kernel.warn "SafeYAML result:"
          Kernel.warn "#{safe_result.inspect}\n"
          Kernel.warn "#{SafeYAML::YAML_ENGINE} result:"
          Kernel.warn "#{exception_thrown.inspect}\n"

        else
          expect(safe_result).to eq(unsafe_result)
        end
      end

      context "by default" do
        it "translates maps to hashes" do
          parse <<-YAML
            potayto: potahto
            tomayto: tomahto
          YAML

          expect(result).to eq({
            "potayto" => "potahto",
            "tomayto" => "tomahto"
          })
        end

        it "translates sequences to arrays" do
          parse <<-YAML
            - foo
            - bar
            - baz
          YAML

          expect(result).to eq(["foo", "bar", "baz"])
        end

        it "translates most values to strings" do
          parse "string: value"
          expect(result).to eq({ "string" => "value" })
        end

        it "does not deserialize symbols" do
          parse ":symbol: value"
          expect(result).to eq({ ":symbol" => "value" })
        end

        it "translates valid integral numbers to integers" do
          parse "integer: 1"
          expect(result).to eq({ "integer" => 1 })
        end

        it "translates valid decimal numbers to floats" do
          parse "float: 3.14"
          expect(result).to eq({ "float" => 3.14 })
        end

        it "translates valid dates" do
          parse "date: 2013-01-24"
          expect(result).to eq({ "date" => Date.parse("2013-01-24") })
        end

        it "translates valid true/false values to booleans" do
          parse <<-YAML
            - yes
            - true
            - no
            - false
          YAML

          expect(result).to eq([true, true, false, false])
        end

        it "translates valid nulls to nil" do
          parse <<-YAML
            - 
            - ~
            - null
          YAML

          expect(result).to eq([nil] * 3)
        end

        it "matches the behavior of the underlying YAML engine w/ respect to capitalization of boolean values" do
          parse_and_test <<-YAML
            - true
            - True
            - TRUE
            - tRue
            - TRue
            - False
            - FALSE
            - fAlse
            - FALse
          YAML

          # using Syck: [true, true, true, "tRue", "TRue", false, false, "fAlse", "FALse"]
          # using Psych: all booleans
        end

        it "matches the behavior of the underlying YAML engine w/ respect to capitalization of nil values" do
          parse_and_test <<-YAML
            - Null
            - NULL
            - nUll
            - NUll
          YAML

          # using Syck: [nil, nil, "nUll", "NUll"]
          # using Psych: all nils
        end

        it "translates quoted empty strings to strings (not nil)" do
          parse "foo: ''"
          expect(result).to eq({ "foo" => "" })
        end

        it "correctly reverse-translates strings encoded via #to_yaml" do
          parse "5.10".to_yaml
          expect(result).to eq("5.10")
        end

        it "does not specially parse any double-quoted strings" do
          parse <<-YAML
            - "1"
            - "3.14"
            - "true"
            - "false"
            - "2013-02-03"
            - "2013-02-03 16:27:00 -0600"
          YAML

          expect(result).to eq(["1", "3.14", "true", "false", "2013-02-03", "2013-02-03 16:27:00 -0600"])
        end

        it "does not specially parse any single-quoted strings" do
          parse <<-YAML
            - '1'
            - '3.14'
            - 'true'
            - 'false'
            - '2013-02-03'
            - '2013-02-03 16:27:00 -0600'
          YAML

          expect(result).to eq(["1", "3.14", "true", "false", "2013-02-03", "2013-02-03 16:27:00 -0600"])
        end

        it "deals just fine with nested maps" do
          parse <<-YAML
            foo:
              bar:
                marco: polo
          YAML

          expect(result).to eq({ "foo" => { "bar" => { "marco" => "polo" } } })
        end

        it "deals just fine with nested sequences" do
          parse <<-YAML
            - foo
            -
              - bar1
              - bar2
              -
                - baz1
                - baz2
          YAML

          expect(result).to eq(["foo", ["bar1", "bar2", ["baz1", "baz2"]]])
        end

        it "applies the same transformations to keys as to values" do
          parse <<-YAML
            foo: string
            :bar: symbol
            1: integer
            3.14: float
            2013-01-24: date
          YAML

          expect(result).to eq({
            "foo"  => "string",
            ":bar" => "symbol",
            1      => "integer",
            3.14   => "float",
            Date.parse("2013-01-24") => "date",
          })
        end

        it "applies the same transformations to elements in sequences as to all values" do
          parse <<-YAML
            - foo
            - :bar
            - 1
            - 3.14
            - 2013-01-24
          YAML

          expect(result).to eq(["foo", ":bar", 1, 3.14, Date.parse("2013-01-24")])
        end
      end

      context "for Ruby version #{RUBY_VERSION}" do
        it "translates valid time values" do
          parse "time: 2013-01-29 05:58:00 -0800"
          expect(result).to eq({ "time" => Time.utc(2013, 1, 29, 13, 58, 0) })
        end

        it "applies the same transformation to elements in sequences" do
          parse "- 2013-01-29 05:58:00 -0800"
          expect(result).to eq([Time.utc(2013, 1, 29, 13, 58, 0)])
        end

        it "applies the same transformation to keys" do
          parse "2013-01-29 05:58:00 -0800: time"
          expect(result).to eq({ Time.utc(2013, 1, 29, 13, 58, 0) => "time" })
        end
      end

      context "with symbol deserialization enabled" do
        before :each do
          SafeYAML::OPTIONS[:deserialize_symbols] = true
        end

        after :each do
          SafeYAML.restore_defaults!
        end

        it "translates values starting with ':' to symbols" do
          parse "symbol: :value"
          expect(result).to eq({ "symbol" => :value })
        end

        it "applies the same transformation to keys" do
          parse ":bar: symbol"
          expect(result).to eq({ :bar  => "symbol" })
        end

        it "applies the same transformation to elements in sequences" do
          parse "- :bar"
          expect(result).to eq([:bar])
        end
      end
    end
  end
end

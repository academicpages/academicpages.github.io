require "spec_helper"

describe YAML do
  def safe_load_round_trip(object, options={})
    yaml = object.to_yaml
    if SafeYAML::YAML_ENGINE == "psych"
      YAML.safe_load(yaml, nil, options)
    else
      YAML.safe_load(yaml, options)
    end
  end

  before :each do
    # Need to require this here (as opposed to somewhere up higher in the file)
    # to ensure that safe_yaml isn't loaded and therefore YAML isn't monkey-
    # patched, for tests that require only safe_yaml/load.
    require "safe_yaml"
    require "exploitable_back_door"

    SafeYAML.restore_defaults!
  end

  after :each do
    SafeYAML.restore_defaults!
  end

  describe "unsafe_load" do
    if SafeYAML::YAML_ENGINE == "psych" && RUBY_VERSION >= "1.9.3"
      it "allows exploits through objects defined in YAML w/ !ruby/hash via custom :[]= methods" do
        backdoor = YAML.unsafe_load("--- !ruby/hash:ExploitableBackDoor\nfoo: bar\n")
        expect(backdoor).to be_exploited_through_setter
      end

      it "allows exploits through objects defined in YAML w/ !ruby/object via the :init_with method" do
        backdoor = YAML.unsafe_load("--- !ruby/object:ExploitableBackDoor\nfoo: bar\n")
        expect(backdoor).to be_exploited_through_init_with
      end
    end

    it "allows exploits through objects w/ sensitive instance variables defined in YAML w/ !ruby/object" do
      backdoor = YAML.unsafe_load("--- !ruby/object:ExploitableBackDoor\nfoo: bar\n")
      expect(backdoor).to be_exploited_through_ivars
    end

    context "with special whitelisted tags defined" do
      before :each do
        SafeYAML::whitelist!(OpenStruct)
      end

      it "effectively ignores the whitelist (since everything is whitelisted)" do
        result = YAML.unsafe_load <<-YAML.unindent
          --- !ruby/object:OpenStruct 
          table: 
            :backdoor: !ruby/object:ExploitableBackDoor 
              foo: bar
        YAML

        expect(result).to be_a(OpenStruct)
        expect(result.backdoor).to be_exploited_through_ivars
      end
    end
  end

  describe "safe_load" do
    it "does NOT allow exploits through objects defined in YAML w/ !ruby/hash" do
      object = YAML.safe_load("--- !ruby/hash:ExploitableBackDoor\nfoo: bar\n")
      expect(object).not_to be_a(ExploitableBackDoor)
    end

    it "does NOT allow exploits through objects defined in YAML w/ !ruby/object" do
      object = YAML.safe_load("--- !ruby/object:ExploitableBackDoor\nfoo: bar\n")
      expect(object).not_to be_a(ExploitableBackDoor)
    end

    context "for YAML engine #{SafeYAML::YAML_ENGINE}" do
      if SafeYAML::YAML_ENGINE == "psych"
        let(:options) { nil }
        let(:arguments) { ["foo: bar", nil, options] }

        context "when no tags are whitelisted" do
          it "constructs a SafeYAML::PsychHandler to resolve nodes as they're parsed, for optimal performance" do
            expect(Psych::Parser).to receive(:new).with an_instance_of(SafeYAML::PsychHandler)
            # This won't work now; we just want to ensure Psych::Parser#parse was in fact called.
            YAML.safe_load(*arguments) rescue nil
          end
        end

        context "when whitelisted tags are specified" do
          let(:options) {
            { :whitelisted_tags => ["foo"] }
          }

          it "instead uses Psych to construct a full tree before examining the nodes" do
            expect(Psych).to receive(:parse)
            # This won't work now; we just want to ensure Psych::Parser#parse was in fact called.
            YAML.safe_load(*arguments) rescue nil
          end
        end
      end

      if SafeYAML::YAML_ENGINE == "syck"
        it "uses Syck internally to parse YAML" do
          expect(YAML).to receive(:parse).with("foo: bar")
          # This won't work now; we just want to ensure YAML::parse was in fact called.
          YAML.safe_load("foo: bar") rescue nil
        end
      end
    end

    it "loads a plain ol' YAML document just fine" do
      result = YAML.safe_load <<-YAML.unindent
        foo:
          number: 1
          boolean: true
          nil: ~
          string: Hello, there!
          symbol: :blah
          sequence:
            - hi
            - bye
      YAML

      expect(result).to eq({
        "foo" => {
          "number"   => 1,
          "boolean"  => true,
          "nil"      => nil,
          "string"   => "Hello, there!",
          "symbol"   => ":blah",
          "sequence" => ["hi", "bye"]
        }
      })
    end

    it "works for YAML documents with anchors and aliases" do
      result = YAML.safe_load <<-YAML
        - &id001 {}
        - *id001
        - *id001
      YAML

      expect(result).to eq([{}, {}, {}])
    end

    it "works for YAML documents with binary tagged keys" do
      result = YAML.safe_load <<-YAML
        ? !!binary >
          Zm9v
        : "bar"
        ? !!binary >
          YmFy
        : "baz"
      YAML

      expect(result).to eq({"foo" => "bar", "bar" => "baz"})
    end

    it "works for YAML documents with binary tagged values" do
      result = YAML.safe_load <<-YAML
        "foo": !!binary >
          YmFy
        "bar": !!binary >
          YmF6
      YAML

      expect(result).to eq({"foo" => "bar", "bar" => "baz"})
    end

    it "works for YAML documents with binary tagged array values" do
      result = YAML.safe_load <<-YAML
        - !binary |-
          Zm9v
        - !binary |-
          YmFy
      YAML

      expect(result).to eq(["foo", "bar"])
    end

    it "works for YAML documents with sections" do
      result = YAML.safe_load <<-YAML
        mysql: &mysql
          adapter: mysql
          pool: 30
        login: &login
          username: user
          password: password123
        development: &development
          <<: *mysql
          <<: *login
          host: localhost
      YAML

      expect(result).to eq({
        "mysql" => {
          "adapter" => "mysql",
          "pool"    => 30
        },
        "login" => {
          "username" => "user",
          "password" => "password123"
        },
        "development" => {
          "adapter"  => "mysql",
          "pool"     => 30,
          "username" => "user",
          "password" => "password123",
          "host"     => "localhost"
        }
      })
    end

    it "correctly prefers explicitly defined values over default values from included sections" do
      # Repeating this test 100 times to increase the likelihood of running into an issue caused by
      # non-deterministic hash key enumeration.
      100.times do
        result = YAML.safe_load <<-YAML
          defaults: &defaults
            foo: foo
            bar: bar
            baz: baz
          custom:
            <<: *defaults
            bar: custom_bar
            baz: custom_baz
        YAML

        expect(result["custom"]).to eq({
          "foo" => "foo",
          "bar" => "custom_bar",
          "baz" => "custom_baz"
        })
      end
    end

    it "works with multi-level inheritance" do
      result = YAML.safe_load <<-YAML
        defaults: &defaults
          foo: foo
          bar: bar
          baz: baz
        custom: &custom
          <<: *defaults
          bar: custom_bar
          baz: custom_baz
        grandcustom: &grandcustom
          <<: *custom
      YAML

      expect(result).to eq({
        "defaults"    => { "foo" => "foo", "bar" => "bar", "baz" => "baz" },
        "custom"      => { "foo" => "foo", "bar" => "custom_bar", "baz" => "custom_baz" },
        "grandcustom" => { "foo" => "foo", "bar" => "custom_bar", "baz" => "custom_baz" }
      })
    end

    it "returns false when parsing an empty document" do
      expect([
        YAML.safe_load(""),
        YAML.safe_load("     "),
        YAML.safe_load("\n")
      ]).to eq([false, false, false])
    end

    it "returns nil when parsing a single value representing nil" do
      expect([
        YAML.safe_load("~"),
        YAML.safe_load("null")
      ]).to eq([nil, nil])
    end

    context "with custom initializers defined" do
      before :each do
        if SafeYAML::YAML_ENGINE == "psych"
          SafeYAML::OPTIONS[:custom_initializers] = {
            "!set" => lambda { Set.new },
            "!hashiemash" => lambda { Hashie::Mash.new }
          }
        else
          SafeYAML::OPTIONS[:custom_initializers] = {
            "tag:yaml.org,2002:set" => lambda { Set.new },
            "tag:yaml.org,2002:hashiemash" => lambda { Hashie::Mash.new }
          }
        end
      end

      it "will use a custom initializer to instantiate an array-like class upon deserialization" do
        result = YAML.safe_load <<-YAML.unindent
          --- !set
          - 1
          - 2
          - 3
        YAML

        expect(result).to be_a(Set)
        expect(result.to_a).to match_array([1, 2, 3])
      end

      it "will use a custom initializer to instantiate a hash-like class upon deserialization" do
        result = YAML.safe_load <<-YAML.unindent
          --- !hashiemash
          foo: bar
        YAML

        expect(result).to be_a(Hashie::Mash)
        expect(result.to_hash).to eq({ "foo" => "bar" })
      end
    end

    context "with special whitelisted tags defined" do
      before :each do
        SafeYAML::whitelist!(OpenStruct)

        # Necessary for deserializing OpenStructs properly.
        SafeYAML::OPTIONS[:deserialize_symbols] = true
      end

      it "will allow objects to be deserialized for whitelisted tags" do
        result = YAML.safe_load("--- !ruby/object:OpenStruct\ntable:\n  foo: bar\n")
        expect(result).to be_a(OpenStruct)
        expect(result.instance_variable_get(:@table)).to eq({ "foo" => "bar" })
      end

      it "will not deserialize objects without whitelisted tags" do
        result = YAML.safe_load("--- !ruby/hash:ExploitableBackDoor\nfoo: bar\n")
        expect(result).not_to be_a(ExploitableBackDoor)
        expect(result).to eq({ "foo" => "bar" })
      end

      it "will not allow non-whitelisted objects to be embedded within objects with whitelisted tags" do
        result = YAML.safe_load <<-YAML.unindent
          --- !ruby/object:OpenStruct 
          table: 
            :backdoor: !ruby/object:ExploitableBackDoor 
              foo: bar
        YAML

        expect(result).to be_a(OpenStruct)
        expect(result.backdoor).not_to be_a(ExploitableBackDoor)
        expect(result.backdoor).to eq({ "foo" => "bar" })
      end

      context "with the :raise_on_unknown_tag option enabled" do
        before :each do
          SafeYAML::OPTIONS[:raise_on_unknown_tag] = true
        end

        after :each do
          SafeYAML.restore_defaults!
        end

        it "raises an exception if a non-nil, non-whitelisted tag is encountered" do
          expect {
            YAML.safe_load <<-YAML.unindent
              --- !ruby/object:Unknown
              foo: bar
            YAML
          }.to raise_error
        end

        it "checks all tags, even those within objects with trusted tags" do
          expect {
            YAML.safe_load <<-YAML.unindent
              --- !ruby/object:OpenStruct
              table:
                :backdoor: !ruby/object:Unknown
                  foo: bar
            YAML
          }.to raise_error
        end

        it "does not raise an exception as long as all tags are whitelisted" do
          result = YAML.safe_load <<-YAML.unindent
            --- !ruby/object:OpenStruct
            table:
              :backdoor:
                string: foo
                integer: 1
                float: 3.14
                symbol: :bar
                date: 2013-02-20
                array: []
                hash: {}
          YAML

          expect(result).to be_a(OpenStruct)
          expect(result.backdoor).to eq({
            "string"  => "foo",
            "integer" => 1,
            "float"   => 3.14,
            "symbol"  => :bar,
            "date"    => Date.parse("2013-02-20"),
            "array"   => [],
            "hash"    => {}
          })
        end

        it "does not raise an exception on the non-specific '!' tag" do
          result = nil
          expect { result = YAML.safe_load "--- ! 'foo'" }.to_not raise_error
          expect(result).to eq("foo")
        end

        context "with whitelisted custom class" do
          class SomeClass
            attr_accessor :foo
          end
          let(:instance) { SomeClass.new }

          before do
            SafeYAML::whitelist!(SomeClass)
            instance.foo = 'with trailing whitespace: '
          end

          it "does not raise an exception on the non-specific '!' tag" do
            result = nil
            expect { result = YAML.safe_load(instance.to_yaml) }.to_not raise_error
            expect(result.foo).to eq('with trailing whitespace: ')
          end
        end
      end
    end

    context "when options are passed direclty to #load which differ from the defaults" do
      let(:default_options) { {} }

      before :each do
        SafeYAML::OPTIONS.merge!(default_options)
      end

      context "(for example, when symbol deserialization is enabled by default)" do
        let(:default_options) { { :deserialize_symbols => true } }

        it "goes with the default option when it is not overridden" do
          silence_warnings do
            expect(YAML.load(":foo: bar")).to eq({ :foo => "bar" })
          end
        end

        it "allows the default option to be overridden on a per-call basis" do
          silence_warnings do
            expect(YAML.load(":foo: bar", :deserialize_symbols => false)).to eq({ ":foo" => "bar" })
            expect(YAML.load(":foo: bar", :deserialize_symbols => true)).to eq({ :foo => "bar" })
          end
        end
      end

      context "(or, for example, when certain tags are whitelisted)" do
        let(:default_options) {
          {
            :deserialize_symbols => true,
            :whitelisted_tags => SafeYAML::YAML_ENGINE == "psych" ?
              ["!ruby/object:OpenStruct"] :
              ["tag:ruby.yaml.org,2002:object:OpenStruct"]
          }
        }

        it "goes with the default option when it is not overridden" do
          result = safe_load_round_trip(OpenStruct.new(:foo => "bar"))
          expect(result).to be_a(OpenStruct)
          expect(result.foo).to eq("bar")
        end

        it "allows the default option to be overridden on a per-call basis" do
          result = safe_load_round_trip(OpenStruct.new(:foo => "bar"), :whitelisted_tags => [])
          expect(result).to eq({ "table" => { :foo => "bar" } })

          result = safe_load_round_trip(OpenStruct.new(:foo => "bar"), :deserialize_symbols => false, :whitelisted_tags => [])
          expect(result).to eq({ "table" => { ":foo" => "bar" } })
        end
      end
    end
  end

  describe "unsafe_load_file" do
    if SafeYAML::YAML_ENGINE == "psych" && RUBY_VERSION >= "1.9.3"
      it "allows exploits through objects defined in YAML w/ !ruby/hash via custom :[]= methods" do
        backdoor = YAML.unsafe_load_file "spec/exploit.1.9.3.yaml"
        expect(backdoor).to be_exploited_through_setter
      end
    end

    if SafeYAML::YAML_ENGINE == "psych" && RUBY_VERSION >= "1.9.2"
      it "allows exploits through objects defined in YAML w/ !ruby/object via the :init_with method" do
        backdoor = YAML.unsafe_load_file "spec/exploit.1.9.2.yaml"
        expect(backdoor).to be_exploited_through_init_with
      end
    end

    it "allows exploits through objects w/ sensitive instance variables defined in YAML w/ !ruby/object" do
      backdoor = YAML.unsafe_load_file "spec/exploit.1.9.2.yaml"
      expect(backdoor).to be_exploited_through_ivars
    end
  end

  describe "safe_load_file" do
    it "does NOT allow exploits through objects defined in YAML w/ !ruby/hash" do
      object = YAML.safe_load_file "spec/exploit.1.9.3.yaml"
      expect(object).not_to be_a(ExploitableBackDoor)
    end

    it "does NOT allow exploits through objects defined in YAML w/ !ruby/object" do
      object = YAML.safe_load_file "spec/exploit.1.9.2.yaml"
      expect(object).not_to be_a(ExploitableBackDoor)
    end
    
    it "returns false when parsing an empty file" do
      expect(YAML.safe_load_file("spec/issue49.yml")).to eq(false)
    end
  end

  describe "load" do
    let(:options) { {} }

    let (:arguments) {
      if SafeYAML::MULTI_ARGUMENT_YAML_LOAD
        ["foo: bar", nil, options]
      else
        ["foo: bar", options]
      end
    }

    context "as long as a :default_mode has been specified" do
      it "doesn't issue a warning for safe mode, since an explicit mode has been set" do
        SafeYAML::OPTIONS[:default_mode] = :safe
        expect(Kernel).not_to receive(:warn)
        YAML.load(*arguments)
      end

      it "doesn't issue a warning for unsafe mode, since an explicit mode has been set" do
        SafeYAML::OPTIONS[:default_mode] = :unsafe
        expect(Kernel).not_to receive(:warn)
        YAML.load(*arguments)
      end
    end

    context "when the :safe options is specified" do
      let(:safe_mode) { true }
      let(:options) { { :safe => safe_mode } }

      it "doesn't issue a warning" do
        expect(Kernel).not_to receive(:warn)
        YAML.load(*arguments)
      end

      it "calls #safe_load if the :safe option is set to true" do
        expect(YAML).to receive(:safe_load)
        YAML.load(*arguments)
      end

      context "when the :safe option is set to false" do
        let(:safe_mode) { false }

        it "calls #unsafe_load if the :safe option is set to false" do
          expect(YAML).to receive(:unsafe_load)
          YAML.load(*arguments)
        end
      end
    end

    it "issues a warning when the :safe option is omitted" do
      silence_warnings do
        expect(Kernel).to receive(:warn)
        YAML.load(*arguments)
      end
    end

    it "only issues a warning once (to avoid spamming an app's output)" do
      silence_warnings do
        expect(Kernel).to receive(:warn).once
        2.times { YAML.load(*arguments) }
      end
    end

    it "defaults to safe mode if the :safe option is omitted" do
      silence_warnings do
        expect(YAML).to receive(:safe_load)
        YAML.load(*arguments)
      end
    end

    context "with the default mode set to :unsafe" do
      before :each do
        SafeYAML::OPTIONS[:default_mode] = :unsafe
      end

      it "defaults to unsafe mode if the :safe option is omitted" do
        silence_warnings do
          expect(YAML).to receive(:unsafe_load)
          YAML.load(*arguments)
        end
      end

      it "calls #safe_load if the :safe option is set to true" do
        expect(YAML).to receive(:safe_load)
        YAML.load(*(arguments + [{ :safe => true }]))
      end
    end
  end

  describe "load_file" do
    let(:filename) { "spec/exploit.1.9.2.yaml" } # doesn't really matter

    it "issues a warning if the :safe option is omitted" do
      silence_warnings do
        expect(Kernel).to receive(:warn)
        YAML.load_file(filename)
      end
    end

    it "doesn't issue a warning as long as the :safe option is specified" do
      expect(Kernel).not_to receive(:warn)
      YAML.load_file(filename, :safe => true)
    end

    it "defaults to safe mode if the :safe option is omitted" do
      silence_warnings do
        expect(YAML).to receive(:safe_load_file)
        YAML.load_file(filename)
      end
    end

    it "calls #safe_load_file if the :safe option is set to true" do
      expect(YAML).to receive(:safe_load_file)
      YAML.load_file(filename, :safe => true)
    end

    it "calls #unsafe_load_file if the :safe option is set to false" do
      expect(YAML).to receive(:unsafe_load_file)
      YAML.load_file(filename, :safe => false)
    end

    context "with arbitrary object deserialization enabled by default" do
      before :each do
        SafeYAML::OPTIONS[:default_mode] = :unsafe
      end

      it "defaults to unsafe mode if the :safe option is omitted" do
        silence_warnings do
          expect(YAML).to receive(:unsafe_load_file)
          YAML.load_file(filename)
        end
      end

      it "calls #safe_load if the :safe option is set to true" do
        expect(YAML).to receive(:safe_load_file)
        YAML.load_file(filename, :safe => true)
      end
    end

    it "handles files starting with --- (see issue #48)" do
      expect(YAML.load_file("spec/issue48.txt", :safe => true)).to eq({
        "title" => "Blah",
        "key"   => "value"
      })
    end

    it "handles content starting with --- (see issue #48)" do
      yaml = File.read("spec/issue48.txt")
      expect(YAML.load(yaml, :safe => true)).to eq({
        "title" => "Blah",
        "key"   => "value"
      })
    end
  end

  describe "whitelist!" do
    context "not a class" do
      it "should raise" do
        expect { SafeYAML::whitelist! :foo }.to raise_error(/not a Class/)
        expect(SafeYAML::OPTIONS[:whitelisted_tags]).to be_empty
      end
    end

    context "anonymous class" do
      it "should raise" do
        expect { SafeYAML::whitelist! Class.new }.to raise_error(/cannot be anonymous/)
        expect(SafeYAML::OPTIONS[:whitelisted_tags]).to be_empty
      end
    end

    context "with a Class as its argument" do
      it "should configure correctly" do
        expect { SafeYAML::whitelist! OpenStruct }.to_not raise_error
        expect(SafeYAML::OPTIONS[:whitelisted_tags].grep(/OpenStruct\Z/)).not_to be_empty
      end

      it "successfully deserializes the specified class" do
        SafeYAML.whitelist!(OpenStruct)

        # necessary for properly assigning OpenStruct attributes
        SafeYAML::OPTIONS[:deserialize_symbols] = true

        result = safe_load_round_trip(OpenStruct.new(:foo => "bar"))
        expect(result).to be_a(OpenStruct)
        expect(result.foo).to eq("bar")
      end

      it "works for ranges" do
        SafeYAML.whitelist!(Range)
        expect(safe_load_round_trip(1..10)).to eq(1..10)
      end

      it "works for regular expressions" do
        SafeYAML.whitelist!(Regexp)
        expect(safe_load_round_trip(/foo/)).to eq(/foo/)
      end

      it "works for multiple classes" do
        SafeYAML.whitelist!(Range, Regexp)
        expect(safe_load_round_trip([(1..10), /bar/])).to eq([(1..10), /bar/])
      end

      it "works for arbitrary Exception subclasses" do
        class CustomException < Exception
          attr_reader :custom_message

          def initialize(custom_message)
            @custom_message = custom_message
          end
        end

        SafeYAML.whitelist!(CustomException)

        ex = safe_load_round_trip(CustomException.new("blah"))
        expect(ex).to be_a(CustomException)
        expect(ex.custom_message).to eq("blah")
      end
    end
  end
end

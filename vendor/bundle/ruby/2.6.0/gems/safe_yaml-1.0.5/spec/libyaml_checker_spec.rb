require "spec_helper"

describe SafeYAML::LibyamlChecker do
  describe "check_libyaml_version" do
    REAL_YAML_ENGINE = SafeYAML::YAML_ENGINE
    REAL_LIBYAML_VERSION = SafeYAML::LibyamlChecker::LIBYAML_VERSION

    let(:libyaml_patched) { false }

    before :each do
      allow(SafeYAML::LibyamlChecker).to receive(:libyaml_patched?).and_return(libyaml_patched)
    end

    after :each do
      silence_warnings do
        SafeYAML::YAML_ENGINE = REAL_YAML_ENGINE
        SafeYAML::LibyamlChecker::LIBYAML_VERSION = REAL_LIBYAML_VERSION
      end
    end

    def test_libyaml_version_ok(expected_result, yaml_engine, libyaml_version=nil)
      silence_warnings do
        SafeYAML.const_set("YAML_ENGINE", yaml_engine)
        SafeYAML::LibyamlChecker.const_set("LIBYAML_VERSION", libyaml_version)
        expect(SafeYAML::LibyamlChecker.libyaml_version_ok?).to eq(expected_result)
      end
    end

    unless defined?(JRUBY_VERSION)
      it "issues no warnings when 'Syck' is the YAML engine" do
        test_libyaml_version_ok(true, "syck")
      end

      it "issues a warning if Psych::LIBYAML_VERSION is not defined" do
        test_libyaml_version_ok(false, "psych")
      end

      it "issues a warning if Psych::LIBYAML_VERSION is < 0.1.6" do
        test_libyaml_version_ok(false, "psych", "0.1.5")
      end

      it "issues no warning if Psych::LIBYAML_VERSION is == 0.1.6" do
        test_libyaml_version_ok(true, "psych", "0.1.6")
      end

      it "issues no warning if Psych::LIBYAML_VERSION is > 0.1.6" do
        test_libyaml_version_ok(true, "psych", "1.0.0")
      end

      it "does a proper version comparison (not just a string comparison)" do
        test_libyaml_version_ok(true, "psych", "0.1.10")
      end

      context "when the system has a known patched libyaml version" do
        let(:libyaml_patched) { true }

        it "issues no warning, even when Psych::LIBYAML_VERSION < 0.1.6" do
          test_libyaml_version_ok(true, "psych", "0.1.4")
        end
      end
    end

    if defined?(JRUBY_VERSION)
      it "issues no warning, as JRuby doesn't use libyaml" do
        test_libyaml_version_ok(true, "psych", "0.1.4")
      end
    end
  end
end

require "spec_helper"

if SafeYAML::YAML_ENGINE == "syck"
  require "safe_yaml/syck_resolver"

  describe SafeYAML::SyckResolver do
    include ResolverSpecs
    let(:resolver) { SafeYAML::SyckResolver.new }
  end
end

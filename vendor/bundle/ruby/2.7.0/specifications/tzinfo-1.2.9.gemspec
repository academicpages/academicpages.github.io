# -*- encoding: utf-8 -*-
# stub: tzinfo 1.2.9 ruby lib

Gem::Specification.new do |s|
  s.name = "tzinfo".freeze
  s.version = "1.2.9"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Philip Ross".freeze]
  s.cert_chain = ["-----BEGIN CERTIFICATE-----\nMIIDPDCCAiSgAwIBAgIBATANBgkqhkiG9w0BAQsFADAkMSIwIAYDVQQDDBlwaGls\nLnJvc3MvREM9Z21haWwvREM9Y29tMB4XDTE5MTIyNDE0NTU0N1oXDTM5MTIyNDE0\nNTU0N1owJDEiMCAGA1UEAwwZcGhpbC5yb3NzL0RDPWdtYWlsL0RDPWNvbTCCASIw\nDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJGcwfqn4ZsmPl0b1Lt9dCzExrE5\nEeP/CRQjBdGHkF+mSpi69XysxdwLdfg5SPr9LfxthUug4nNFd5fDCiXM8hYe9jQD\nTmkIQKNBh4fFpGngn9gyy+SumCXi6b5L6d/aMc59NAOM6LJ88TOdH1648dh5rq3C\nULq82n3gg4+u0HHGjRPuR/pnCFQCZbANYdX+UBWd0qkOJn/EreNKROmEeHr/xKuh\n2/GlKFKt9KLcW3hwBB4fHHVYUzRau7D1m9KbEERdg//qNDC4B7fD2BFJuPbM5S7J\n41VwDAh1O8B/Qpg0f+S83K4Kodw4MiPGsug55UkNtd3mGR/zZJ9WM03DSwkCAwEA\nAaN5MHcwCQYDVR0TBAIwADALBgNVHQ8EBAMCBLAwHQYDVR0OBBYEFA+Z8zvfzBuA\nesoHIfz7+jxfUOcfMB4GA1UdEQQXMBWBE3BoaWwucm9zc0BnbWFpbC5jb20wHgYD\nVR0SBBcwFYETcGhpbC5yb3NzQGdtYWlsLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEA\nJ80xgZ3gGdQVA8N+8NJANU5HLuZIU9jOaAlziU9ImoTgPiOHKGZC4as1TwT4kBt1\nQcnu7YSANYRrxP5tpOHsWPF/MQYgerAFCZS5+PzOTudwZ+7OsMW4/EMHy6aCVHEd\nc7HzQRC4mSrDRpWxzyBnZ5nX5OAmIkKA8NgeKybT/4Ku6iFPPUQwlyxQaO+Wlxdo\nFqHwpjRyoiVSpe4RUTNK3d3qesWPYi7Lxn6k6ZZeEdvG6ya33AXktE3jmmF+jPR1\nJ3Zn/kSTjTekiaspyGbczC3PUaeJNxr+yCvR4sk71Xmk/GaKKGOHedJ1uj/LAXrA\nMR0mpl7b8zCg0PFC1J73uw==\n-----END CERTIFICATE-----\n".freeze]
  s.date = "2020-12-16"
  s.description = "TZInfo provides daylight savings aware transformations between times in different time zones.".freeze
  s.email = "phil.ross@gmail.com".freeze
  s.extra_rdoc_files = ["README.md".freeze, "CHANGES.md".freeze, "LICENSE".freeze]
  s.files = ["CHANGES.md".freeze, "LICENSE".freeze, "README.md".freeze]
  s.homepage = "https://tzinfo.github.io".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--title".freeze, "TZInfo".freeze, "--main".freeze, "README.md".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 1.8.7".freeze)
  s.rubygems_version = "3.1.2".freeze
  s.summary = "Daylight savings aware timezone library".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<thread_safe>.freeze, ["~> 0.1"])
  else
    s.add_dependency(%q<thread_safe>.freeze, ["~> 0.1"])
  end
end

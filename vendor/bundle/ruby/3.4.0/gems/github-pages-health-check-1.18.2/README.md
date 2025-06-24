# GitHub Pages Health Check

*Checks your GitHub Pages site for common DNS configuration issues*

[![Build Status](https://github.com/github/pages-health-check/actions/workflows/push-cibuild.yml/badge.svg)](https://github.com/github/pages-health-check/actions/workflows/push-cibuild.yml)
[![Gem Version](https://badge.fury.io/rb/github-pages-health-check.svg)](http://badge.fury.io/rb/github-pages-health-check)

## Installation

`gem install github-pages-health-check`

## Usage

### Basic Usage

```ruby
> check = GitHubPages::HealthCheck::Site.new("choosealicense.com")
=> #<GitHubPages::HealthCheck::Site @domain="choosealicense.com" valid?=true>
> check.valid?
=> true
```

### An invalid domain

```ruby
> check = GitHubPages::HealthCheck::Site.new("foo.github.com")
> check.valid?
=> false
> check.valid!
raises GitHubPages::HealthCheck::Errors::InvalidCNAMEError
```


### Retrieving specific checks

``` ruby
> check.domain.should_be_a_record?
=> true
> check.domain.a_record?
=> true
```

### Getting checks in bulk

```ruby
> check.to_hash
=> {
 :cloudflare_ip?=>false,
 :old_ip_address?=>false,
 :a_record?=>true,
 :cname_record?=>false,
 :valid_domain?=>true,
 :apex_domain?=>true,
 :should_be_a_record?=>true,
 :pointed_to_github_user_domain?=>false,
 :pointed_to_github_pages_ip?=>false,
 :pages_domain?=>false,
 :valid?=>true
}
> check.to_json
=> "{\"cloudflare_ip?\":false,\"old_ip_address?\":false,\"a_record?\":true,\"cname_record?\":false,\"valid_domain?\":true,\"apex_domain?\":true,\"should_be_a_record?\":true,\"pointed_to_github_user_domain?\":false,\"pointed_to_github_pages_ip?\":false,\"pages_domain?\":false,\"valid?\":true}"
```

### Getting the reason a domain is invalid

```ruby
> check = GitHubPages::HealthCheck::Site.new "developer.facebook.com"
> check.valid?
=> false
> check.reason
=> #<GitHubPages::HealthCheck::InvalidCNAME>
> check.reason.message
=> "CNAME does not point to GitHub Pages"
```

### Repository checks

Repository checks require a personal access or OAuth token with `repo` or scope. This can be passed as the second argument to the Site or Repository constructors like so:

```ruby
check = GitHubPages::HealthCheck::Site.new "github/pages-health-check", access_token: "1234
```

You can also set `OCTOKIT_ACCESS_TOKEN` as an environmental variable, or via a `.env` file in your working directory.

### Command Line

```
./script/check pages.github.com

host: pages.github.com
uri: https://pages.github.com/
nameservers: :default
dns_resolves?: true
proxied?: false
cloudflare_ip?: false
fastly_ip?: false
old_ip_address?: false
a_record?: false
cname_record?: true
mx_records_present?: false
valid_domain?: true
apex_domain?: false
should_be_a_record?: false
cname_to_github_user_domain?: true
cname_to_pages_dot_github_dot_com?: false
cname_to_fastly?: false
pointed_to_github_pages_ip?: false
non_github_pages_ip_present?: false
pages_domain?: true
served_by_pages?: true
valid?: true
reason:
https?: true
enforces_https?: true
https_error:
https_eligible?: true
caa_error:
dns_zone_soa?: false
dns_zone_ns?: false
```

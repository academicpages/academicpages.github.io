# Changelog

## v1.0

Initial release.
This release consists of the same middleware that was previously bundled with Faraday but removed in Faraday v2.0, plus:

### Fixed

*  Retry middleware `retry_block` is not called if retry will not happen due to `max_interval`, https://github.com/lostisland/faraday/pull/1350

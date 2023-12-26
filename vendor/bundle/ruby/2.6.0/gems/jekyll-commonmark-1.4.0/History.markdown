## 1.4.0 / 2022-01-30

### Minor Enhancements

  * Require at least commonmarker-0.22 (#44)
  * Highlight fenced code-block contents with Rouge (#29)

### Bug Fixes

  * Refactor away extra abstractions (#53)

### Development Fixes

  * DRY begin-rescue-end block with a private helper (#28)
  * Fix failing CI builds (#33)
  * Remove gemspec dependency on Jekyll (#34)
  * Test rendering with invalid configuration (#27)
  * Refactor to improve readability (#37)
  * Set up Continuous Integration via GH Actions (#46)
  * Clean up gemspec (#47)
  * Add workflow to release gem via GH Actions (#54)

### Documentation

  * Update README to link to commonmarker (#38)

## 1.3.1 / 2019-03-25

### Bug Fixes

  * Re-introduce Ruby 2.3 support and test Jekyll 3.7+ (#32)

## 1.3.0 / 2019-03-22

### Development Fixes

  * Allow Jekyll v4 (still alpha)
  * Drop Ruby < 2.4
  * chore(deps): rubocop-jekyll 0.3.0 (#25)
  * Target Ruby 2.4 (#30)

## 1.2.0 / 2018-03-29

### Minor Enhancements

  * Allow render options (#4)
  * Only set options once (#17)

### Development Fixes

  * Test plugin on Windows (#13)
  * Allow options passed to Rubocop (#15)
  * Add tests (#16)
  * Test against Ruby 2.5 (#18)
  * Version with class (#19)

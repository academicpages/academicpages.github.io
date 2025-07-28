---
title: 'Upgrading Python.org: From Django 4.2 to 5.2'
date: 2025-07-28
permalink: /posts/2025/07/python-org-django-5-upgrade/
tags:
  - django
  - python
  - infrastructure
  - psf
  - python software foundation
---

After months of waiting and plotting, [I've](https://github.com/JacobCoffee/) successfully upgraded Python.org from 
Django 4.2 to Django 5.2 almost a year after the upgrade from Django 2.2 to 4.2!

You can check out the [release notes for Django 5.0][django-5.0-release-notes], [Django 5.2][django-5.2-release-notes],
and a [great video from JetBrains][whats-news-in-django-5] that covers the major changes in Django 5.x.

This major version upgrade brings better async support and sets the foundation for future 
enhancements by requiring Python 3.10+, along with numerous bug fixes and minor improvements.

## The Challenge

Python.org serves millions of developers worldwide, hosting critical resources including:
- Python binaries for download
- Community resources and news
- Event calendars and job boards
- ...and more!

With such high impact, upgrading a major framework version requires a great deal of careful planning and testing. 
Python.org itself is very well tested with a comprehensive suite tests. We rely on these tests along with
time-gating the upgrade process until the LTS (Long Term Support) version of Django 5.2 is available
for some arbitrary period of time after its release.

One of our key considerations was dependency compatibility. We opted for a 'minimum viable upgrade' strategy where
we update packages only to meet Django 5's requirements rather than their latest versions. 

This meant upgrading from `foo==1.2` to `foo==1.9` (the minimum required) instead of jumping to `foo==2.0`, 
keeping our changes focused and testable. Separate feature branches can be created later to explore new features
and deal with any breaking changes in third-party packages.

## The Upgrade Process

Initially with all Django upgrades, we started with a fresh local environment and ran 
[adamchainz](https://github.com/adamchainz)'s [django-upgrade](https://github.com/adamchainz/django-upgrade)
tool to find and fix deprecation warnings. This tool is always immensely helpful!

Something to the tune of:

```shell
git ls-files -z -- '*.py' | xargs -0r uvx run django-upgrade --target-version 5.2
```

...or just using something like a pre-commit hook to run against the codebase.

### Cat and Mouse Game

After that, it was mostly fixing the few uncaught deprecation warnings (`length_is` was one)
and a cat a mouse game of updating dependency versions and running tests until everything was green.

One of the last to fall in line was [`django-pipeline`](github.com/jazzband/django-pipeline/issues/834),
but we are happy to report that it is now fully compatible with Django 5.2!

### Rollout

Ideally, we would have a staging environment to test the upgrade before deploying to production but due 
to the nature of Python.org's infrastructure, we opt for a direct upgrade on the production service.

This is where having a robust test suite and monitoring eases your nerves 😅.

## Lessons Learned

1. **Comprehensive Testing is mportant**: Our extensive test suite caught numerous edge cases before they reached production.

2. **Community Packages Matter**: Ensure third-party package compatibility early, because we rely on many!

3. **Monitoring gives you breathing room**: Monitoring during rollout allows us to quickly identify and address any issues.

## Thank You

This upgrade wouldn't have been possible without the dedication of the many package maintainers that Python.org relies on.
Stay tuned for more infrastructure updates as we continue improving Python.org for the global Python community!

---

*Have questions about the upgrade? Reach out via [Bluesky][bluesky] :)*

[//]: # (links)
[django-5.0-release-notes]: https://docs.djangoproject.com/en/5.0/releases/5.0/
[django-5.2-release-notes]: https://docs.djangoproject.com/en/5.2/releases/5.2/
[whats-news-in-django-5]: https://www.youtube.com/watch?v=PiftWvafq80
[bluesky]: https://bsky.app/profile/monorepo.bsky.social

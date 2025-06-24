---
title: Blah
key: value
---

I'm going to inject a bunch of YAML-looking stuff below and it should all just get ignored.

foo: bar

- foo
- bar

:foo
42
~

---
text: |
  Look, I'm another YAML document!
---

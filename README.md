## Navigating the repo

- Use `make lserve` to serve locally using the "local" config file
- Use `make serve` to use the real config file

## Notes

- See the [original repository](https://github.com/academicpages/academicpages.github.io) for help
- See the creator's [personal website](http://stuartgeiger.com/) and the [corresponding repo](https://github.com/staeiou/staeiou.github.io)

### Writing math

The GitHub Pages gem renders pages using kramdown and the MathJax option. This
leads to some weird results, where whole blocks get commented out. I found the simplest
answer was the bypass kramdown altogether by wrapping paragraphs around double-dollars:

```
<p>
$$
x = y
$$
</p>
```

This way, kramdown doesn't touch anything inside, and MathJax finds the `$$` and works
its normal magic.

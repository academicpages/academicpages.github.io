# prettier-plugin-go-template

[![NPM Badge](https://img.shields.io/npm/v/prettier-plugin-go-template)](https://www.npmjs.com/package/prettier-plugin-go-template) [![CodeCov Badge](https://img.shields.io/codecov/c/github/niklaspor/prettier-plugin-go-template)](https://codecov.io/gh/NiklasPor/prettier-plugin-go-template) [![Contributions Badge](https://img.shields.io/github/all-contributors/niklaspor/prettier-plugin-go-template)](#contributors-)

Formatter plugin for go template files. The only peer dependency is [prettier](https://www.npmjs.com/package/prettier).

```bash
npm install --save-dev prettier prettier-plugin-go-template
```

Starting with Prettier 3 auto-discovery has been removed. Configuration is required ⬇️

```json
// .prettierrc
{
  "plugins": ["prettier-plugin-go-template"]
}
```

The following file types will be detected automatically:
`.gohtml`, `.gotmpl`, `.go.tmpl`, `.tmpl`, `.tpl`, `.html.tmpl`
If you want to add support for `.html` read the section on it below the examples.

<table>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>

<!-- prettier-ignore-start -->
```html
{{ if or .Prev .Next -}}
{{ $p := where site.Pages }}
<div class="my-navigation">
{{ with $p.Next . -}}
<a href="{{ .RelPermalink }}">
<div class="row">
<div class="cell py-2">
  {{ .Title }} 
</div> </div> </a>
{{ end -}}
</div>
{{ end -}}
```
<!-- prettier-ignore-end -->

</td>
<td>

<!-- prettier-ignore-start -->
```html
{{ if or .Prev .Next -}}
  {{ $p := where site.Pages }}
  <div class="my-navigation">
    {{ with $p.Next . -}}
      <a href="{{ .RelPermalink }}">
        <div class="row">
          <div class="cell py-2">{{ .Title }}</div>
        </div>
      </a>
    {{ end -}}
  </div>
{{ end -}}
```
<!-- prettier-ignore-end -->

</td>
</tr>
</table>

## GoHugo / `.html`

To use it with GoHugo and basic `.html` files, you'll have to override the used parser inside your `.prettierrc` file:

```json
{
  "plugins": ["prettier-plugin-go-template"]
  "overrides": [
    {
      "files": ["*.html"],
      "options": {
        "parser": "go-template",
      },
    },
  ],
}
```

## VSCode

Make sure to always have installed **both** dependencies:

- `prettier`
- `prettier-plugin-go-template`

Also make sure that they are installed inside the same scope.
Install both globally (`npm i -g`) or locally – otherwise prettier may not pick up the plugin.

> Note: The global setup additional requires setting your VSCode prettier path to your global prettier path. You can read in [this issue](https://github.com/NiklasPor/prettier-plugin-go-template/issues/58#issuecomment-1085060511) how to set it up – should be doable in less than a minute if you have npm & VSCode already running.

## Additional Options

```js
// .prettierrc
{
  /**
   * Enables & disables spacing between go statements.
   * E.g. {{ statement }} vs {{statement}}.
   * Default: true
   */
  "goTemplateBracketSpacing": true
}
```

## Ignoring Code

#### Single Block

```html
<div>
  <!-- prettier-ignore -->
  {{if }}
  {{end }}
</div>
```

#### Multiline

```html
<html>
  {{/* prettier-ignore-start */}}
  <script>
    {{if }}
    Whatever.
    {{else }}
    Psych.
    {{end }}
  </script>
  {{/* prettier-ignore-end */}}
</html>
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/alqu"><img src="https://avatars1.githubusercontent.com/u/12250845?v=4?s=100" width="100px;" alt=""/><br /><sub><b>alqu</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Aalqu" title="Bug reports">🐛</a> <a href="https://github.com/NiklasPor/prettier-plugin-go-template/commits?author=alqu" title="Tests">⚠️</a> <a href="https://github.com/NiklasPor/prettier-plugin-go-template/commits?author=alqu" title="Code">💻</a></td>
    <td align="center"><a href="https://www.gabrielmaldi.com"><img src="https://avatars3.githubusercontent.com/u/3728897?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gabriel Monteagudo</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Agabrielmaldi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/bgold0"><img src="https://avatars1.githubusercontent.com/u/4645400?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Abgold0" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://richtera.org"><img src="https://avatars2.githubusercontent.com/u/708186?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Andreas Richter</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Arichtera" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://noahbrenner.github.io/"><img src="https://avatars3.githubusercontent.com/u/24858379?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Noah Brenner</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/commits?author=noahbrenner" title="Code">💻</a> <a href="https://github.com/NiklasPor/prettier-plugin-go-template/commits?author=noahbrenner" title="Documentation">📖</a></td>
    <td align="center"><a href="https://silverwind.io"><img src="https://avatars1.githubusercontent.com/u/115237?v=4?s=100" width="100px;" alt=""/><br /><sub><b>silverwind</b></sub></a><br /><a href="#ideas-silverwind" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://codeberg.org/cpence"><img src="https://avatars0.githubusercontent.com/u/297075?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Charles Pence</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Acpence" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://jasik.xyz"><img src="https://avatars.githubusercontent.com/u/10626596?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Caleb Jasik</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Ajasikpark" title="Bug reports">🐛</a> <a href="https://github.com/NiklasPor/prettier-plugin-go-template/commits?author=jasikpark" title="Documentation">📖</a> <a href="#example-jasikpark" title="Examples">💡</a> <a href="#ideas-jasikpark" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-jasikpark" title="Maintenance">🚧</a> <a href="#question-jasikpark" title="Answering Questions">💬</a></td>
    <td align="center"><a href="http://DanGold.me"><img src="https://avatars.githubusercontent.com/u/8890238?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dan Gold</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3ALandGod" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://mtlynch.io"><img src="https://avatars.githubusercontent.com/u/7783288?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael Lynch</b></sub></a><br /><a href="https://github.com/NiklasPor/prettier-plugin-go-template/issues?q=author%3Amtlynch" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

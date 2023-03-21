# node-imagemagick-cli

[![npm version](https://badge.fury.io/js/imagemagick-cli.svg)](https://badge.fury.io/js/imagemagick-cli) [![CircleCI](https://circleci.com/gh/dwmkerr/node-imagemagick-cli.svg?style=shield)](https://circleci.com/gh/dwmkerr/node-imagemagick-cli) [![Build status](https://ci.appveyor.com/api/projects/status/uwggloq6ooxq1vtj?svg=true)](https://ci.appveyor.com/project/dwmkerr/node-imagemagick-cli) [![codecov](https://codecov.io/gh/dwmkerr/node-imagemagick-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/dwmkerr/node-imagemagick-cli) [![dependencies Status](https://david-dm.org/dwmkerr/node-imagemagick-cli/status.svg)](https://david-dm.org/dwmkerr/node-imagemagick-cli) [![devDependencies Status](https://david-dm.org/dwmkerr/node-imagemagick-cli/dev-status.svg)](https://david-dm.org/dwmkerr/node-imagemagick-cli?type=dev) [![Greenkeeper badge](https://badges.greenkeeper.io/dwmkerr/node-imagemagick-cli.svg)](https://greenkeeper.io/)

Access the ImageMagick CLI tools from Node. Cross-platform, with support for ImageMagick 6 and 7.


<!-- vim-markdown-toc GFM -->

* [Introduction](#introduction)
* [Compatibility](#compatibility)
* [API](#api)
* [Debugging](#debugging)
* [Prior Art / Design Goals](#prior-art--design-goals)
* [Coding](#coding)
    * [Creating a Release](#creating-a-release)
* [License](#license)

<!-- vim-markdown-toc -->

## Introduction

This library is designed to provide a *safe* and *platform independent* way of calling the ImageMagick CLI tools.

It is *safe* because it correctly deals with the [Windows convert issue](http://www.imagemagick.org/Usage/windows/#convert_issue). It is *platform independent* because you don't have to worry about how it deals with the issue.

Install with npm:

```bash
npm install --save imagemagick-cli
```

To call an ImageMagick CLI tool, just run:

```node
const imagemagickCli = require('imagemagick-cli');
imagemagickCli.exec('convert -version');
```

This command will work consistently on MacOSX, Windows and Linux. On Windows, it will not conflict with the system installed `convert.exe` tool.

## Compatibility

This libary is tested with the following platforms and ImageMagick versions:

| Platform          | ImageMagick Version |
|-------------------|---------------------|
| OSX               | 6  ✅               |
| OSX               | 7  ✅               |
| Ubuntu            | 6  ✅               |
| Ubuntu            | 7  ✅               |
| Windows           | 6  ✅               |
| Windows           | 7  ✅               |

## API

Execute a command:

```node
imagemagickCli
    .exec('convert -version')
    .then(({ stdout, stderr }) => {
        console.log(`Output: ${stdout}`);
    });
```

Check the ImageMagick version:

```node
imagemagickCli
    .getVersion()
    .then((version) => {
        console.log(`Version: ${version}`);
    });
```

If the version cannot be identified (most likely because ImageMagick is not installed) then the function resolves with `null`.

## Debugging

This library uses the [`node-debug`](https://github.com/visionmedia/debug) module. To see low-level debugging information when using this library, set `imagemagick-cli` as part of the `DEBUG` environment variable:

```bash
DEBUG=imagemagick-cli node ./my-script.js
```

With debugging enabled, the full command sent to the CLI, as well as all `stderr` and `stdout` output is shown in the log.

## Prior Art / Design Goals

I made this library to deal with some issues relating to Windows in the [`app-icon`](https://github.com/dwmkerr/app-icon) project, which I didn't have to deal with again in other projects (like [`app-splash`](https://github.com/dwmkerr/app-splash).

There are some great and sophisticated modules around for working with IM:

- https://github.com/rsms/node-imagemagick
- https://github.com/yourdeveloper/node-imagemagick (which is the active fork of the above)
- https://github.com/elad/node-imagemagick-native

I decided to create my own library because I don't need *apis* for ImageMagick in my use cases, just a platform agnostic way to call the CLI tools. The design goals for this project are that it allows you to run IM CLI tools without having to worry about platform or version nuances, that's it.

If you need more functionality I recommend looking into the projects above.

## Coding

The only dependencies are Node 6 (or above).

Useful commands for development are:

| Command              | Usage                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| `npm test`           | Runs the unit tests.                                                                                           |
| `npm run test:debug` | Runs the tests in a debugger. Combine with `.only` and `debugger` for ease of debugging.                       |
| `npm run cov`        | Runs the tests, writing coverage reports to `./artifacts/coverage`.                                            |
| `npm run lint`       | Lint the code, using [airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb). |

### Creating a Release

To create a release.

- Merge your work to master.
- Use `npm run release` to bump and update the changelog
- Push and deploy `git push --follow-tags && npm publish`

## License

MIT

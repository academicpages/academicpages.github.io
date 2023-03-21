# Twemoji Parser [![Build Status](https://travis-ci.com/twitter/twemoji-parser.svg)](https://travis-ci.com/twitter/twemoji-parser)

A simple library for identifying emoji entities within a string in order to render them as Twemoji.

For example, this parser is used within the rendering flow for Tweets and other text on [mobile.twitter.com](https://mobile.twitter.com)

## Setup
Add `twemoji-parser` as a dependency to your project:
```
yarn add twemoji-parser
```

Or, to work directly in this repo, clone it and run `yarn install` from the repo root.

## Usage
The [tests](src/__tests__/index.test.js) are intended to serve as a more exhaustive source of documentation, but the general idea is that the parser takes a string and returns an array of the emoji entities it finds:
```js
import { parse } from 'twemoji-parser';
const entities = parse('I 🧡 Twemoji! 🥳');
/*
entities = [
  {
    url: 'https://twemoji.maxcdn.com/v/latest/svg/1f9e1.svg',
    indices: [ 2, 4 ],
    text: '🧡',
    type: 'emoji'
  },
  {
    url: 'https://twemoji.maxcdn.com/v/latest/svg/1f973.svg',
    indices: [ 12, 14 ],
    text: '🥳',
    type: 'emoji'
  }
]
*/
```
## Authors

* Nathan Downs <ndowns [at] twitter [dot] com>

Follow [@TwitterOSS](https://twitter.com/twitteross) on Twitter for updates.

## Contributing

We feel that a welcoming community is important and we ask that you follow Twitter's
[Open Source Code of Conduct](https://github.com/twitter/code-of-conduct/blob/master/code-of-conduct.md)
in all interactions with the community.

## Support

Create a [new issue](https://github.com/twitter/twemoji-parser/issues/new) on GitHub.

## Security Issues?
Please report sensitive security issues via Twitter's bug-bounty program (https://hackerone.com/twitter) rather than GitHub.

## License

MIT https://github.com/twitter/twemoji-parser/blob/master/LICENSE.md

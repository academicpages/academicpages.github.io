# merge-streams

> Merge multiple streams into a unified stream

## Install

```sh
npm install @sindresorhus/merge-streams
```

## Usage

```js
import mergeStreams from '@sindresorhus/merge-streams';

const stream = mergeStreams([streamA, streamB]);

for await (const chunk of stream) {
	console.log(chunk);
	//=> 'A1'
	//=> 'B1'
	//=> 'A2'
	//=> 'B2'
}
```

## API

### `mergeStreams(streams: stream.Readable[]): stream.Readable`

Merges an array of [readable streams](https://nodejs.org/api/stream.html#readable-streams) and returns a new readable stream that emits data from the individual streams as it arrives.

If you provide an empty array, it returns an already-ended stream.

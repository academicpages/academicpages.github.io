/**
Merges an array of [readable streams](https://nodejs.org/api/stream.html#readable-streams) and returns a new readable stream that emits data from the individual streams as it arrives.

If you provide an empty array, it returns an already-ended stream.

@example
```
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
*/
export default function mergeStreams(streams: NodeJS.ReadableStream[]): NodeJS.ReadableStream;

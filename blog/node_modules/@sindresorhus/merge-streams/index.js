import {PassThrough as PassThroughStream} from 'node:stream';

export default function mergeStreams(streams) {
	if (!Array.isArray(streams)) {
		throw new TypeError(`Expected an array, got \`${typeof streams}\`.`);
	}

	const passThroughStream = new PassThroughStream({objectMode: true});
	passThroughStream.setMaxListeners(Number.POSITIVE_INFINITY);

	if (streams.length === 0) {
		passThroughStream.end();
		return passThroughStream;
	}

	let activeStreams = streams.length;

	for (const stream of streams) {
		if (!(typeof stream?.pipe === 'function')) {
			throw new TypeError(`Expected a stream, got: \`${typeof stream}\`.`);
		}

		stream.pipe(passThroughStream, {end: false});

		stream.on('end', () => {
			activeStreams--;

			if (activeStreams === 0) {
				passThroughStream.end();
			}
		});

		stream.on('error', error => {
			passThroughStream.emit('error', error);
		});
	}

	return passThroughStream;
}

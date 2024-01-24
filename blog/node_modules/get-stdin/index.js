const {stdin} = process;

export default async function getStdin() {
	let result = '';

	if (stdin.isTTY) {
		return result;
	}

	stdin.setEncoding('utf8');

	for await (const chunk of stdin) {
		result += chunk;
	}

	return result;
}

getStdin.buffer = async () => {
	const result = [];
	let length = 0;

	if (stdin.isTTY) {
		return Buffer.concat([]);
	}

	for await (const chunk of stdin) {
		result.push(chunk);
		length += chunk.length;
	}

	return Buffer.concat(result, length);
};

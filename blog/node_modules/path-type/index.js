import fs, {promises as fsPromises} from 'fs';

async function isType(fsStatType, statsMethodName, filePath) {
	if (typeof filePath !== 'string') {
		throw new TypeError(`Expected a string, got ${typeof filePath}`);
	}

	try {
		const stats = await fsPromises[fsStatType](filePath);
		return stats[statsMethodName]();
	} catch (error) {
		if (error.code === 'ENOENT') {
			return false;
		}

		throw error;
	}
}

function isTypeSync(fsStatType, statsMethodName, filePath) {
	if (typeof filePath !== 'string') {
		throw new TypeError(`Expected a string, got ${typeof filePath}`);
	}

	try {
		return fs[fsStatType](filePath)[statsMethodName]();
	} catch (error) {
		if (error.code === 'ENOENT') {
			return false;
		}

		throw error;
	}
}

export const isFile = isType.bind(null, 'stat', 'isFile');
export const isDirectory = isType.bind(null, 'stat', 'isDirectory');
export const isSymlink = isType.bind(null, 'lstat', 'isSymbolicLink');
export const isFileSync = isTypeSync.bind(null, 'statSync', 'isFile');
export const isDirectorySync = isTypeSync.bind(null, 'statSync', 'isDirectory');
export const isSymlinkSync = isTypeSync.bind(null, 'lstatSync', 'isSymbolicLink');

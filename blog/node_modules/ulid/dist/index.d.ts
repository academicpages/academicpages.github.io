export interface PRNG {
    (): number;
}
export interface ULID {
    (seedTime?: number): string;
}
export interface LibError extends Error {
    source: string;
}
export declare function replaceCharAt(str: string, index: number, char: string): string;
export declare function incrementBase32(str: string): string;
export declare function randomChar(prng: PRNG): string;
export declare function encodeTime(now: number, len: number): string;
export declare function encodeRandom(len: number, prng: PRNG): string;
export declare function decodeTime(id: string): number;
export declare function detectPrng(allowInsecure?: boolean, root?: any): PRNG;
export declare function factory(currPrng?: PRNG): ULID;
export declare function monotonicFactory(currPrng?: PRNG): ULID;
export declare const ulid: ULID;

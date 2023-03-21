export type HashFunction = (text: string) => string;
declare const computeChecksum: HashFunction;
export default computeChecksum;

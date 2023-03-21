import { BlockInfo } from "./lib/block-info";
export interface CodeChunkData {
    /**
     * id of the code chunk
     */
    id: string;
    /**
     * code content of the code chunk
     */
    code: string;
    /**
     * code block info (normalized in advance)
     */
    normalizedInfo: BlockInfo;
    /**
     * result after running code chunk
     */
    plainResult: string;
    /**
     * result after formatting according to options['output'] format
     */
    result: string;
    /**
     * whether is running the code chunk or not
     */
    running: boolean;
    /**
     * previous code chunk
     */
    prev: string;
    /**
     * next code chunk
     */
    next: string;
}
export interface CodeChunksData {
    [key: string]: CodeChunkData;
}

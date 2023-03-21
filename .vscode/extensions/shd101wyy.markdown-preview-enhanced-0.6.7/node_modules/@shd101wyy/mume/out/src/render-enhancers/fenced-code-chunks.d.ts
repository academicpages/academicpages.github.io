/// <reference types="cheerio" />
import { CodeChunkData, CodeChunksData } from "../code-chunk-data";
import { BlockInfo } from "../lib/block-info";
import { MarkdownEngineRenderOption } from "../markdown-engine";
export default function enhance($: any, codeChunksData: CodeChunksData, renderOptions: MarkdownEngineRenderOption, runOptions: RunCodeChunkOptions): Promise<void>;
export declare function renderCodeBlock($container: Cheerio, normalizedInfo: BlockInfo, $: CheerioStatic, codeChunksData: CodeChunksData, arrayOfCodeChunkData: CodeChunkData[], renderOptions: MarkdownEngineRenderOption, runOptions: RunCodeChunkOptions): Promise<void>;
export interface RunCodeChunkOptions {
    enableScriptExecution: boolean;
    fileDirectoryPath: string;
    filePath: string;
    imageFolderPath: string;
    latexEngine: any;
    modifySource: any;
    parseMD: any;
    headings: any;
    resolveFilePath: any;
}
export declare function runCodeChunk(id: string, codeChunksData: CodeChunksData, runOptions: RunCodeChunkOptions): Promise<string>;
export declare function runCodeChunks(codeChunksData: CodeChunksData, runOptions: RunCodeChunkOptions): Promise<any[]>;

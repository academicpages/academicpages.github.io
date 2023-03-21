import HeadingIdGenerator from "./heading-id-generator";
export interface HeadingData {
    content: string;
    level: number;
    id: string;
}
export interface TransformMarkdownOutput {
    outputString: string;
    /**
     * An array of slide configs.
     */
    slideConfigs: object[];
    /**
     * whehter we found [TOC] in markdown file or not.
     */
    tocBracketEnabled: boolean;
    /**
     * imported javascript and css files
     * convert .js file to <script src='...'></script>
     * convert .css file to <link href='...'></link>
     */
    JSAndCssFiles: string[];
    headings: HeadingData[];
    /**
     * Get `---\n...\n---\n` string.
     */
    frontMatterString: string;
}
export interface TransformMarkdownOptions {
    fileDirectoryPath: string;
    projectDirectoryPath: string;
    filesCache: {
        [key: string]: string;
    };
    useRelativeFilePath: boolean;
    forPreview: boolean;
    forMarkdownExport?: boolean;
    protocolsWhiteListRegExp: RegExp;
    notSourceFile?: boolean;
    imageDirectoryPath?: string;
    usePandocParser: boolean;
    headingIdGenerator?: HeadingIdGenerator;
    onWillTransformMarkdown?: (markdown: string) => Promise<string>;
    onDidTransformMarkdown?: (markdown: string) => Promise<string>;
}
/**
 *
 * @param inputString
 * @param fileDirectoryPath
 * @param projectDirectoryPath
 * @param param3
 */
export declare function transformMarkdown(inputString: string, { fileDirectoryPath, projectDirectoryPath, filesCache, useRelativeFilePath, forPreview, forMarkdownExport, protocolsWhiteListRegExp, notSourceFile, imageDirectoryPath, usePandocParser, headingIdGenerator, onWillTransformMarkdown, onDidTransformMarkdown, }: TransformMarkdownOptions): Promise<TransformMarkdownOutput>;

export declare function toSVGMarkdown(texFilePath: string, { latexEngine, svgDirectoryPath, markdownDirectoryPath, svgZoom, svgWidth, svgHeight, }: {
    latexEngine: string;
    svgDirectoryPath?: string;
    markdownDirectoryPath: string;
    svgZoom?: string;
    svgWidth?: string;
    svgHeight?: string;
}): Promise<string>;

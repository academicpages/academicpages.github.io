export declare function toSVGMarkdown(pdfFilePath: string, { svgDirectoryPath, markdownDirectoryPath, svgZoom, svgWidth, svgHeight, }: {
    markdownDirectoryPath: string;
    svgDirectoryPath?: string;
    svgZoom?: string;
    svgWidth?: string;
    svgHeight?: string;
}): Promise<string>;

/// <reference types="cheerio" />
import { MarkdownEngineConfig } from "../markdown-engine-config";
/**
 * Embed local images. Load the image file and display it in base64 format
 */
export default function enhance($: CheerioStatic, options: MarkdownEngineConfig, resolveFilePath: (path: string, useRelativeFilePath: boolean) => string): Promise<void>;

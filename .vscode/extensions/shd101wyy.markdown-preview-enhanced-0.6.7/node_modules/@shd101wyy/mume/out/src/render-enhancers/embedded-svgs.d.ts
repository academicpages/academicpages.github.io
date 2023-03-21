/// <reference types="cheerio" />
import { MarkdownEngineConfig } from "../mume";
/**
 * Load local svg files and embed them into html directly.
 * @param $
 */
export default function enhance($: CheerioStatic, options: MarkdownEngineConfig, resolveFilePath: (path: string, useRelativeFilePath: boolean) => string): Promise<void>;

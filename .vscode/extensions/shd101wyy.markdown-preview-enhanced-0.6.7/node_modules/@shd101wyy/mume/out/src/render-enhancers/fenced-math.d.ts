import { MathRenderingOption } from "../markdown-engine-config";
/**
 * Enhances the document with literate fenced math
 * Attributes supported:
 * - literate [=true] if false, no math rendering happens
 * - hide [=true] if set to false, both code and output are shown
 * - output_first [=false] if true, math output shows before the code block (requires hide=false)
 *
 * @param renderingOption which math engine to use
 * @param $ cheerio element containing the entire document
 */
export default function enhance($: any, renderingOption: MathRenderingOption, mathBlockDelimiters: string[][]): Promise<void>;

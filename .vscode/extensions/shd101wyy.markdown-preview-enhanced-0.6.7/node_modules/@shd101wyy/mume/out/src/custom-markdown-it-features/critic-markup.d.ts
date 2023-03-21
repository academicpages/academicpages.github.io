/**
 * critic markup	              HTML         	          LaTeX
 * {--[text]--}	          <del>[text]</del>	                    \st{[text]}
 * {++[text]++}          	<ins>[text]</ins>	                    \underline{[text]}
 * {~~[text1]~>[text2]~~}	<del>[text1]</del><ins>[text2]</ins>	\st{[text1]}\underline{[text2]}
 * {==[text]==}          	<mark>[text]</mark>	                  \hl{[text]}
 * {>>[text]<<}          	<aside>[text]</aside>                	\marginpar{[text]}
 */
import { MarkdownIt } from "markdown-it";
import { MarkdownEngineConfig } from "../markdown-engine-config";
declare const _default: (md: MarkdownIt, config: MarkdownEngineConfig) => void;
export default _default;

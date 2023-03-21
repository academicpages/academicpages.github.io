"use strict";
/**
 * critic markup	              HTML         	          LaTeX
 * {--[text]--}	          <del>[text]</del>	                    \st{[text]}
 * {++[text]++}          	<ins>[text]</ins>	                    \underline{[text]}
 * {~~[text1]~>[text2]~~}	<del>[text1]</del><ins>[text2]</ins>	\st{[text1]}\underline{[text2]}
 * {==[text]==}          	<mark>[text]</mark>	                  \hl{[text]}
 * {>>[text]<<}          	<aside>[text]</aside>                	\marginpar{[text]}
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = (md, config) => {
    // @ts-ignore
    md.inline.ruler.before("strikethrough", "critic-markup", (state, silent) => {
        if (!config.enableCriticMarkupSyntax) {
            return false;
        }
        const { src, pos } = state;
        if (src[pos] === "{" &&
            ((src[pos + 1] === "-" && src[pos + 2] === "-") ||
                (src[pos + 1] === "+" && src[pos + 2] === "+") ||
                (src[pos + 1] === "~" && src[pos + 2] === "~") ||
                (src[pos + 1] === "=" && src[pos + 2] === "=") ||
                (src[pos + 1] === ">" && src[pos + 2] === ">"))) {
            const tag = src.slice(pos + 1, pos + 3);
            const closeTag = tag[0] === ">" ? "<<}" : `${tag}}`;
            let i = pos + 3;
            let end = -1;
            let content = null;
            while (i < src.length) {
                if (src.startsWith(closeTag, i)) {
                    end = i;
                    break;
                }
                i += 1;
            }
            if (end >= 0) {
                content = src.slice(pos + 3, end);
            }
            else {
                return false;
            }
            if (content && !silent) {
                const token = state.push("critic-markup");
                token.content = content;
                token.tag = tag;
                state.pos = end + closeTag.length;
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    });
    /**
     * CriticMarkup renderer
     */
    md.renderer.rules["critic-markup"] = (tokens, idx) => {
        const token = tokens[idx];
        const tag = token.tag;
        const content = token.content;
        if (tag === "--") {
            return `<del>${content}</del>`;
        }
        else if (tag === "++") {
            return `<ins>${content}</ins>`;
        }
        else if (tag === "==") {
            return `<mark>${content}</mark>`;
        }
        else if (tag === ">>") {
            return `<span style="display:none">${content}</span>`;
        }
        else {
            // {~~[text1]~>[text2]~~}
            const arr = content.split("~>");
            if (arr.length === 2) {
                return `<del>${arr[0]}</del><ins>${arr[1]}</ins>`;
            }
            else {
                return `<code>Error: ~> not found.</code>`;
            }
        }
    };
};
//# sourceMappingURL=critic-markup.js.map
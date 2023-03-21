"use strict";
/**
 * inline [[]]
 * [[...]]
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = (md, config) => {
    // @ts-ignore
    md.inline.ruler.before("autolink", "wikilink", (state, silent) => {
        if (!config.enableWikiLinkSyntax ||
            !state.src.startsWith("[[", state.pos)) {
            return false;
        }
        let content = null;
        const tag = "]]";
        let end = -1;
        let i = state.pos + tag.length;
        while (i < state.src.length) {
            if (state.src[i] === "\\") {
                i += 1;
            }
            else if (state.src.startsWith(tag, i)) {
                end = i;
                break;
            }
            i += 1;
        }
        if (end >= 0) {
            // found ]]
            content = state.src.slice(state.pos + tag.length, end);
        }
        else {
            return false;
        }
        if (content && !silent) {
            const token = state.push("wikilink");
            token.content = content;
            state.pos += content.length + 2 * tag.length;
            return true;
        }
        else {
            return false;
        }
    });
    md.renderer.rules.wikilink = (tokens, idx) => {
        const { content } = tokens[idx];
        if (!content) {
            return;
        }
        const splits = content.split("|");
        let wikiLink;
        let linkText;
        if (splits.length === 1) {
            linkText = splits[0].trim();
            const filename = linkText.replace(/\s/g, "_");
            wikiLink = `${filename}${config.wikiLinkFileExtension}`;
        }
        else {
            if (config.useGitHubStylePipedLink) {
                linkText = splits[0].trim();
                wikiLink = `${splits[1].trim()}${config.wikiLinkFileExtension}`;
            }
            else {
                linkText = splits[1].trim();
                wikiLink = `${splits[0].trim()}${config.wikiLinkFileExtension}`;
            }
        }
        return `<a href="${wikiLink}">${linkText}</a>`;
    };
};
//# sourceMappingURL=wikilink.js.map
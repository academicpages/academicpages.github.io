"use strict";
/**
 * A wrapper of mermaid CLI
 * https://github.com/mermaid-js/mermaid-cli
 */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.mermaidToPNG = void 0;
const utility = require("./utility");
function mermaidToPNG(mermaidCode, pngFilePath, projectDirectoryPath, themeName) {
    return __awaiter(this, void 0, void 0, function* () {
        const info = yield utility.tempOpen({
            prefix: "mume-mermaid",
            suffix: ".mmd",
        });
        yield utility.write(info.fd, mermaidCode);
        if (!themeName) {
            themeName = "null";
        }
        try {
            yield utility.execFile("npx", [
                "-p",
                "@mermaid-js/mermaid-cli",
                "mmdc",
                "--theme",
                themeName,
                "--input",
                info.path,
                "--output",
                pngFilePath,
            ], {
                shell: true,
                cwd: projectDirectoryPath,
            });
            return pngFilePath;
        }
        catch (error) {
            throw new Error("mermaid CLI is required to be installed.\nCheck https://github.com/mermaid-js/mermaid-cli for more information.\n\n" +
                error.toString());
        }
    });
}
exports.mermaidToPNG = mermaidToPNG;
//# sourceMappingURL=mermaid.js.map
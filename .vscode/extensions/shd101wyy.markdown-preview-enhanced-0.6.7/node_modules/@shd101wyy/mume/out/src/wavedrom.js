"use strict";
/**
 * A wrapper of wavedrom CLI
 * https://github.com/wavedrom/cli
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
exports.render = void 0;
const utility = require("./utility");
function render(wavedromCode, projectDirectoryPath) {
    return __awaiter(this, void 0, void 0, function* () {
        const info = yield utility.tempOpen({
            prefix: "mume-wavedrom",
            suffix: ".js",
        });
        yield utility.write(info.fd, wavedromCode);
        try {
            const svg = yield utility.execFile("npx", ["wavedrom-cli", "-i", info.path], {
                shell: true,
                cwd: projectDirectoryPath,
            });
            return svg;
        }
        catch (error) {
            throw new Error("wavedrom CLI is required to be installed.\nCheck http://github.com/wavedrom/cli for more information.\n\n" +
                error.toString());
        }
    });
}
exports.render = render;
//# sourceMappingURL=wavedrom.js.map
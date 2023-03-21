"use strict";
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
exports.toSVG = void 0;
/**
 * Convert vega-lite to vega first, then render to svg.
 */
const YAML = require("yamljs");
const utility = require("./utility");
const vega = require("./vega");
let vl = null;
function toSVG(spec = "", baseURL = "") {
    return __awaiter(this, void 0, void 0, function* () {
        if (!vl) {
            vl = utility.loadDependency("vega-lite/vega-lite.min.js");
        }
        spec = spec.trim();
        let d;
        if (spec[0] !== "{") {
            d = YAML.parse(spec);
        }
        else {
            // json
            d = JSON.parse(spec);
        }
        return utility.allowUnsafeEval(() => {
            return utility.allowUnsafeNewFunction(() => {
                return vega.toSVG(JSON.stringify(vl.compile(d).spec), baseURL);
            });
        });
    });
}
exports.toSVG = toSVG;
//# sourceMappingURL=vega-lite.js.map
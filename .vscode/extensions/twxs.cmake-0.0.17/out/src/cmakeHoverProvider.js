"use strict";
const vscode = require("vscode");
const cmake = require("./cmake");
class CMakeExtraInfoSupport {
    provideHover(document, position, token) {
        let range = document.getWordRangeAtPosition(position);
        let value = document.getText(range);
        let promises = cmake.cmake_help_all();
        return Promise.all([
            cmake.cmCommandsSuggestionsExact(value),
            cmake.cmVariablesSuggestionsExact(value),
            cmake.cmModulesSuggestionsExact(value),
            cmake.cmPropertiesSuggestionsExact(value),
        ]).then(function (results) {
            const suggestions = Array.prototype.concat.apply([], results);
            if (suggestions.length === 0) {
                return null;
            }
            let suggestion = suggestions[0];
            return promises[cmake.cmakeTypeFromvscodeKind(suggestion.kind)](suggestion.label).then(function (result) {
                let lines = result.split("\n");
                lines = lines.slice(2, Math.min(20, lines.length));
                const hover = new vscode.Hover({ language: "md", value: lines.join("\n") });
                return hover;
            });
        });
    }
}
exports.CMakeExtraInfoSupport = CMakeExtraInfoSupport;
//# sourceMappingURL=cmakeHoverProvider.js.map
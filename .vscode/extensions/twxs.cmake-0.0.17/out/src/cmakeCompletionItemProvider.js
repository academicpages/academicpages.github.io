"use strict";
const cmake = require("./cmake");
class CMakeCompletionItemProvider {
    constructor() {
        this.excludeTokens = ["string", "comment", "numeric"];
    }
    provideCompletionItems(document, position, token) {
        let wordAtPosition = document.getWordRangeAtPosition(position);
        let currentWord = "";
        if (wordAtPosition && wordAtPosition.start.character < position.character) {
            const word = document.getText(wordAtPosition);
            currentWord = word.substr(0, position.character - wordAtPosition.start.character);
        }
        return new Promise(function (resolve, reject) {
            Promise.all([
                cmake.cmCommandsSuggestions(currentWord),
                cmake.cmVariablesSuggestions(currentWord),
                cmake.cmPropertiesSuggestions(currentWord),
                cmake.cmModulesSuggestions(currentWord)
            ]).then(function (results) {
                const suggestions = Array.prototype.concat.apply([], results);
                resolve(suggestions);
            }).catch(err => { reject(err); });
        });
    }
    resolveCompletionItem(item, token) {
        let promises = cmake.cmake_help_all();
        let type = cmake.cmakeTypeFromvscodeKind(item.kind);
        return promises[type](item.label).then(function (result) {
            item.documentation = result.split("\n")[3];
            return item;
        });
    }
}
exports.CMakeCompletionItemProvider = CMakeCompletionItemProvider;
//# sourceMappingURL=cmakeCompletionItemProvider.js.map
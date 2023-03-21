"use strict";
const vscode = require("vscode");
const cmakeHoverProvider_1 = require("./cmakeHoverProvider");
const cmakeCompletionItemProvider_1 = require("./cmakeCompletionItemProvider");
const cmakeDocumentFormattingEditProvider_1 = require("./cmakeDocumentFormattingEditProvider");
const cmakeDefinitionProvider_1 = require("./cmakeDefinitionProvider");
const cmakeRenameProvider_1 = require("./cmakeRenameProvider");
const cmakeReferenceProvider_1 = require("./cmakeReferenceProvider");
const cmakeCMakeCodeLensProvider_1 = require("./cmakeCMakeCodeLensProvider");
function activate(context) {
    const CMAKE_MODE = { language: "cmake", scheme: "file" };
    context.subscriptions.push(vscode.languages.registerHoverProvider(CMAKE_MODE, new cmakeHoverProvider_1.CMakeExtraInfoSupport()));
    context.subscriptions.push(vscode.languages.registerCompletionItemProvider("cmake", new cmakeCompletionItemProvider_1.CMakeCompletionItemProvider()));
    context.subscriptions.push(vscode.languages.registerDefinitionProvider(CMAKE_MODE, new cmakeDefinitionProvider_1.CMakeDefinitionProvider()));
    let cmakeConfig = vscode.workspace.getConfiguration("cmake");
    if (cmakeConfig.get("experimental.enableFormattingEditProvider", false))
        context.subscriptions.push(vscode.languages.registerDocumentFormattingEditProvider(CMAKE_MODE, new cmakeDocumentFormattingEditProvider_1.CMakeDocumentFormattingEditProvider()));
    if (cmakeConfig.get("experimental.enableRenameProvider", false))
        context.subscriptions.push(vscode.languages.registerRenameProvider(CMAKE_MODE, new cmakeRenameProvider_1.CMakeRenameProvider()));
    if (cmakeConfig.get("experimental.enableReferenceProvider", false))
        context.subscriptions.push(vscode.languages.registerReferenceProvider(CMAKE_MODE, new cmakeReferenceProvider_1.CMakeReferenceProvider()));
    if (cmakeConfig.get("experimental.enableCodeLensProvider", false))
        context.subscriptions.push(vscode.languages.registerCodeLensProvider(CMAKE_MODE, new cmakeCMakeCodeLensProvider_1.CMakeCodeLensProvider()));
    vscode.languages.setLanguageConfiguration(CMAKE_MODE.language, {
        indentationRules: {
            // ^(.*\*/)?\s*\}.*$
            decreaseIndentPattern: /^(.*\*\/)?\s*\}.*$/,
            // ^.*\{[^}""]*$
            increaseIndentPattern: /^.*\{[^}""]*$/
        },
        wordPattern: /(-?\d*\.\d\w*)|([^\`\~\!\@\#\%\^\&\*\(\)\-\=\+\[\{\]\}\\\|\;\:\"\"\,\.\<\>\/\?\s]+)/g,
        comments: {
            lineComment: "#",
            blockComment: ["#[[", "]]"],
        },
        brackets: [
            ["{", "}"],
            ["(", ")"],
        ],
        __electricCharacterSupport: {
            brackets: [
                { tokenType: "delimiter.curly.ts", open: "{", close: "}", isElectric: true },
                { tokenType: "delimiter.square.ts", open: "[", close: "]", isElectric: true },
                { tokenType: "delimiter.paren.ts", open: "(", close: ")", isElectric: true }
            ]
        },
        __characterPairSupport: {
            autoClosingPairs: [
                { open: "{", close: "}" },
                { open: "(", close: ")" },
                { open: "\"", close: "\"", notIn: ["string"] },
            ]
        }
    });
    // const cmake = new cmake_mod.CMakeTools();
    // function register(name, fn) {
    //     fn = fn.bind(cmake);
    //     return vscode.commands.registerCommand(name, _ => fn());
    // }
    // for (const key of [
    //     "configure",
    //     "build",
    //     "cleanConfigure",
    //     "jumpToCacheFile",
    //     "clean",
    //     "cleanRebuild",
    //     "buildWithTarget",
    //     "setDefaultTarget",
    //     "setBuildType",
    //     "ctest",
    //     "quickStart",
    //     "stop",
    // ]) {
    //     context.subscriptions.push(register("cmake." + key, cmake[key]));
    // }
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() {
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map
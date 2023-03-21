"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator.throw(value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments)).next());
    });
};
const proc = require("child_process");
const vscode = require("vscode");
function cmake(args) {
    return __awaiter(this, void 0, Promise, function* () {
        return new Promise(function (resolve, reject) {
            let cmd = proc.spawn("cmake", args.map(arg => { return arg.replace(/\r/gm, ""); }));
            let stdout = "";
            cmd.stdout.on("data", function (data) {
                const txt = data.toString("utf8");
                stdout += txt.replace(/\r/gm, "");
            });
            cmd.on("error", function (error) {
                reject();
            });
            cmd.on("exit", function (code) {
                resolve(stdout);
            });
        });
    });
}
exports.cmake = cmake;
function cmake_help_list(kind) {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake(["--help-" + kind + "-list"]);
    });
}
exports.cmake_help_list = cmake_help_list;
function cmake_help_command_list() {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help_list("command");
    });
}
exports.cmake_help_command_list = cmake_help_command_list;
function cmake_help_variable_list() {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help_list("variable");
    });
}
exports.cmake_help_variable_list = cmake_help_variable_list;
function cmake_help_property_list() {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help_list("property");
    });
}
exports.cmake_help_property_list = cmake_help_property_list;
function cmake_help_module_list() {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help_list("module");
    });
}
exports.cmake_help_module_list = cmake_help_module_list;
function cmake_help(kind, name) {
    return __awaiter(this, void 0, Promise, function* () {
        try {
            const result = yield cmake_help_list(kind);
            if (result.indexOf(name) > -1) {
                return yield cmake(["--help-" + kind, name]);
            }
            else {
                throw ("not found");
            }
        }
        catch (e) {
            throw ("not found");
        }
    });
}
exports.cmake_help = cmake_help;
function cmake_help_command(name) {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help("command", name);
    });
}
exports.cmake_help_command = cmake_help_command;
function cmake_help_variable(name) {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help("variable", name);
    });
}
exports.cmake_help_variable = cmake_help_variable;
function cmake_help_module(name) {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help("module", name);
    });
}
exports.cmake_help_module = cmake_help_module;
function cmake_help_property(name) {
    return __awaiter(this, void 0, Promise, function* () {
        return yield cmake_help("property", name);
    });
}
exports.cmake_help_property = cmake_help_property;
function cmake_help_all() {
    let promises = {
        "function": (name) => {
            return this.cmake_help_command(name);
        },
        "module": (name) => {
            return this.cmake_help_module(name);
        },
        "variable": (name) => {
            return this.cmake_help_variable(name);
        },
        "property": (name) => {
            return this.cmake_help_property(name);
        }
    };
    return promises;
}
exports.cmake_help_all = cmake_help_all;
function _extractVersion(output) {
    let re = /cmake\s+version\s+(\d+.\d+.\d+)/;
    if (re.test(output)) {
        let result = re.exec(output);
        return result[1];
    }
    return "";
}
function cmake_version() {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd_output = yield this.cmake(["--version"]);
        let version = this._extractVersion(cmd_output);
        return version;
    });
}
exports.cmake_version = cmake_version;
function vscodeKindFromCMakeCodeClass(kind) {
    switch (kind) {
        case "function":
            return vscode.CompletionItemKind.Function;
        case "variable":
            return vscode.CompletionItemKind.Variable;
        case "module":
            return vscode.CompletionItemKind.Module;
    }
    return vscode.CompletionItemKind.Property; // TODO@EG additional mappings needed?
}
exports.vscodeKindFromCMakeCodeClass = vscodeKindFromCMakeCodeClass;
function cmakeTypeFromvscodeKind(kind) {
    switch (kind) {
        case vscode.CompletionItemKind.Function:
            return "function";
        case vscode.CompletionItemKind.Variable:
            return "variable";
        case vscode.CompletionItemKind.Module:
            return "module";
    }
    return "property";
}
exports.cmakeTypeFromvscodeKind = cmakeTypeFromvscodeKind;
function suggestionsHelper(cmake_cmd, currentWord, type, insertText, matchPredicate) {
    return __awaiter(this, void 0, Promise, function* () {
        const stdout = yield cmake_cmd;
        let suggestions = [];
        let commands = stdout.split("\n").filter(function (v) { return matchPredicate(v, currentWord); });
        if (commands.length > 0) {
            suggestions = commands.map(function (command_name) {
                const item = new vscode.CompletionItem(command_name);
                item.kind = vscodeKindFromCMakeCodeClass(type);
                if (insertText == null || insertText === "") {
                    item.insertText = command_name;
                }
                else {
                    item.insertText = insertText(command_name);
                }
                return item;
            });
        }
        return suggestions;
    });
}
exports.suggestionsHelper = suggestionsHelper;
/// strings Helpers
function strContains(word, pattern) {
    return word.indexOf(pattern) > -1;
}
function strEquals(word, pattern) {
    return word === pattern;
}
function cmModuleInsertText(module) {
    if (module.indexOf("Find") === 0) {
        return "find_package(" + module.replace("Find", "") + "{{ REQUIRED}})";
    }
    else {
        return "include(" + module + ")";
    }
}
function cmFunctionInsertText(func) {
    let scoped_func = ["if", "function", "while", "macro", "foreach"];
    let is_scoped = scoped_func.reduceRight(function (prev, name, idx, array) { return prev || func === name; }, false);
    if (is_scoped)
        return func + "({{}})\n  \nend" + func + "()\n";
    else
        return func + "({{}})";
}
function cmVariableInsertText(variable) {
    return variable.replace(/<(.*)>/g, "{{$1}}");
}
function cmPropetryInsertText(variable) {
    return variable.replace(/<(.*)>/g, "{{$1}}");
}
function cmCommandsSuggestions(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_command_list();
        return suggestionsHelper(cmd, currentWord, "function", cmFunctionInsertText, strContains);
    });
}
exports.cmCommandsSuggestions = cmCommandsSuggestions;
function cmVariablesSuggestions(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_variable_list();
        return suggestionsHelper(cmd, currentWord, "variable", cmVariableInsertText, strContains);
    });
}
exports.cmVariablesSuggestions = cmVariablesSuggestions;
function cmPropertiesSuggestions(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_property_list();
        return suggestionsHelper(cmd, currentWord, "property", cmPropetryInsertText, strContains);
    });
}
exports.cmPropertiesSuggestions = cmPropertiesSuggestions;
function cmModulesSuggestions(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_module_list();
        return suggestionsHelper(cmd, currentWord, "module", cmModuleInsertText, strContains);
    });
}
exports.cmModulesSuggestions = cmModulesSuggestions;
function cmCommandsSuggestionsExact(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_command_list();
        return suggestionsHelper(cmd, currentWord, "function", cmFunctionInsertText, strEquals);
    });
}
exports.cmCommandsSuggestionsExact = cmCommandsSuggestionsExact;
function cmVariablesSuggestionsExact(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_variable_list();
        return suggestionsHelper(cmd, currentWord, "variable", cmVariableInsertText, strEquals);
    });
}
exports.cmVariablesSuggestionsExact = cmVariablesSuggestionsExact;
function cmPropertiesSuggestionsExact(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_property_list();
        return suggestionsHelper(cmd, currentWord, "property", cmPropetryInsertText, strEquals);
    });
}
exports.cmPropertiesSuggestionsExact = cmPropertiesSuggestionsExact;
function cmModulesSuggestionsExact(currentWord) {
    return __awaiter(this, void 0, Promise, function* () {
        let cmd = cmake_help_module_list();
        return suggestionsHelper(cmd, currentWord, "module", cmModuleInsertText, strEquals);
    });
}
exports.cmModulesSuggestionsExact = cmModulesSuggestionsExact;
//# sourceMappingURL=cmake.js.map
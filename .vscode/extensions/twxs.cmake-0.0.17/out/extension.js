"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode_1 = require("vscode");
const child_process = require("child_process");
/// strings Helpers
function strContains(word, pattern) {
    return word.indexOf(pattern) > -1;
}
function strEquals(word, pattern) {
    return word == pattern;
}
/// configuration helpers
function config(key, defaultValue) {
    const cmake_conf = vscode_1.workspace.getConfiguration('cmake');
    return cmake_conf.get(key, defaultValue);
}
/// Cmake process helpers
// Simple helper function that invoke the CMAKE executable
// and return a promise with stdout
let cmake = (args) => {
    return new Promise(function (resolve, reject) {
        let cmd = child_process.spawn(config('cmakePath', 'cmake'), args.map(arg => { return arg.replace(/\r/gm, ''); }));
        let stdout = '';
        cmd.stdout.on('data', function (data) {
            var txt = data.toString();
            stdout += txt.replace(/\r/gm, '');
        });
        cmd.on("error", function (error) {
            if (error && error.code === 'ENOENT') {
                vscode_1.window.showInformationMessage('The "cmake" command is not found in PATH.  Install it or use `cmake.cmakePath` in the workspace settings to define the CMake executable binary.');
            }
            reject();
        });
        cmd.on('exit', function (code) {
            resolve(stdout);
        });
    });
};
function _extractVersion(output) {
    let re = /cmake\s+version\s+(\d+.\d+.\d+)/;
    if (re.test(output)) {
        let result = re.exec(output);
        return result[1];
    }
    return '';
}
function cmake_version() {
    return __awaiter(this, void 0, void 0, function* () {
        let cmd_output = yield cmake(['--version']);
        let version = _extractVersion(cmd_output);
        return version;
    });
}
// Return the url for the online help based on the cmake executable binary used
function cmake_help_url() {
    return __awaiter(this, void 0, void 0, function* () {
        let base_url = 'https://cmake.org/cmake/help';
        let version = yield cmake_version();
        if (version.length > 0) {
            if (version >= '3.0') {
                let re = /(\d+.\d+).\d+/;
                version = version.replace(re, '$1/');
            }
            else {
                let older_versions = [
                    '2.8.12', '2.8.11', '2.8.10', '2.8.9', '2.8.8', '2.8.7', '2.8.6', '2.8.5', '2.8.4', '2.8.3', '2.8.2', '2.8.1', '2.8.0', '2.6'
                ];
                if (older_versions.indexOf(version) == -1) {
                    version = 'latest/';
                }
                else {
                    version = version + '/cmake.html';
                }
            }
        }
        else {
            version = 'latest/';
        }
        return base_url + '/v' + version;
    });
}
// return the cmake command list
function cmake_help_command_list() {
    return cmake(['--help-command-list']);
}
function cmake_help_command(name) {
    return cmake_help_command_list()
        .then(function (result) {
        let contains = result.indexOf(name) > -1;
        return new Promise(function (resolve, reject) {
            if (contains) {
                resolve(name);
            }
            else {
                reject('not found');
            }
        });
    }, function (e) { })
        .then(function (n) {
        return cmake(['--help-command', n]);
    }, null);
}
function cmake_help_variable_list() {
    return cmake(['--help-variable-list']);
}
function cmake_help_variable(name) {
    return cmake_help_variable_list()
        .then(function (result) {
        let contains = result.indexOf(name) > -1;
        return new Promise(function (resolve, reject) {
            if (contains) {
                resolve(name);
            }
            else {
                reject('not found');
            }
        });
    }, function (e) { }).then(function (name) { return cmake(['--help-variable', name]); }, null);
}
function cmake_help_property_list() {
    return cmake(['--help-property-list']);
}
function cmake_help_property(name) {
    return cmake_help_property_list()
        .then(function (result) {
        let contains = result.indexOf(name) > -1;
        return new Promise(function (resolve, reject) {
            if (contains) {
                resolve(name);
            }
            else {
                reject('not found');
            }
        });
    }, function (e) { }).then(function (name) { return cmake(['--help-property', name]); }, null);
}
function cmake_help_module_list() {
    return cmake(['--help-module-list']);
}
function cmake_help_module(name) {
    return cmake_help_module_list()
        .then(function (result) {
        let contains = result.indexOf(name) > -1;
        return new Promise(function (resolve, reject) {
            if (contains) {
                resolve(name);
            }
            else {
                reject('not found');
            }
        });
    }, function (e) { }).then(function (name) { return cmake(['--help-module', name]); }, null);
}
function cmake_help_all() {
    let promises = {
        'function': (name) => {
            return cmake_help_command(name);
        },
        'module': (name) => {
            return cmake_help_module(name);
        },
        'variable': (name) => {
            return cmake_help_variable(name);
        },
        'property': (name) => {
            return cmake_help_property(name);
        }
    };
    return promises;
}
function cmake_online_help(search) {
    return __awaiter(this, void 0, void 0, function* () {
        let url = yield cmake_help_url();
        let v2x = url.endsWith('html'); // cmake < 3.0 
        return Promise.all([
            cmCommandsSuggestionsExact(search),
            cmVariablesSuggestionsExact(search),
            cmModulesSuggestionsExact(search),
            cmPropertiesSuggestionsExact(search),
        ]).then(function (results) {
            var opener = require("opener");
            var suggestions = Array.prototype.concat.apply([], results);
            if (suggestions.length == 0) {
                search = search.replace(/[<>]/g, '');
                if (v2x || search.length == 0) {
                    opener(url);
                }
                else {
                    opener(url + 'search.html?q=' + search + '&check_keywords=yes&area=default');
                }
            }
            else {
                let suggestion = suggestions[0];
                let type = cmakeTypeFromvscodeKind(suggestion.kind);
                if (type == 'property') {
                    if (v2x) {
                        opener(url);
                    }
                    else {
                        // TODO : needs to filter properties per scope to detect the right URL
                        opener(url + 'search.html?q=' + search + '&check_keywords=yes&area=default');
                    }
                }
                else {
                    if (type == 'function') {
                        type = 'command';
                    }
                    search = search.replace(/[<>]/g, '');
                    if (v2x) {
                        opener(url + '#' + type + ':' + search);
                    }
                    else {
                        opener(url + type + '/' + search + '.html');
                    }
                }
            }
        });
    });
}
// this method is called when your extension is activated. activation is
// controlled by the activation events defined in package.json
function activate(disposables) {
    vscode_1.commands.registerCommand('cmake.onlineHelp', () => {
        // The code you place here will be executed every time your command is executed
        // Display a message box to the user
        var editor = vscode_1.window.activeTextEditor;
        if (!editor) {
            return; // No open text editor
        }
        var selection = editor.selection;
        let document = editor.document;
        let position = selection.start;
        var currentWord = document.getText(selection);
        let wordAtPosition = document.getWordRangeAtPosition(position);
        var currentWord = '';
        if (wordAtPosition && wordAtPosition.start.character < position.character) {
            var word = document.getText(wordAtPosition);
            currentWord = word;
        }
        vscode_1.window.showInputBox({ prompt: 'Search on Cmake online documentation', placeHolder: currentWord }).then(function (result) {
            if (typeof result != 'undefined') {
                if (result.length === 0) {
                    result = currentWord;
                }
                if (result != "") {
                    cmake_online_help(result);
                }
            }
        });
    });
    const CMAKE_MODE = { language: 'cmake', scheme: 'file' };
    vscode_1.languages.registerHoverProvider('cmake', new CMakeExtraInfoSupport());
    vscode_1.languages.registerCompletionItemProvider('cmake', new CMakeSuggestionSupport());
    vscode_1.languages.setLanguageConfiguration(CMAKE_MODE.language, {
        indentationRules: {
            // ^(.*\*/)?\s*\}.*$
            decreaseIndentPattern: /^(.*\*\/)?\s*\}.*$/,
            // ^.*\{[^}"']*$
            increaseIndentPattern: /^.*\{[^}"']*$/
        },
        wordPattern: /(-?\d*\.\d\w*)|([^\`\~\!\@\#\%\^\&\*\(\)\-\=\+\[\{\]\}\\\|\;\:\'\"\,\.\<\>\/\?\s]+)/g,
        comments: {
            lineComment: '#'
        },
        brackets: [
            ['{', '}'],
            ['(', ')'],
        ],
        __electricCharacterSupport: {
            brackets: [
                { tokenType: 'delimiter.curly.ts', open: '{', close: '}', isElectric: true },
                { tokenType: 'delimiter.square.ts', open: '[', close: ']', isElectric: true },
                { tokenType: 'delimiter.paren.ts', open: '(', close: ')', isElectric: true }
            ]
        },
        __characterPairSupport: {
            autoClosingPairs: [
                { open: '{', close: '}' },
                { open: '(', close: ')' },
                { open: '"', close: '"', notIn: ['string'] },
            ]
        }
    });
}
exports.activate = activate;
// Show Tooltip on mouse over
class CMakeExtraInfoSupport {
    provideHover(document, position, token) {
        let range = document.getWordRangeAtPosition(position);
        let value = document.getText(range);
        let promises = cmake_help_all();
        return Promise.all([
            cmCommandsSuggestionsExact(value),
            cmVariablesSuggestionsExact(value),
            cmModulesSuggestionsExact(value),
            cmPropertiesSuggestionsExact(value),
        ]).then(function (results) {
            var suggestions = Array.prototype.concat.apply([], results);
            if (suggestions.length == 0) {
                return null;
            }
            let suggestion = suggestions[0];
            return promises[cmakeTypeFromvscodeKind(suggestion.kind)](suggestion.label).then(function (result) {
                let lines = result.split('\n');
                lines = lines.slice(2, Math.min(20, lines.length));
                let hover = new vscode_1.Hover({ language: 'md', value: lines.join('\n') });
                return hover;
            });
        });
    }
}
function vscodeKindFromCMakeCodeClass(kind) {
    switch (kind) {
        case "function":
            return vscode_1.CompletionItemKind.Function;
        case "variable":
            return vscode_1.CompletionItemKind.Variable;
        case "module":
            return vscode_1.CompletionItemKind.Module;
    }
    return vscode_1.CompletionItemKind.Property; // TODO@EG additional mappings needed?
}
function cmakeTypeFromvscodeKind(kind) {
    switch (kind) {
        case vscode_1.CompletionItemKind.Function:
            return "function";
        case vscode_1.CompletionItemKind.Variable:
            return "variable";
        case vscode_1.CompletionItemKind.Module:
            return "module";
    }
    return "property";
}
function suggestionsHelper(cmake_cmd, currentWord, type, insertText, matchPredicate) {
    return new Promise(function (resolve, reject) {
        cmake_cmd.then(function (stdout) {
            let commands = stdout.split('\n').filter(function (v) { return matchPredicate(v, currentWord); });
            if (commands.length > 0) {
                let suggestions = commands.map(function (command_name) {
                    var item = new vscode_1.CompletionItem(command_name);
                    item.kind = vscodeKindFromCMakeCodeClass(type);
                    if (insertText == null || insertText == '') {
                        item.insertText = command_name;
                    }
                    else {
                        let snippet = new vscode_1.SnippetString(insertText(command_name));
                        item.insertText = snippet;
                    }
                    return item;
                });
                resolve(suggestions);
            }
            else {
                resolve([]);
            }
        }).catch(function (err) {
            reject(err);
        });
    });
}
function cmModuleInsertText(module) {
    if (module.indexOf('Find') == 0) {
        return 'find_package(' + module.replace('Find', '') + '${1: REQUIRED})';
    }
    else {
        return 'include(' + module + ')';
    }
}
function cmFunctionInsertText(func) {
    let scoped_func = ['if', 'function', 'while', 'macro', 'foreach'];
    let is_scoped = scoped_func.reduceRight(function (prev, name, idx, array) { return prev || func == name; }, false);
    if (is_scoped)
        return func + '(${1})\n\t\nend' + func + '(${1})\n';
    else
        return func + '(${1})';
}
function cmVariableInsertText(variable) {
    return variable.replace(/<(.*)>/g, '${1:<$1>}');
}
function cmPropetryInsertText(variable) {
    return variable.replace(/<(.*)>/g, '${1:<$1>}');
}
function cmCommandsSuggestions(currentWord) {
    let cmd = cmake_help_command_list();
    return suggestionsHelper(cmd, currentWord, 'function', cmFunctionInsertText, strContains);
}
function cmVariablesSuggestions(currentWord) {
    let cmd = cmake_help_variable_list();
    return suggestionsHelper(cmd, currentWord, 'variable', cmVariableInsertText, strContains);
}
function cmPropertiesSuggestions(currentWord) {
    let cmd = cmake_help_property_list();
    return suggestionsHelper(cmd, currentWord, 'property', cmPropetryInsertText, strContains);
}
function cmModulesSuggestions(currentWord) {
    let cmd = cmake_help_module_list();
    return suggestionsHelper(cmd, currentWord, 'module', cmModuleInsertText, strContains);
}
function cmCommandsSuggestionsExact(currentWord) {
    let cmd = cmake_help_command_list();
    return suggestionsHelper(cmd, currentWord, 'function', cmFunctionInsertText, strEquals);
}
function cmVariablesSuggestionsExact(currentWord) {
    let cmd = cmake_help_variable_list();
    return suggestionsHelper(cmd, currentWord, 'variable', cmVariableInsertText, strEquals);
}
function cmPropertiesSuggestionsExact(currentWord) {
    let cmd = cmake_help_property_list();
    return suggestionsHelper(cmd, currentWord, 'property', cmPropetryInsertText, strEquals);
}
function cmModulesSuggestionsExact(currentWord) {
    let cmd = cmake_help_module_list();
    return suggestionsHelper(cmd, currentWord, 'module', cmModuleInsertText, strEquals);
}
class CMakeSuggestionSupport {
    constructor() {
        this.excludeTokens = ['string', 'comment', 'numeric'];
    }
    provideCompletionItems(document, position, token) {
        let wordAtPosition = document.getWordRangeAtPosition(position);
        var currentWord = '';
        if (wordAtPosition && wordAtPosition.start.character < position.character) {
            var word = document.getText(wordAtPosition);
            currentWord = word.substr(0, position.character - wordAtPosition.start.character);
        }
        return new Promise(function (resolve, reject) {
            Promise.all([
                cmCommandsSuggestions(currentWord),
                cmVariablesSuggestions(currentWord),
                cmPropertiesSuggestions(currentWord),
                cmModulesSuggestions(currentWord)
            ]).then(function (results) {
                var suggestions = Array.prototype.concat.apply([], results);
                resolve(suggestions);
            }).catch(err => { reject(err); });
        });
    }
    resolveCompletionItem(item, token) {
        let promises = cmake_help_all();
        let type = cmakeTypeFromvscodeKind(item.kind);
        return promises[type](item.label).then(function (result) {
            item.documentation = result.split('\n')[3];
            return item;
        });
    }
}
// CMake Language Definition
// class CMakeLanguageDef  /*implements LanguageConfiguration*/ {
//         public comments = {
// 			lineComment: '#',
// 		}
//         public name:string = 'cmake';
//         public displayName:string= 'Cmake';
//         public ignoreCase: boolean = true;
//         public lineComment: string = '#';
//         public autoClosingPairs:string[][] = [
//             ['{', '}'],
//             ['"', '"']];
//        public keywords :string[] = [
//            'if', 'endif', 'else',
//            'foreach', 'endforeach',
//            'function', 'endfunction',
//            'macro', 'endmacro',
//            'include',
//            'set',
//            'project'
//        ];
//         public brackets = [
//             { token: 'delimiter.parenthesis', open: '(', close: ')' },
//         ];
//         public textAfterBrackets:boolean = true;
//         public variable= /\$\{\w+\}/;
//        public  enhancedBrackets = [           
//             {
//                 openTrigger: '\)',
//                 open: /if\((\w*)\)/i,
//                 closeComplete: 'endif\($1\)',
//                 matchCase: true,
//                 closeTrigger: '\)',
//                 close: /endif\($1\)$/,
//                 tokenType: 'keyword.tag-if'
//             },
//             {
//                 openTrigger: '\)',
//                 open: /foreach\((\w*)\)/i,
//                 closeComplete: 'endforeach\($1\)',
//                 matchCase: true,
//                 closeTrigger: '\)',
//                 close: /endforeach\($1\)$/,
//                 tokenType: 'keyword.tag-foreach'
//             },
//             {
//                 openTrigger: '\)',
//                 open: /function\((\w+)\)/i,
//                 closeComplete: 'endfunction\($1\)',
//                 matchCase: true,
//                 closeTrigger: '\)',
//                 close: /function\($1\)$/,
//                 tokenType: 'keyword.tag-function'
//             },
//             {
//                 openTrigger: '\)',
//                 open: /macro\((\w+)\)/i,
//                 closeComplete: 'endmacro\($1\)',
//                 matchCase: true,
//                 closeTrigger: '\)',
//                 close: /macro\($1\)$/,
//                 tokenType: 'keyword.tag-macro'
//             }
//         ];
//         // we include these common regular expressions
//         public symbols = /[=><!~?&|+\-*\/\^;\.,]+/;
//         public escapes= /\\(?:[abfnrtv\\"']|x[0-9A-Fa-f]{1,4}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})/;
//         // The main tokenizer for our languages
//         public tokenizer= {
//             root: [
//                 [/([a-zA-Z_]\w*)( *\()/,  [{cases: { '@keywords': { token: 'keyword.$0' } , '@default': 'identifier.method'}}, '']],
//                 { include: '@whitespace' },
//                 [/\$\{\w+\}/, 'variable'],
//                 [/\d*\.\d+([eE][\-+]?\d+)?/, 'number.float'],
//                 [/0[xX][0-9a-fA-F_]*[0-9a-fA-F]/, 'number.hex'],
//                 [/\d+/, 'number'],
//                 [/"/, 'string', '@string."'],
//                 [/'/, 'string', '@string.\''],
//             ],
//             whitespace: [
//                 [/[ \t\r\n]+/, ''],
//                 [/#.*$/, 'comment'],
//             ],
//             string: [
//                 [/[^\\"'%]+/, { cases: { '@eos': { token: 'string', next: '@popall' }, '@default': 'string' } }],
//                 [/@escapes/, 'string.escape'],
//                 [/\\./, 'string.escape.invalid'],
//                 [/\$\{[\w ]+\}/, 'variable'],
//                 [/["']/, { cases: { '$#==$S2': { token: 'string', next: '@pop' }, '@default': 'string' } }],
//                 [/$/, 'string', '@popall']
//             ],
//         };
//     }
//# sourceMappingURL=extension.js.map
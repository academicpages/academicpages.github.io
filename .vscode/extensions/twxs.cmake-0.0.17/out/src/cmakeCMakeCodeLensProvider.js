"use strict";
const vscode = require("vscode");
let pegCMake = require("peg-cmake");
function traversAST(ast, matcher) {
    ast.forEach((element) => {
        if (matcher[element.type])
            matcher[element.type](element);
    });
}
function locationToRange(location) {
    return new vscode.Range(new vscode.Position(location.start.line - 1, location.start.column - 1), new vscode.Position(location.end.line - 1, location.end.column - 1));
}
class CMakeCodeLensProvider {
    provideCodeLenses(document, token) {
        try {
            const txt = document.getText();
            const ast = pegCMake.parse(txt);
            function Visitor() {
                this.definitions = {};
                this._func = (elt) => {
                    this.definitions[elt.identifier.value] = { declaration: elt, references: [] };
                };
                this.macro = this._func;
                this.function = this._func;
                this.command_invocation = (elt) => {
                    if (this.definitions[elt.identifier.value])
                        this.definitions[elt.identifier.value].references.push(elt);
                };
                this.if = (elt) => {
                    traversAST(elt.body, this);
                    if (elt.elseif)
                        elt.elseif.forEach((e) => { traversAST(elt.body, this); });
                    if (elt.else)
                        traversAST(elt.else.body, this);
                };
            }
            ;
            let matcher = new Visitor();
            ast.forEach((element) => {
                if (matcher[element.type])
                    matcher[element.type](element);
            });
            if (matcher.definitions) {
                let lenses = [];
                for (let p in matcher.definitions) {
                    let e = matcher.definitions[p];
                    const len = e.references.length;
                    lenses.push(new vscode.CodeLens(locationToRange(e.declaration.location), {
                        title: len === 1 ? "1 reference" : `${len} references`,
                        command: "editor.action.showReferences",
                        arguments: [document.uri, locationToRange(e.declaration.location).start,
                            e.references.map((r => { return new vscode.Location(document.uri, locationToRange(r.location)); }))
                        ]
                    }));
                }
                return lenses;
            }
        }
        catch (e) {
            console.log("error parsing AST");
        }
        let lenses = [];
        return lenses;
    }
}
exports.CMakeCodeLensProvider = CMakeCodeLensProvider;
//# sourceMappingURL=cmakeCMakeCodeLensProvider.js.map
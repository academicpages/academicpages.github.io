"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.getBottomVisibleLine = exports.getTopVisibleLine = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const mume_1 = require("@shd101wyy/mume");
const fs = require("fs");
const path = require("path");
const vscode = require("vscode");
const image_helper_1 = require("./image-helper");
const preview_content_provider_1 = require("./preview-content-provider");
let editorScrollDelay = Date.now();
// hide default vscode markdown preview buttons if necessary
const hideDefaultVSCodeMarkdownPreviewButtons = vscode.workspace
    .getConfiguration("markdown-preview-enhanced")
    .get("hideDefaultVSCodeMarkdownPreviewButtons");
if (hideDefaultVSCodeMarkdownPreviewButtons) {
    vscode.commands.executeCommand("setContext", "hasCustomMarkdownPreview", true);
}
// this method is called when your extension iopenTextDocuments activated
// your extension is activated the very first time the command is executed
function activate(context) {
    // assume only one preview supported.
    const contentProvider = new preview_content_provider_1.MarkdownPreviewEnhancedView(context);
    function openPreviewToTheSide(uri) {
        let resource = uri;
        if (!(resource instanceof vscode.Uri)) {
            if (vscode.window.activeTextEditor) {
                // we are relaxed and don't check for markdown files
                resource = vscode.window.activeTextEditor.document.uri;
            }
        }
        contentProvider.initPreview(resource, vscode.window.activeTextEditor, {
            viewColumn: vscode.ViewColumn.Two,
            preserveFocus: true,
        });
    }
    function openPreview(uri) {
        let resource = uri;
        if (!(resource instanceof vscode.Uri)) {
            if (vscode.window.activeTextEditor) {
                // we are relaxed and don't check for markdown files
                resource = vscode.window.activeTextEditor.document.uri;
            }
        }
        contentProvider.initPreview(resource, vscode.window.activeTextEditor, {
            viewColumn: vscode.ViewColumn.One,
            preserveFocus: false,
        });
    }
    function toggleScrollSync() {
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        const scrollSync = !config.get("scrollSync");
        config.update("scrollSync", scrollSync, true).then(() => {
            contentProvider.updateConfiguration();
            if (scrollSync) {
                vscode.window.showInformationMessage("Scroll Sync is enabled");
            }
            else {
                vscode.window.showInformationMessage("Scroll Sync is disabled");
            }
        });
    }
    function toggleLiveUpdate() {
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        const liveUpdate = !config.get("liveUpdate");
        config.update("liveUpdate", liveUpdate, true).then(() => {
            contentProvider.updateConfiguration();
            if (liveUpdate) {
                vscode.window.showInformationMessage("Live Update is enabled");
            }
            else {
                vscode.window.showInformationMessage("Live Update is disabled");
            }
        });
    }
    function toggleBreakOnSingleNewLine() {
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        const breakOnSingleNewLine = !config.get("breakOnSingleNewLine");
        config
            .update("breakOnSingleNewLine", breakOnSingleNewLine, true)
            .then(() => {
            contentProvider.updateConfiguration();
            if (breakOnSingleNewLine) {
                vscode.window.showInformationMessage("Break On Single New Line is enabled");
            }
            else {
                vscode.window.showInformationMessage("Break On Single New Line is disabled");
            }
        });
    }
    function customizeCSS() {
        const globalStyleLessFile = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./style.less"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(globalStyleLessFile));
    }
    function openMermaidConfig() {
        const mermaidConfigFilePath = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./mermaid_config.js"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(mermaidConfigFilePath));
    }
    function openMathJaxConfig() {
        const mathjaxConfigFilePath = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./mathjax_config.js"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(mathjaxConfigFilePath));
    }
    function openKaTeXConfig() {
        const katexConfigFilePath = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./katex_config.js"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(katexConfigFilePath));
    }
    function extendParser() {
        const parserConfigPath = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./parser.js"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(parserConfigPath));
    }
    function showUploadedImages() {
        const imageHistoryFilePath = mume_1.utility.addFileProtocol(path.resolve((0, mume_1.getExtensionConfigPath)(), "./image_history.md"));
        vscode.commands.executeCommand("vscode.open", vscode.Uri.parse(imageHistoryFilePath));
    }
    function insertNewSlide() {
        const editor = vscode.window.activeTextEditor;
        if (editor && editor.document && editor.edit) {
            editor.edit((textEdit) => {
                textEdit.insert(editor.selection.active, "<!-- slide -->\n");
            });
        }
    }
    function insertPagebreak() {
        const editor = vscode.window.activeTextEditor;
        if (editor && editor.document && editor.edit) {
            editor.edit((textEdit) => {
                textEdit.insert(editor.selection.active, "<!-- pagebreak -->\n");
            });
        }
    }
    function createTOC() {
        const editor = vscode.window.activeTextEditor;
        if (editor && editor.document && editor.edit) {
            editor.edit((textEdit) => {
                textEdit.insert(editor.selection.active, '\n<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->\n');
            });
        }
    }
    function insertTable() {
        const editor = vscode.window.activeTextEditor;
        if (editor && editor.document && editor.edit) {
            editor.edit((textEdit) => {
                textEdit.insert(editor.selection.active, `|   |   |
|---|---|
|   |   |
`);
            });
        }
    }
    function openImageHelper() {
        contentProvider.openImageHelper(vscode.window.activeTextEditor.document.uri);
    }
    function webviewFinishLoading(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.updateMarkdown(sourceUri);
    }
    /**
     * Insert imageUrl to markdown file
     * @param uri: markdown source uri
     * @param imageUrl: url of image to be inserted
     */
    function insertImageUrl(uri, imageUrl) {
        const sourceUri = vscode.Uri.parse(uri);
        vscode.window.visibleTextEditors
            .filter((editor) => (0, preview_content_provider_1.isMarkdownFile)(editor.document) &&
            editor.document.uri.fsPath === sourceUri.fsPath)
            .forEach((editor) => {
            // const line = editor.selection.active.line
            editor.edit((textEditorEdit) => {
                textEditorEdit.insert(editor.selection.active, `![enter image description here](${imageUrl})`);
            });
        });
    }
    function refreshPreview(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.refreshPreview(sourceUri);
    }
    function openInBrowser(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.openInBrowser(sourceUri);
    }
    function htmlExport(uri, offline) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.htmlExport(sourceUri, offline);
    }
    function chromeExport(uri, type) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.chromeExport(sourceUri, type);
    }
    function princeExport(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.princeExport(sourceUri);
    }
    function eBookExport(uri, fileType) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.eBookExport(sourceUri, fileType);
    }
    function pandocExport(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.pandocExport(sourceUri);
    }
    function markdownExport(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.markdownExport(sourceUri);
    }
    /*
      function cacheSVG(uri, code, svg) {
          const sourceUri = vscode.Uri.parse(uri);
          contentProvider.cacheSVG(sourceUri, code, svg)
      }
      */
    function cacheCodeChunkResult(uri, id, result) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.cacheCodeChunkResult(sourceUri, id, result);
    }
    function runCodeChunk(uri, codeChunkId) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.runCodeChunk(sourceUri, codeChunkId);
    }
    function runAllCodeChunks(uri) {
        const sourceUri = vscode.Uri.parse(uri);
        contentProvider.runAllCodeChunks(sourceUri);
    }
    function runAllCodeChunksCommand() {
        const textEditor = vscode.window.activeTextEditor;
        if (!textEditor.document) {
            return;
        }
        if (!(0, preview_content_provider_1.isMarkdownFile)(textEditor.document)) {
            return;
        }
        const sourceUri = textEditor.document.uri;
        const previewUri = (0, preview_content_provider_1.getPreviewUri)(sourceUri);
        if (!previewUri) {
            return;
        }
        contentProvider.previewPostMessage(sourceUri, {
            command: "runAllCodeChunks",
        });
    }
    function runCodeChunkCommand() {
        const textEditor = vscode.window.activeTextEditor;
        if (!textEditor.document) {
            return;
        }
        if (!(0, preview_content_provider_1.isMarkdownFile)(textEditor.document)) {
            return;
        }
        const sourceUri = textEditor.document.uri;
        const previewUri = (0, preview_content_provider_1.getPreviewUri)(sourceUri);
        if (!previewUri) {
            return;
        }
        contentProvider.previewPostMessage(sourceUri, {
            command: "runCodeChunk",
        });
    }
    function syncPreview() {
        const textEditor = vscode.window.activeTextEditor;
        if (!textEditor.document) {
            return;
        }
        if (!(0, preview_content_provider_1.isMarkdownFile)(textEditor.document)) {
            return;
        }
        const sourceUri = textEditor.document.uri;
        contentProvider.previewPostMessage(sourceUri, {
            command: "changeTextEditorSelection",
            line: textEditor.selections[0].active.line,
            forced: true,
        });
    }
    function clickTagA(uri, href) {
        href = decodeURIComponent(href);
        href = href
            .replace(/^vscode\-resource:\/\//, "")
            .replace(/^vscode\-webview\-resource:\/\/(.+?)\//, "")
            .replace(/^file\/\/\//, "file:///")
            .replace(/^https:\/\/file\+\.vscode-resource.vscode-cdn.net\//, "file:///")
            .replace(/^https?:\/\/(.+?)\.vscode-webview-test.com\/vscode-resource\/file\/+/, "file:///")
            .replace(/^https?:\/\/file(.+?)\.vscode-webview\.net\/+/, "file:///");
        if ([".pdf", ".xls", ".xlsx", ".doc", ".ppt", ".docx", ".pptx"].indexOf(path.extname(href)) >= 0) {
            mume_1.utility.openFile(href);
        }
        else if (href.match(/^file:\/\/\//)) {
            // openFilePath = href.slice(8) # remove protocol
            let openFilePath = mume_1.utility.addFileProtocol(href);
            openFilePath = decodeURI(openFilePath);
            const fileUri = vscode.Uri.parse(openFilePath);
            // determine from link fragment to which line to jump
            let line = -1;
            const found = fileUri.fragment.match(/^L(\d+)/);
            if (found) {
                line = parseInt(found[1], 10);
                if (line > 0) {
                    line = line - 1;
                }
            }
            // find if there is already opened such file
            // and remember in which view column it is
            let col = vscode.ViewColumn.One;
            tgrLoop: for (const tabGroup of vscode.window.tabGroups.all) {
                for (const tab of tabGroup.tabs) {
                    if (tab.input instanceof vscode.TabInputText) {
                        if (tab.input.uri.path === fileUri.path) {
                            col = tabGroup.viewColumn;
                            break tgrLoop;
                        }
                    }
                }
            }
            // open file if needed, if not we will use already opened editor
            // (by specifying view column in which it is already shown)
            if (fs.existsSync(fileUri.fsPath)) {
                vscode.workspace.openTextDocument(fileUri.path).then((doc) => {
                    vscode.window.showTextDocument(doc, col).then((editor) => {
                        // if there was line fragment, jump to line
                        if (line >= 0) {
                            let viewPos = vscode.TextEditorRevealType.InCenter;
                            if (editor.selection.active.line === line) {
                                viewPos = vscode.TextEditorRevealType.InCenterIfOutsideViewport;
                            }
                            const sel = new vscode.Selection(line, 0, line, 0);
                            editor.selection = sel;
                            editor.revealRange(sel, viewPos);
                        }
                    });
                });
            }
            else {
                vscode.commands.executeCommand("vscode.open", fileUri, vscode.ViewColumn.One);
            }
        }
        else {
            mume_1.utility.openFile(href);
        }
    }
    function clickTaskListCheckbox(uri, dataLine) {
        const sourceUri = vscode.Uri.parse(uri);
        const visibleTextEditors = vscode.window.visibleTextEditors;
        for (let i = 0; i < visibleTextEditors.length; i++) {
            const editor = visibleTextEditors[i];
            if (editor.document.uri.fsPath === sourceUri.fsPath) {
                dataLine = parseInt(dataLine, 10);
                editor.edit((edit) => {
                    let line = editor.document.lineAt(dataLine).text;
                    if (line.match(/\[ \]/)) {
                        line = line.replace("[ ]", "[x]");
                    }
                    else {
                        line = line.replace(/\[[xX]\]/, "[ ]");
                    }
                    edit.replace(new vscode.Range(new vscode.Position(dataLine, 0), new vscode.Position(dataLine, line.length)), line);
                });
                break;
            }
        }
    }
    function setPreviewTheme(uri, theme) {
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        config.update("previewTheme", theme, true);
    }
    context.subscriptions.push(vscode.workspace.onDidSaveTextDocument((document) => {
        if ((0, preview_content_provider_1.isMarkdownFile)(document)) {
            contentProvider.updateMarkdown(document.uri, true);
        }
    }));
    context.subscriptions.push(vscode.workspace.onDidChangeTextDocument((event) => {
        if ((0, preview_content_provider_1.isMarkdownFile)(event.document)) {
            contentProvider.update(event.document.uri);
        }
    }));
    context.subscriptions.push(vscode.workspace.onDidChangeConfiguration(() => {
        contentProvider.updateConfiguration();
    }));
    context.subscriptions.push(vscode.window.onDidChangeTextEditorSelection((event) => {
        if ((0, preview_content_provider_1.isMarkdownFile)(event.textEditor.document)) {
            const firstVisibleScreenRow = getTopVisibleLine(event.textEditor);
            const lastVisibleScreenRow = getBottomVisibleLine(event.textEditor);
            const topRatio = (event.selections[0].active.line - firstVisibleScreenRow) /
                (lastVisibleScreenRow - firstVisibleScreenRow);
            contentProvider.previewPostMessage(event.textEditor.document.uri, {
                command: "changeTextEditorSelection",
                line: event.selections[0].active.line,
                topRatio,
            });
        }
    }));
    context.subscriptions.push(vscode.window.onDidChangeTextEditorVisibleRanges((event) => {
        const textEditor = event.textEditor;
        if (Date.now() < editorScrollDelay) {
            return;
        }
        if ((0, preview_content_provider_1.isMarkdownFile)(textEditor.document)) {
            const sourceUri = textEditor.document.uri;
            if (!event.textEditor.visibleRanges.length) {
                return undefined;
            }
            else {
                const topLine = getTopVisibleLine(textEditor);
                const bottomLine = getBottomVisibleLine(textEditor);
                let midLine;
                if (topLine === 0) {
                    midLine = 0;
                }
                else if (Math.floor(bottomLine) ===
                    textEditor.document.lineCount - 1) {
                    midLine = bottomLine;
                }
                else {
                    midLine = Math.floor((topLine + bottomLine) / 2);
                }
                contentProvider.previewPostMessage(sourceUri, {
                    command: "changeTextEditorSelection",
                    line: midLine,
                });
            }
        }
    }));
    /**
     * Open preview automatically if the `automaticallyShowPreviewOfMarkdownBeingEdited` is on.
     * @param textEditor
     */
    context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor((textEditor) => {
        if (textEditor && textEditor.document && textEditor.document.uri) {
            if ((0, preview_content_provider_1.isMarkdownFile)(textEditor.document)) {
                const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
                const sourceUri = textEditor.document.uri;
                const automaticallyShowPreviewOfMarkdownBeingEdited = config.get("automaticallyShowPreviewOfMarkdownBeingEdited");
                const isUsingSinglePreview = config.get("singlePreview");
                /**
                 * Is using single preview and the preview is on.
                 * When we switched text ed()tor, update preview to that text editor.
                 */
                if (contentProvider.isPreviewOn(sourceUri)) {
                    if (isUsingSinglePreview &&
                        !contentProvider.previewHasTheSameSingleSourceUri(sourceUri)) {
                        contentProvider.initPreview(sourceUri, textEditor, {
                            viewColumn: contentProvider.getPreview(sourceUri).viewColumn,
                            preserveFocus: true,
                        });
                    }
                    else if (!isUsingSinglePreview) {
                        const previewPanel = contentProvider.getPreview(sourceUri);
                        if (previewPanel) {
                            previewPanel.reveal(vscode.ViewColumn.Two, true);
                        }
                    }
                }
                else if (automaticallyShowPreviewOfMarkdownBeingEdited) {
                    openPreviewToTheSide(sourceUri);
                }
            }
        }
    }));
    /*
      context.subscriptions.push(vscode.workspace.onDidOpenTextDocument((textDocument)=> {
          // console.log('onDidOpenTextDocument', textDocument.uri)
      }))
      */
    /*
      context.subscriptions.push(vscode.window.onDidChangeVisibleTextEditors(textEditors=> {
          // console.log('onDidChangeonDidChangeVisibleTextEditors ', textEditors)
      }))
      */
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openPreviewToTheSide", openPreviewToTheSide));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openPreview", openPreview));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.toggleScrollSync", toggleScrollSync));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.toggleLiveUpdate", toggleLiveUpdate));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.toggleBreakOnSingleNewLine", toggleBreakOnSingleNewLine));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openImageHelper", openImageHelper));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.runAllCodeChunks", runAllCodeChunksCommand));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.runCodeChunk", runCodeChunkCommand));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.syncPreview", syncPreview));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.customizeCss", customizeCSS));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openMermaidConfig", openMermaidConfig));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openMathJaxConfig", openMathJaxConfig));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.openKaTeXConfig", openKaTeXConfig));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.extendParser", extendParser));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.showUploadedImages", showUploadedImages));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.insertNewSlide", insertNewSlide));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.insertTable", insertTable));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.insertPagebreak", insertPagebreak));
    context.subscriptions.push(vscode.commands.registerCommand("markdown-preview-enhanced.createTOC", createTOC));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.revealLine", revealLine));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.insertImageUrl", insertImageUrl));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.pasteImageFile", image_helper_1.pasteImageFile));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.uploadImageFile", image_helper_1.uploadImageFile));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.refreshPreview", refreshPreview));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.openInBrowser", openInBrowser));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.htmlExport", htmlExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.chromeExport", chromeExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.princeExport", princeExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.eBookExport", eBookExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.pandocExport", pandocExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.markdownExport", markdownExport));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.webviewFinishLoading", webviewFinishLoading));
    // context.subscriptions.push(vscode.commands.registerCommand('_mume.cacheSVG', cacheSVG))
    context.subscriptions.push(vscode.commands.registerCommand("_mume.cacheCodeChunkResult", cacheCodeChunkResult));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.runCodeChunk", runCodeChunk));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.runAllCodeChunks", runAllCodeChunks));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.clickTagA", clickTagA));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.clickTaskListCheckbox", clickTaskListCheckbox));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.showUploadedImageHistory", showUploadedImages));
    context.subscriptions.push(vscode.commands.registerCommand("_mume.setPreviewTheme", setPreviewTheme));
}
exports.activate = activate;
function revealLine(uri, line) {
    const sourceUri = vscode.Uri.parse(uri);
    vscode.window.visibleTextEditors
        .filter((editor) => (0, preview_content_provider_1.isMarkdownFile)(editor.document) &&
        editor.document.uri.fsPath === sourceUri.fsPath)
        .forEach((editor) => {
        const sourceLine = Math.min(Math.floor(line), editor.document.lineCount - 1);
        const fraction = line - sourceLine;
        const text = editor.document.lineAt(sourceLine).text;
        const start = Math.floor(fraction * text.length);
        editorScrollDelay = Date.now() + 500;
        editor.revealRange(new vscode.Range(sourceLine, start, sourceLine + 1, 0), vscode.TextEditorRevealType.InCenter);
        editorScrollDelay = Date.now() + 500;
    });
}
/**
 * Get the top-most visible range of `editor`.
 *
 * Returns a fractional line number based the visible character within the line.
 * Floor to get real line number
 */
function getTopVisibleLine(editor) {
    if (!editor["visibleRanges"].length) {
        return undefined;
    }
    const firstVisiblePosition = editor["visibleRanges"][0].start;
    const lineNumber = firstVisiblePosition.line;
    const line = editor.document.lineAt(lineNumber);
    const progress = firstVisiblePosition.character / (line.text.length + 2);
    return lineNumber + progress;
}
exports.getTopVisibleLine = getTopVisibleLine;
/**
 * Get the bottom-most visible range of `editor`.
 *
 * Returns a fractional line number based the visible character within the line.
 * Floor to get real line number
 */
function getBottomVisibleLine(editor) {
    if (!editor["visibleRanges"].length) {
        return undefined;
    }
    const firstVisiblePosition = editor["visibleRanges"][0].end;
    const lineNumber = firstVisiblePosition.line;
    let text = "";
    if (lineNumber < editor.document.lineCount) {
        text = editor.document.lineAt(lineNumber).text;
    }
    const progress = firstVisiblePosition.character / (text.length + 2);
    return lineNumber + progress;
}
exports.getBottomVisibleLine = getBottomVisibleLine;
// this method is called when your extension is deactivated
function deactivate() {
    //
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map
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
exports.isMarkdownFile = exports.getPreviewUri = exports.useSinglePreview = exports.MarkdownPreviewEnhancedView = void 0;
const mume = require("@shd101wyy/mume");
const mume_1 = require("@shd101wyy/mume");
const utility_1 = require("@shd101wyy/mume/out/src/utility");
const fs = require("fs");
const os_1 = require("os");
const path = require("path");
const vscode = require("vscode");
const config_1 = require("./config");
// http://www.typescriptlang.org/play/
// https://github.com/Microsoft/vscode/blob/master/extensions/markdown/media/main.js
// https://github.com/Microsoft/vscode/tree/master/extensions/markdown/src
// https://github.com/tomoki1207/gfm-preview/blob/master/src/gfmProvider.ts
// https://github.com/cbreeden/vscode-markdownit
class MarkdownPreviewEnhancedView {
    constructor(context) {
        this.context = context;
        this.waiting = false;
        /**
         * The key is markdown file fsPath
         * value is MarkdownEngine
         */
        this.engineMaps = {};
        /**
         * The key is markdown file fspath
         * value is Preview (vscode.Webview) object
         */
        this.previewMaps = {};
        this.preview2EditorMap = new Map();
        /**
         * The key is markdown file fsPath
         * value is JSAndCssFiles
         */
        this.jsAndCssFilesMaps = {};
        this.config = config_1.MarkdownPreviewEnhancedConfig.getCurrentConfig();
        mume
            .init(this.config.configPath) // init markdown-preview-enhanced
            .then(() => {
            mume.onDidChangeConfigFile(this.refreshAllPreviews.bind(this));
            mume_1.MarkdownEngine.onModifySource(this.modifySource.bind(this));
            (0, utility_1.useExternalAddFileProtocolFunction)((filePath, preview) => {
                if (preview) {
                    return preview.webview
                        .asWebviewUri(vscode.Uri.file(filePath))
                        .toString(true)
                        .replace(/%3F/gi, "?")
                        .replace(/%23/g, "#");
                }
                else {
                    if (!filePath.startsWith("file://")) {
                        filePath = "file:///" + filePath;
                    }
                    filePath = filePath.replace(/^file\:\/+/, "file:///");
                    return filePath;
                }
            });
            const extensionVersion = require(path.resolve(this.context.extensionPath, "./package.json"))["version"];
            if (extensionVersion !== mume.configs.config["vscode_mpe_version"]) {
                const config = Object.assign({}, mume.configs.config, {
                    vscode_mpe_version: extensionVersion,
                });
                fs.writeFileSync(path.resolve(mume.getExtensionConfigPath(), "config.json"), JSON.stringify(config));
            }
        })
            .catch((error) => {
            vscode.window.showErrorMessage(error.toString());
        });
    }
    refreshAllPreviews() {
        // clear caches
        for (const key in this.engineMaps) {
            if (this.engineMaps.hasOwnProperty(key)) {
                const engine = this.engineMaps[key];
                if (engine) {
                    // No need to resetConfig.
                    // Otherwiser when user change settings like `previewTheme`, the preview won't change immediately.
                    // engine.resetConfig();
                    engine.clearCaches();
                }
            }
        }
        // refresh iframes
        if (useSinglePreview()) {
            this.refreshPreviewPanel(this.singlePreviewPanelSourceUriTarget);
        }
        else {
            for (const key in this.previewMaps) {
                if (this.previewMaps.hasOwnProperty(key)) {
                    this.refreshPreviewPanel(vscode.Uri.file(key));
                }
            }
        }
    }
    /**
     * modify markdown source, append `result` after corresponding code chunk.
     * @param codeChunkData
     * @param result
     * @param filePath
     */
    modifySource(codeChunkData, result, filePath) {
        return __awaiter(this, void 0, void 0, function* () {
            function insertResult(i, editor) {
                const lineCount = editor.document.lineCount;
                let start = 0;
                // find <!-- code_chunk_output -->
                for (let j = i + 1; j < i + 6 && j < lineCount; j++) {
                    if (editor.document
                        .lineAt(j)
                        .text.startsWith("<!-- code_chunk_output -->")) {
                        start = j;
                        break;
                    }
                }
                if (start) {
                    // found
                    // TODO: modify exited output
                    let end = start + 1;
                    while (end < lineCount) {
                        if (editor.document
                            .lineAt(end)
                            .text.startsWith("<!-- /code_chunk_output -->")) {
                            break;
                        }
                        end += 1;
                    }
                    // if output not changed, then no need to modify editor buffer
                    let r = "";
                    for (let i2 = start + 2; i2 < end - 1; i2++) {
                        r += editor.document.lineAt(i2).text + "\n";
                    }
                    if (r === result + "\n") {
                        return "";
                    } // no need to modify output
                    editor.edit((edit) => {
                        edit.replace(new vscode.Range(new vscode.Position(start + 2, 0), new vscode.Position(end - 1, 0)), result + "\n");
                    });
                    return "";
                }
                else {
                    editor.edit((edit) => {
                        edit.insert(new vscode.Position(i + 1, 0), `\n<!-- code_chunk_output -->\n\n${result}\n\n<!-- /code_chunk_output -->\n`);
                    });
                    return "";
                }
            }
            const visibleTextEditors = vscode.window.visibleTextEditors;
            for (let i = 0; i < visibleTextEditors.length; i++) {
                const editor = visibleTextEditors[i];
                if (this.formatPathIfNecessary(editor.document.uri.fsPath) === filePath) {
                    let codeChunkOffset = 0;
                    const targetCodeChunkOffset = codeChunkData.normalizedInfo.attributes["code_chunk_offset"];
                    const lineCount = editor.document.lineCount;
                    for (let i2 = 0; i2 < lineCount; i2++) {
                        const line = editor.document.lineAt(i2);
                        if (line.text.match(/^```(.+)\"?cmd\"?\s*[=\s}]/)) {
                            if (codeChunkOffset === targetCodeChunkOffset) {
                                i2 = i2 + 1;
                                while (i2 < lineCount) {
                                    if (editor.document.lineAt(i2).text.match(/^\`\`\`\s*/)) {
                                        break;
                                    }
                                    i2 += 1;
                                }
                                return insertResult(i2, editor);
                            }
                            else {
                                codeChunkOffset++;
                            }
                        }
                        else if (line.text.match(/\@import\s+(.+)\"?cmd\"?\s*[=\s}]/)) {
                            if (codeChunkOffset === targetCodeChunkOffset) {
                                return insertResult(i2, editor);
                            }
                            else {
                                codeChunkOffset++;
                            }
                        }
                    }
                    break;
                }
            }
            return "";
        });
    }
    /**
     * return markdown engine of sourceUri
     * @param sourceUri
     */
    getEngine(sourceUri) {
        return this.engineMaps[sourceUri.fsPath];
    }
    /**
     * return markdown preview of sourceUri
     * @param sourceUri
     */
    getPreview(sourceUri) {
        if (useSinglePreview()) {
            return this.singlePreviewPanel;
        }
        else {
            return this.previewMaps[sourceUri.fsPath];
        }
    }
    /**
     * check if the markdown preview is on for the textEditor
     * @param textEditor
     */
    isPreviewOn(sourceUri) {
        if (useSinglePreview()) {
            return !!this.singlePreviewPanel;
        }
        else {
            return !!this.getPreview(sourceUri);
        }
    }
    destroyPreview(sourceUri) {
        if (useSinglePreview()) {
            this.singlePreviewPanel = null;
            this.singlePreviewPanelSourceUriTarget = null;
            this.preview2EditorMap = new Map();
            this.previewMaps = {};
        }
        else {
            const previewPanel = this.getPreview(sourceUri);
            if (previewPanel) {
                this.preview2EditorMap.delete(previewPanel);
                delete this.previewMaps[sourceUri.fsPath];
            }
        }
    }
    /**
     * remove engine from this.engineMaps
     * @param sourceUri
     */
    destroyEngine(sourceUri) {
        if (useSinglePreview()) {
            return (this.engineMaps = {});
        }
        const engine = this.getEngine(sourceUri);
        if (engine) {
            delete this.engineMaps[sourceUri.fsPath]; // destroy engine
        }
    }
    /**
     * Format pathString if it is on Windows. Convert `c:\` like string to `C:\`
     * @param pathString
     */
    formatPathIfNecessary(pathString) {
        if (process.platform === "win32") {
            pathString = pathString.replace(/^([a-zA-Z])\:\\/, (_, $1) => `${$1.toUpperCase()}:\\`);
        }
        return pathString;
    }
    getProjectDirectoryPath(sourceUri, workspaceFolders = []) {
        const possibleWorkspaceFolders = workspaceFolders.filter((workspaceFolder) => {
            return (path
                .dirname(sourceUri.path.toUpperCase())
                .indexOf(workspaceFolder.uri.path.toUpperCase()) >= 0);
        });
        let projectDirectoryPath;
        if (possibleWorkspaceFolders.length) {
            // We pick the workspaceUri that has the longest path
            const workspaceFolder = possibleWorkspaceFolders.sort((x, y) => y.uri.fsPath.length - x.uri.fsPath.length)[0];
            projectDirectoryPath = workspaceFolder.uri.fsPath;
        }
        else {
            projectDirectoryPath = "";
        }
        return this.formatPathIfNecessary(projectDirectoryPath);
    }
    getFilePath(sourceUri) {
        return this.formatPathIfNecessary(sourceUri.fsPath);
    }
    /**
     * Initialize MarkdownEngine for this markdown file
     */
    initMarkdownEngine(sourceUri) {
        let engine = this.getEngine(sourceUri);
        if (!engine) {
            engine = new mume_1.MarkdownEngine({
                filePath: this.getFilePath(sourceUri),
                projectDirectoryPath: this.getProjectDirectoryPath(sourceUri, vscode.workspace.workspaceFolders),
                config: this.config,
            });
            this.engineMaps[sourceUri.fsPath] = engine;
            this.jsAndCssFilesMaps[sourceUri.fsPath] = [];
        }
        return engine;
    }
    initPreview(sourceUri, editor, viewOptions) {
        return __awaiter(this, void 0, void 0, function* () {
            const isUsingSinglePreview = useSinglePreview();
            let previewPanel;
            if (isUsingSinglePreview && this.singlePreviewPanel) {
                const oldResourceRoot = this.getProjectDirectoryPath(this.singlePreviewPanelSourceUriTarget, vscode.workspace.workspaceFolders) || path.dirname(this.singlePreviewPanelSourceUriTarget.fsPath);
                const newResourceRoot = this.getProjectDirectoryPath(sourceUri, vscode.workspace.workspaceFolders) || path.dirname(sourceUri.fsPath);
                if (oldResourceRoot !== newResourceRoot) {
                    this.singlePreviewPanel.dispose();
                    return this.initPreview(sourceUri, editor, viewOptions);
                }
                else {
                    previewPanel = this.singlePreviewPanel;
                    this.singlePreviewPanelSourceUriTarget = sourceUri;
                }
            }
            else if (this.previewMaps[sourceUri.fsPath]) {
                previewPanel = this.previewMaps[sourceUri.fsPath];
            }
            else {
                const localResourceRoots = [
                    vscode.Uri.file(this.context.extensionPath),
                    vscode.Uri.file(mume.utility.extensionDirectoryPath),
                    vscode.Uri.file(mume.getExtensionConfigPath()),
                    vscode.Uri.file((0, os_1.tmpdir)()),
                    vscode.Uri.file(this.getProjectDirectoryPath(sourceUri, vscode.workspace.workspaceFolders) || path.dirname(sourceUri.fsPath)),
                ];
                previewPanel = vscode.window.createWebviewPanel("markdown-preview-enhanced", `Preview ${path.basename(sourceUri.fsPath)}`, viewOptions, {
                    enableFindWidget: true,
                    localResourceRoots,
                    enableScripts: true, // TODO: This might be set by enableScriptExecution config. But for now we just enable it.
                });
                previewPanel.iconPath = vscode.Uri.file(path.join(this.context.extensionPath, "media", "preview.svg"));
                // register previewPanel message events
                previewPanel.webview.onDidReceiveMessage((message) => {
                    vscode.commands.executeCommand(`_mume.${message.command}`, ...message.args);
                }, null, this.context.subscriptions);
                // unregister previewPanel
                previewPanel.onDidDispose(() => {
                    this.destroyPreview(sourceUri);
                    this.destroyEngine(sourceUri);
                }, null, this.context.subscriptions);
                if (isUsingSinglePreview) {
                    this.singlePreviewPanel = previewPanel;
                    this.singlePreviewPanelSourceUriTarget = sourceUri;
                }
            }
            // register previewPanel
            this.previewMaps[sourceUri.fsPath] = previewPanel;
            this.preview2EditorMap.set(previewPanel, editor);
            // set title
            previewPanel.title = `Preview ${path.basename(sourceUri.fsPath)}`;
            // init markdown engine
            let initialLine;
            if (editor && editor.document.uri.fsPath === sourceUri.fsPath) {
                initialLine = yield new Promise((resolve, reject) => {
                    // Hack: sometimes we only get 0. I couldn't find API to wait for editor getting loaded.
                    setTimeout(() => {
                        return resolve(editor.selections[0].active.line || 0);
                    }, 100);
                });
            }
            const text = editor.document.getText();
            let engine = this.getEngine(sourceUri);
            if (!engine) {
                engine = this.initMarkdownEngine(sourceUri);
            }
            engine
                .generateHTMLTemplateForPreview({
                inputString: text,
                config: {
                    sourceUri: sourceUri.toString(),
                    initialLine,
                    vscode: true,
                },
                contentSecurityPolicy: "",
                vscodePreviewPanel: previewPanel,
            })
                .then((html) => {
                previewPanel.webview.html = html;
            });
        });
    }
    /**
     * Close all previews
     */
    closeAllPreviews(singlePreview) {
        if (singlePreview) {
            if (this.singlePreviewPanel) {
                this.singlePreviewPanel.dispose();
            }
        }
        else {
            const previewPanels = [];
            for (const key in this.previewMaps) {
                if (this.previewMaps.hasOwnProperty(key)) {
                    const previewPanel = this.previewMaps[key];
                    if (previewPanel) {
                        previewPanels.push(previewPanel);
                    }
                }
            }
            previewPanels.forEach((previewPanel) => previewPanel.dispose());
        }
        this.previewMaps = {};
        this.preview2EditorMap = new Map();
        this.engineMaps = {};
        this.singlePreviewPanel = null;
        this.singlePreviewPanelSourceUriTarget = null;
    }
    previewPostMessage(sourceUri, message) {
        const preview = this.getPreview(sourceUri);
        if (preview) {
            preview.webview.postMessage(message);
        }
    }
    previewHasTheSameSingleSourceUri(sourceUri) {
        if (!this.singlePreviewPanelSourceUriTarget) {
            return false;
        }
        else {
            return this.singlePreviewPanelSourceUriTarget.fsPath === sourceUri.fsPath;
        }
    }
    updateMarkdown(sourceUri, triggeredBySave) {
        const engine = this.getEngine(sourceUri);
        if (!engine) {
            return;
        }
        const previewPanel = this.getPreview(sourceUri);
        if (!previewPanel) {
            return;
        }
        // presentation mode
        if (engine.isPreviewInPresentationMode) {
            return this.refreshPreview(sourceUri);
        }
        // not presentation mode
        vscode.workspace.openTextDocument(sourceUri).then((document) => {
            const text = document.getText();
            this.previewPostMessage(sourceUri, {
                command: "startParsingMarkdown",
            });
            const preview = this.getPreview(sourceUri);
            engine
                .parseMD(text, {
                isForPreview: true,
                useRelativeFilePath: false,
                hideFrontMatter: false,
                triggeredBySave,
                vscodePreviewPanel: preview,
            })
                .then(({ markdown, html, tocHTML, JSAndCssFiles, yamlConfig }) => {
                // check JSAndCssFiles
                if (JSON.stringify(JSAndCssFiles) !==
                    JSON.stringify(this.jsAndCssFilesMaps[sourceUri.fsPath]) ||
                    yamlConfig["isPresentationMode"]) {
                    this.jsAndCssFilesMaps[sourceUri.fsPath] = JSAndCssFiles;
                    // restart iframe
                    this.refreshPreview(sourceUri);
                }
                else {
                    this.previewPostMessage(sourceUri, {
                        command: "updateHTML",
                        html,
                        tocHTML,
                        totalLineCount: document.lineCount,
                        sourceUri: sourceUri.toString(),
                        id: yamlConfig.id || "",
                        class: yamlConfig.class || "",
                    });
                }
            });
        });
    }
    refreshPreviewPanel(sourceUri) {
        this.preview2EditorMap.forEach((editor, previewPanel) => {
            if (previewPanel &&
                editor &&
                editor.document &&
                isMarkdownFile(editor.document) &&
                editor.document.uri &&
                editor.document.uri.fsPath === sourceUri.fsPath) {
                this.initPreview(sourceUri, editor, {
                    viewColumn: previewPanel.viewColumn,
                    preserveFocus: true,
                });
            }
        });
    }
    refreshPreview(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine.clearCaches();
            // restart iframe
            this.refreshPreviewPanel(sourceUri);
        }
    }
    openInBrowser(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine.openInBrowser({}).catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    htmlExport(sourceUri, offline) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .htmlExport({ offline })
                .then((dest) => {
                vscode.window.showInformationMessage(`File ${path.basename(dest)} was created at path: ${dest}`);
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    chromeExport(sourceUri, type) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .chromeExport({ fileType: type, openFileAfterGeneration: true })
                .then((dest) => {
                vscode.window.showInformationMessage(`File ${path.basename(dest)} was created at path: ${dest}`);
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    princeExport(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .princeExport({ openFileAfterGeneration: true })
                .then((dest) => {
                if (dest.endsWith("?print-pdf")) {
                    // presentation pdf
                    vscode.window.showInformationMessage(`Please copy and open the link: { ${dest.replace(/\_/g, "\\_")} } in Chrome then Print as Pdf.`);
                }
                else {
                    vscode.window.showInformationMessage(`File ${path.basename(dest)} was created at path: ${dest}`);
                }
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    eBookExport(sourceUri, fileType) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .eBookExport({ fileType, runAllCodeChunks: false })
                .then((dest) => {
                vscode.window.showInformationMessage(`eBook ${path.basename(dest)} was created as path: ${dest}`);
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    pandocExport(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .pandocExport({ openFileAfterGeneration: true })
                .then((dest) => {
                vscode.window.showInformationMessage(`Document ${path.basename(dest)} was created as path: ${dest}`);
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    markdownExport(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine
                .markdownExport({})
                .then((dest) => {
                vscode.window.showInformationMessage(`Document ${path.basename(dest)} was created as path: ${dest}`);
            })
                .catch((error) => {
                vscode.window.showErrorMessage(error.toString());
            });
        }
    }
    /*
    public cacheSVG(sourceUri: Uri, code:string, svg:string) {
      const engine = this.getEngine(sourceUri)
      if (engine) {
        engine.cacheSVG(code, svg)
      }
    }
    */
    cacheCodeChunkResult(sourceUri, id, result) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine.cacheCodeChunkResult(id, result);
        }
    }
    runCodeChunk(sourceUri, codeChunkId) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine.runCodeChunk(codeChunkId).then(() => {
                this.updateMarkdown(sourceUri);
            });
        }
    }
    runAllCodeChunks(sourceUri) {
        const engine = this.getEngine(sourceUri);
        if (engine) {
            engine.runCodeChunks().then(() => {
                this.updateMarkdown(sourceUri);
            });
        }
    }
    update(sourceUri) {
        if (!this.config.liveUpdate || !this.getPreview(sourceUri)) {
            return;
        }
        if (!this.waiting) {
            this.waiting = true;
            setTimeout(() => {
                this.waiting = false;
                // this._onDidChange.fire(uri);
                this.updateMarkdown(sourceUri);
            }, 300);
        }
    }
    updateConfiguration() {
        const newConfig = config_1.MarkdownPreviewEnhancedConfig.getCurrentConfig();
        if (!this.config.isEqualTo(newConfig)) {
            // if `singlePreview` setting is changed, close all previews.
            if (this.config.singlePreview !== newConfig.singlePreview) {
                this.closeAllPreviews(this.config.singlePreview);
                this.config = newConfig;
            }
            else {
                this.config = newConfig;
                for (const fsPath in this.engineMaps) {
                    if (this.engineMaps.hasOwnProperty(fsPath)) {
                        const engine = this.engineMaps[fsPath];
                        engine.updateConfiguration(newConfig);
                    }
                }
                // update all generated md documents
                this.refreshAllPreviews();
            }
        }
    }
    openImageHelper(sourceUri) {
        if (sourceUri.scheme === "markdown-preview-enhanced") {
            return vscode.window.showWarningMessage("Please focus a markdown file.");
        }
        else if (!this.isPreviewOn(sourceUri)) {
            return vscode.window.showWarningMessage("Please open preview first.");
        }
        else {
            return this.previewPostMessage(sourceUri, {
                command: "openImageHelper",
            });
        }
    }
}
exports.MarkdownPreviewEnhancedView = MarkdownPreviewEnhancedView;
/**
 * check whehter to use only one preview or not
 */
function useSinglePreview() {
    const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
    return config.get("singlePreview");
}
exports.useSinglePreview = useSinglePreview;
function getPreviewUri(uri) {
    if (uri.scheme === "markdown-preview-enhanced") {
        return uri;
    }
    let previewUri;
    if (useSinglePreview()) {
        previewUri = uri.with({
            scheme: "markdown-preview-enhanced",
            path: "single-preview.rendered",
        });
    }
    else {
        previewUri = uri.with({
            scheme: "markdown-preview-enhanced",
            path: uri.path + ".rendered",
            query: uri.toString(),
        });
    }
    return previewUri;
}
exports.getPreviewUri = getPreviewUri;
function isMarkdownFile(document) {
    return (document.languageId === "markdown" &&
        document.uri.scheme !== "markdown-preview-enhanced"); // prevent processing of own documents
}
exports.isMarkdownFile = isMarkdownFile;
//# sourceMappingURL=preview-content-provider.js.map
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.uploadImageFile = exports.pasteImageFile = void 0;
const mume_1 = require("@shd101wyy/mume");
const fs = require("fs");
const path = require("path");
const vscode = require("vscode");
const preview_content_provider_1 = require("./preview-content-provider");
/**
 * Copy ans paste image at imageFilePath to config.imageForlderPath.
 * Then insert markdown image url to markdown file.
 * @param uri
 * @param imageFilePath
 */
function pasteImageFile(sourceUri, imageFilePath) {
    if (typeof sourceUri === "string") {
        sourceUri = vscode.Uri.parse(sourceUri);
    }
    const imageFolderPath = vscode.workspace
        .getConfiguration("markdown-preview-enhanced")
        .get("imageFolderPath");
    let imageFileName = path.basename(imageFilePath);
    const projectDirectoryPath = vscode.workspace.rootPath;
    let assetDirectoryPath;
    let description;
    if (imageFolderPath[0] === "/") {
        assetDirectoryPath = path.resolve(projectDirectoryPath, "." + imageFolderPath);
    }
    else {
        assetDirectoryPath = path.resolve(path.dirname(sourceUri.fsPath), imageFolderPath);
    }
    const destPath = path.resolve(assetDirectoryPath, path.basename(imageFilePath));
    vscode.window.visibleTextEditors
        .filter((editor) => (0, preview_content_provider_1.isMarkdownFile)(editor.document) &&
        editor.document.uri.fsPath === sourceUri.fsPath)
        .forEach((editor) => {
        fs.mkdir(assetDirectoryPath, (error) => {
            fs.stat(destPath, (err, stat) => {
                if (err == null) {
                    // file existed
                    const lastDotOffset = imageFileName.lastIndexOf(".");
                    const uid = "_" +
                        Math.random()
                            .toString(36)
                            .substr(2, 9);
                    if (lastDotOffset > 0) {
                        description = imageFileName.slice(0, lastDotOffset);
                        imageFileName =
                            imageFileName.slice(0, lastDotOffset) +
                                uid +
                                imageFileName.slice(lastDotOffset, imageFileName.length);
                    }
                    else {
                        description = imageFileName;
                        imageFileName = imageFileName + uid;
                    }
                    fs.createReadStream(imageFilePath).pipe(fs.createWriteStream(path.resolve(assetDirectoryPath, imageFileName)));
                }
                else if (err.code === "ENOENT") {
                    // file doesn't exist
                    fs.createReadStream(imageFilePath).pipe(fs.createWriteStream(destPath));
                    if (imageFileName.lastIndexOf(".")) {
                        description = imageFileName.slice(0, imageFileName.lastIndexOf("."));
                    }
                    else {
                        description = imageFileName;
                    }
                }
                else {
                    return vscode.window.showErrorMessage(err.toString());
                }
                vscode.window.showInformationMessage(`Image ${imageFileName} has been copied to folder ${assetDirectoryPath}`);
                let url = `${imageFolderPath}/${imageFileName}`;
                if (url.indexOf(" ") >= 0) {
                    url = url.replace(/ /g, "%20");
                }
                editor.edit((textEditorEdit) => {
                    textEditorEdit.insert(editor.selection.active, `![${description}](${url})`);
                });
            });
        });
    });
}
exports.pasteImageFile = pasteImageFile;
function replaceHint(editor, line, hint, withStr) {
    const textLine = editor.document.lineAt(line);
    if (textLine.text.indexOf(hint) >= 0) {
        editor.edit((textEdit) => {
            textEdit.replace(new vscode.Range(new vscode.Position(line, 0), new vscode.Position(line, textLine.text.length)), textLine.text.replace(hint, withStr));
        });
        return true;
    }
    return false;
}
function setUploadedImageURL(imageFileName, url, editor, hint, curPos) {
    let description;
    if (imageFileName.lastIndexOf(".")) {
        description = imageFileName.slice(0, imageFileName.lastIndexOf("."));
    }
    else {
        description = imageFileName;
    }
    const withStr = `![${description}](${url})`;
    if (!replaceHint(editor, curPos.line, hint, withStr)) {
        let i = curPos.line - 20;
        while (i <= curPos.line + 20) {
            if (replaceHint(editor, i, hint, withStr)) {
                break;
            }
            i++;
        }
    }
}
/**
 * Upload image at imageFilePath to config.imageUploader.
 * Then insert markdown image url to markdown file.
 * @param uri
 * @param imageFilePath
 */
function uploadImageFile(sourceUri, imageFilePath, imageUploader) {
    // console.log('uploadImageFile', sourceUri, imageFilePath, imageUploader)
    if (typeof sourceUri === "string") {
        sourceUri = vscode.Uri.parse(sourceUri);
    }
    const imageFileName = path.basename(imageFilePath);
    vscode.window.visibleTextEditors
        .filter((editor) => (0, preview_content_provider_1.isMarkdownFile)(editor.document) &&
        editor.document.uri.fsPath === sourceUri.fsPath)
        .forEach((editor) => {
        const uid = Math.random()
            .toString(36)
            .substr(2, 9);
        const hint = `![Uploading ${imageFileName}… (${uid})]()`;
        const curPos = editor.selection.active;
        editor.edit((textEditorEdit) => {
            textEditorEdit.insert(curPos, hint);
        });
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        const AccessKey = config.get("AccessKey") || "";
        const SecretKey = config.get("SecretKey") || "";
        const Bucket = config.get("Bucket") || "";
        const Domain = config.get("Domain") || "";
        mume_1.utility
            .uploadImage(imageFilePath, {
            method: imageUploader,
            qiniu: { AccessKey, SecretKey, Bucket, Domain },
        })
            .then((url) => {
            setUploadedImageURL(imageFileName, url, editor, hint, curPos);
        })
            .catch((error) => {
            vscode.window.showErrorMessage(error.toString());
        });
    });
}
exports.uploadImageFile = uploadImageFile;
//# sourceMappingURL=image-helper.js.map
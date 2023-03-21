// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import * as vscode from 'vscode';
import * as json from './json';

enum SlideShowType {
	slide = 'slide',
	subslide = 'subslide',
	fragment = 'fragment',
	skip = 'skip',
	notes = 'notes',
	none = 'none'
}


export class CellSlideShowStatusBarProvider implements vscode.NotebookCellStatusBarItemProvider {
	provideCellStatusBarItems(cell: vscode.NotebookCell, token: vscode.CancellationToken): vscode.ProviderResult<vscode.NotebookCellStatusBarItem[]> {
		const items: vscode.NotebookCellStatusBarItem[] = [];
		const slideshow = cell.metadata.custom?.metadata?.slideshow;

		if (slideshow?.slide_type) {
			items.push({
				text: `Slide Type: ${slideshow.slide_type}`,
				tooltip: `Slide Type: ${slideshow.slide_type}`,
				command: 'jupyter-slideshow.switchSlideType',
				alignment: vscode.NotebookCellStatusBarAlignment.Right,
			});
		}

		return items;
	}
}

export function getActiveCell() {
	// find active cell
	const editor = vscode.window.activeNotebookEditor;
	if (!editor) {
		return;
	}

	return editor.notebook.cellAt(editor.selections[0].start);
}

export function reviveCell(args: vscode.NotebookCell | vscode.Uri | undefined): vscode.NotebookCell | undefined {
	if (!args) {
		return getActiveCell();
	}

	if (args && 'index' in args && 'kind' in args && 'notebook' in args && 'document' in args) {
        return args as vscode.NotebookCell;
    }

	if (args && 'scheme' in args && 'path' in args) {
		const cellUri = vscode.Uri.from(args);
		const cellUriStr = cellUri.toString();
		let activeCell: vscode.NotebookCell | undefined = undefined;

		for (const document of vscode.workspace.notebookDocuments) {
			for (const cell of document.getCells()) {
				if (cell.document.uri.toString() === cellUriStr) {
					activeCell = cell;
					break;
				}
			}

			if (activeCell) {
				break;
			}
		}

		return activeCell;
	}

	return undefined;
}

export function register(context: vscode.ExtensionContext) {
	context.subscriptions.push(vscode.notebooks.registerNotebookCellStatusBarItemProvider('jupyter-notebook', new CellSlideShowStatusBarProvider()));

    context.subscriptions.push(vscode.commands.registerCommand('jupyter-slideshow.switchSlideType', async (cell: vscode.NotebookCell | vscode.Uri | undefined) => {
		cell = reviveCell(cell);
		if (!cell) {
			return;
		}

		// create quick pick items for each slide type
		const items: vscode.QuickPickItem[] = [];
		for (const type in SlideShowType) {
			items.push({
				label: type
			});
		}

		// show quick pick
		const selected = await vscode.window.showQuickPick(items);
		// updat cell metadata with this slide type
		if (selected) {
			const cellMetadataCopy = { ...cell.metadata };
			if (selected.label === SlideShowType.none) {
				// remove the slideshow metadata
				delete cellMetadataCopy.custom?.metadata?.slideshow;
			} else {
				if (!cellMetadataCopy.custom) {
					cellMetadataCopy.custom = {};
				}

				if (cellMetadataCopy.custom.metadata) {
					cellMetadataCopy.custom.metadata.slideshow = cellMetadataCopy.custom.metadata.slideshow ?? {};
					cellMetadataCopy.custom.metadata.slideshow.slide_type = selected.label;
				} else {
					// no metadata, so create it
					cellMetadataCopy.custom.metadata = {
						slideshow: {
							slide_type: selected.label
						}
					};
				}
			}

			// create workspace edit to update slideshow
			const edit = new vscode.WorkspaceEdit();
			const nbEdit = vscode.NotebookEdit.updateCellMetadata(cell.index, {
				...cellMetadataCopy,
			});
			edit.set(cell.notebook.uri, [nbEdit]);
			await vscode.workspace.applyEdit(edit);
		}
	}));

	context.subscriptions.push(vscode.commands.registerCommand('jupyter-slideshow.editSlideShowInJSON', async (cell: vscode.NotebookCell | vscode.Uri | undefined) => {
		cell = reviveCell(cell);
		if (!cell) {
			return;
		}

		const resourceUri = cell.notebook.uri;
		const document = await vscode.workspace.openTextDocument(resourceUri);
		const tree = json.parseTree(document.getText());
		const cells = json.findNodeAtLocation(tree, ['cells']);
		if (cells && cells.children && cells.children[cell.index]) {
			const cellNode = cells.children[cell.index];
			const metadata = json.findNodeAtLocation(cellNode, ['metadata']);
			if (metadata) {
				const slideshow = json.findNodeAtLocation(metadata, ['slideshow']);
				if (slideshow) {
					const range = new vscode.Range(document.positionAt(slideshow.offset), document.positionAt(slideshow.offset + slideshow.length));
					await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
				} else {
					const range = new vscode.Range(document.positionAt(metadata.offset), document.positionAt(metadata.offset + metadata.length));
					await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
				}
			}  else {
				const range = new vscode.Range(document.positionAt(cellNode.offset), document.positionAt(cellNode.offset + cellNode.length));
				await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
			}
		}
	}));
}
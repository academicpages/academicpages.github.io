// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import * as vscode from 'vscode';
import * as json from './json';

export async function addCellTag(cell: vscode.NotebookCell, tags: string[]) {
	const oldTags = cell.metadata.custom?.metadata?.tags ?? [];
    const newTags: string[] = [];
    for (const tag of tags) {
        if (!oldTags.includes(tag)) {
            newTags.push(tag);
        }
    }
	if (newTags.length) {
		oldTags.push(...newTags);
	}

	const cellMetadata = { ...cell.metadata };
	if (!cellMetadata.custom) {
		cellMetadata.custom = {};
	}

	if (!cellMetadata.custom.metadata) {
		cellMetadata.custom.metadata = {};
	}

	cellMetadata.custom.metadata.tags = oldTags;

    // create workspace edit to update tag
    const edit = new vscode.WorkspaceEdit();
    const nbEdit = vscode.NotebookEdit.updateCellMetadata(cell.index, {
        ...cellMetadata,
    });
    edit.set(cell.notebook.uri, [nbEdit]);
    await vscode.workspace.applyEdit(edit);
}

export class CellTagStatusBarProvider implements vscode.NotebookCellStatusBarItemProvider {
	provideCellStatusBarItems(cell: vscode.NotebookCell, token: vscode.CancellationToken): vscode.ProviderResult<vscode.NotebookCellStatusBarItem[]> {
		const items: vscode.NotebookCellStatusBarItem[] = [];
		cell.metadata.custom?.metadata?.tags?.forEach((tag: string) => {
			items.push({
				text: '$(close) ' + tag,
				tooltip: tag,
				command: {
					title: `Remove Tag ${tag}`,
					command: 'jupyter-cell-tags.removeTag',
					arguments: [cell, tag]
				},
				alignment: vscode.NotebookCellStatusBarAlignment.Left,
			});
		});

		if (items.length) {
			// add insert tag status bar item
			items.push({
				text: '$(plus) Tag',
				tooltip: 'Add Tag',
				command: {
					title: 'Add Tag',
					command: 'jupyter-cell-tags.addTag',
					arguments: [cell]
				},
				alignment: vscode.NotebookCellStatusBarAlignment.Left,
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

	if (editor.selections[0].start >= editor.notebook.cellCount) {
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
	context.subscriptions.push(vscode.notebooks.registerNotebookCellStatusBarItemProvider('jupyter-notebook', new CellTagStatusBarProvider()));
	context.subscriptions.push(vscode.commands.registerCommand('jupyter-cell-tags.removeTag', async (cell: vscode.NotebookCell | string, tag: string) => {
		let activeCell: vscode.NotebookCell | undefined;
		if (typeof cell === 'string') {
			// find active cell
			activeCell = getActiveCell();
			tag = cell;
		} else {
			activeCell = cell;
		}

		if (!activeCell) {
			return;
		}

        let tags = activeCell.metadata.custom.metadata.tags;
        if (tags) {
            // remove tag from tags
            const index = tags.indexOf(tag);
            if (index > -1) {
                tags.splice(index, 1);
            }
            activeCell.metadata.custom.metadata.tags = tags;

            // create workspace edit to update tag
            const edit = new vscode.WorkspaceEdit();
            const nbEdit = vscode.NotebookEdit.updateCellMetadata(activeCell.index, {
                ...activeCell.metadata,
            });
            edit.set(activeCell.notebook.uri, [nbEdit]);
            await vscode.workspace.applyEdit(edit);
        } else {
            return;
        }
	}));

	context.subscriptions.push(vscode.commands.registerCommand('jupyter-cell-tags.addTag', async (cell: vscode.NotebookCell | vscode.Uri | undefined) => {
		cell = reviveCell(cell);
		
		if (!cell) {
			return;
		}

		const tag = await vscode.window.showInputBox({
			placeHolder: 'Type to create a cell tag'
		});

		if (tag) {
			await addCellTag(cell, [tag]);
		}
	}));

	context.subscriptions.push(vscode.commands.registerCommand('jupyter-cell-tags.paramaterize', async (cell: vscode.NotebookCell | vscode.Uri | undefined) => {
		cell = reviveCell(cell);
		if (!cell) {
			return;
		}
		await addCellTag(cell, ['parameters']);
	}));

	context.subscriptions.push(vscode.commands.registerCommand('jupyter-cell-tags.editTagsInJSON', async (cell: vscode.NotebookCell | vscode.Uri | undefined) => {
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
				const tags = json.findNodeAtLocation(metadata, ['tags']);
				if (tags) {
					const range = new vscode.Range(document.positionAt(tags.offset), document.positionAt(tags.offset + tags.length));
					await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
				} else {
					const range = new vscode.Range(document.positionAt(metadata.offset), document.positionAt(metadata.offset + metadata.length));
					await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
				}
			} else {
				const range = new vscode.Range(document.positionAt(cellNode.offset), document.positionAt(cellNode.offset + cellNode.length));
				await vscode.window.showTextDocument(document, { selection: range, viewColumn: vscode.ViewColumn.Beside });
			}
		}
	}));
}
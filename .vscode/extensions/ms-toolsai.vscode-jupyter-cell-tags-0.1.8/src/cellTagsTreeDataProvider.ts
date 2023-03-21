// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import * as vscode from 'vscode';
import { getCellTags } from './helper';

export class TagTreeDataProvider implements vscode.TreeDataProvider<string> {
	private _onDidChangeTreeData: vscode.EventEmitter<void> = new vscode.EventEmitter<void>();
	onDidChangeTreeData: vscode.Event<void> = this._onDidChangeTreeData.event;

	private _tags: string[] = [];
	private _disposables: vscode.Disposable[] = [];
	private _editorDisposables: vscode.Disposable[] = [];
	constructor() {
		this._tags = [];

		this._disposables.push(vscode.window.onDidChangeActiveNotebookEditor(e => {
			this.registerEditorListeners(e);
		}));

		if (vscode.window.activeNotebookEditor) {
			this.registerEditorListeners(vscode.window.activeNotebookEditor);
		}
	}

	private async registerEditorListeners(editor: vscode.NotebookEditor | undefined) {
		this._editorDisposables.forEach(d => d.dispose());

		if (!editor) {
			return;
		}

		if (editor.notebook.notebookType !== 'jupyter-notebook') {
			return;
		}

		await vscode.commands.executeCommand('setContext', 'jupyter:showTagsExplorer', true);

		this._editorDisposables = [];
		this._editorDisposables.push(vscode.window.onDidChangeNotebookEditorSelection(e => {
			this.updateTags(editor);
		}));
		this._editorDisposables.push(vscode.workspace.onDidChangeNotebookDocument(e => {
			this.updateTags(editor);
		}));
		this.updateTags(editor);
	}

	private async updateTags(editor: vscode.NotebookEditor | undefined) {
		// clear if no editor
		if (!editor) {
			this._tags = [];
			this._onDidChangeTreeData.fire();
			return;
		}

		// get active cell
		if (!editor.selections || !editor.selections[0]) {
			return;
		}

		if (editor.selections[0].start >= editor.notebook.cellCount) {
			return;
		}

		const activeCell = editor.notebook.cellAt(editor.selections[0].start);
		if (!activeCell) {
			this._tags = [];
			this._onDidChangeTreeData.fire();
			return;
		}

		// get tags
		const tags = getCellTags(activeCell);
		this._tags = tags;
		this._onDidChangeTreeData.fire();
	}

	getTreeItem(element: string): vscode.TreeItem | Thenable<vscode.TreeItem> {
		return {
			label: element,
			collapsibleState: vscode.TreeItemCollapsibleState.None,
		};
	}

	getChildren(element?: string | undefined): vscode.ProviderResult<string[]> {
		if (!element) {
			return this._tags;
		} else {
			return [];
		}
	}

	dispose() {
		this._editorDisposables.forEach(d => d.dispose());
		this._disposables.forEach(d => d.dispose());
	}
}

export function register(context: vscode.ExtensionContext) {
	// register tree view for tags on the sidebar
	const treeDataProvider = new TagTreeDataProvider();
	context.subscriptions.push(vscode.window.registerTreeDataProvider('cell-tag', treeDataProvider));
}
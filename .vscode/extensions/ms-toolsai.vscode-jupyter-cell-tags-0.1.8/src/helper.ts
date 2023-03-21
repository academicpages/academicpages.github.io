// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import * as vscode from 'vscode';

export function getCellTags(cell: vscode.NotebookCell) {
	return cell.metadata.custom?.metadata?.tags ?? [];
}
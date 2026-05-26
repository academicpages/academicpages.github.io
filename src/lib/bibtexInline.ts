import type { BibTeXInlineNode } from '@/types/publication';

const commandTypes: Record<string, Exclude<BibTeXInlineNode['type'], 'text'>> = {
  emph: 'em',
  textit: 'em',
  textbf: 'strong',
  textsc: 'smallCaps',
  textsuperscript: 'sup',
  textsubscript: 'sub',
};

interface ParseResult {
  nodes: BibTeXInlineNode[];
  index: number;
}

export interface ParsedBibTeXInline {
  plainText: string;
  nodes: BibTeXInlineNode[];
}

function normalizeBibTeXInput(value: string): string {
  return value.replace(/^["']|["']$/g, '');
}

function pushText(nodes: BibTeXInlineNode[], text: string) {
  if (!text) return;

  const last = nodes[nodes.length - 1];
  if (last?.type === 'text') {
    last.text += text;
    return;
  }

  nodes.push({ type: 'text', text });
}

function readCommand(value: string, index: number): { command: string; index: number } {
  let cursor = index;
  let command = '';

  while (cursor < value.length && /[A-Za-z]/.test(value[cursor])) {
    command += value[cursor];
    cursor += 1;
  }

  if (!command && cursor < value.length) {
    command = value[cursor];
    cursor += 1;
  }

  return { command, index: cursor };
}

function parseGroup(value: string, index: number): ParseResult | null {
  if (value[index] !== '{') {
    return null;
  }

  return parseNodes(value, index + 1, true);
}

function parseNodes(value: string, startIndex: number, stopAtBrace: boolean): ParseResult {
  const nodes: BibTeXInlineNode[] = [];
  let index = startIndex;

  while (index < value.length) {
    const char = value[index];

    if (char === '}' && stopAtBrace) {
      return { nodes, index: index + 1 };
    }

    if (char === '{') {
      const parsedGroup = parseGroup(value, index);
      if (parsedGroup) {
        nodes.push(...parsedGroup.nodes);
        index = parsedGroup.index;
        continue;
      }
    }

    if (char === '\\') {
      const { command, index: afterCommand } = readCommand(value, index + 1);

      if (command === 'cite') {
        const citationGroup = parseGroup(value, afterCommand);
        index = citationGroup?.index ?? afterCommand;
        continue;
      }

      const nodeType = commandTypes[command];
      if (nodeType && value[afterCommand] === '{') {
        const parsedGroup = parseGroup(value, afterCommand);
        if (parsedGroup) {
          nodes.push({ type: nodeType, children: parsedGroup.nodes });
          index = parsedGroup.index;
          continue;
        }
      }

      pushText(nodes, command ? command : '\\');
      index = afterCommand;
      continue;
    }

    if (char === '~') {
      pushText(nodes, ' ');
      index += 1;
      continue;
    }

    pushText(nodes, char);
    index += 1;
  }

  return { nodes, index };
}

function compactWhitespace(value: string): string {
  return value.replace(/\s+/g, ' ').trim();
}

export function flattenBibTeXInlineNodes(nodes: BibTeXInlineNode[]): string {
  return nodes.map((node) => {
    if (node.type === 'text') {
      return node.text;
    }
    return flattenBibTeXInlineNodes(node.children);
  }).join('');
}

export function parseBibTeXInline(value?: string): ParsedBibTeXInline {
  if (!value) {
    return { plainText: '', nodes: [] };
  }

  const parsed = parseNodes(normalizeBibTeXInput(value), 0, false);
  const plainText = compactWhitespace(flattenBibTeXInlineNodes(parsed.nodes));

  return {
    plainText,
    nodes: parsed.nodes,
  };
}

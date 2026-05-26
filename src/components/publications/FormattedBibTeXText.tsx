import type { BibTeXInlineNode } from '@/types/publication';

interface FormattedBibTeXTextProps {
  nodes?: BibTeXInlineNode[];
  fallback: string;
}

function renderNodes(nodes: BibTeXInlineNode[], keyPrefix = 'node'): React.ReactNode {
  return nodes.map((node, index) => {
    const key = `${keyPrefix}-${index}`;

    if (node.type === 'text') {
      return node.text;
    }

    const children = renderNodes(node.children, key);

    if (node.type === 'em') {
      return <em key={key}>{children}</em>;
    }

    if (node.type === 'strong') {
      return <strong key={key}>{children}</strong>;
    }

    if (node.type === 'smallCaps') {
      return (
        <span key={key} className="font-semibold uppercase tracking-[0.08em] text-[0.88em]">
          {children}
        </span>
      );
    }

    if (node.type === 'sup') {
      return <sup key={key}>{children}</sup>;
    }

    return <sub key={key}>{children}</sub>;
  });
}

export default function FormattedBibTeXText({ nodes, fallback }: FormattedBibTeXTextProps) {
  if (!nodes || nodes.length === 0) {
    return <>{fallback}</>;
  }

  return <>{renderNodes(nodes)}</>;
}

module.exports = function (Prism) {
  Prism.languages.k = {
    comment: [
      {
        pattern: /(^|[^\\])\/\*[\s\S]*?(?:\*\/|$)/,
        lookbehind: true,
      },
      {
        pattern: /(^|[^\\:])\/\/.*/,
        lookbehind: true,
        greedy: true,
      },
    ],
    string: {
      pattern: /(["'])(?:\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/,
      greedy: true,
    },
    "class-name": /\b(?:strict|avoid|prefer|bracket|non-assoc|seqstrict|left|right|macro\-rec|macro|token|notInRules|autoReject|structural|latex|binder|klabel|symbol|format)\b/,
    keyword: {
      pattern: /\b(?:syntax\s+(?:priority|priorities|left|right|non-assoc|lexical)|syntax|rule|Id|Int|Bool|String|Token|Lexer|Float|configuration|import|imports|require|requires|Kresult|context\s+alias|context|module|endmodule|claim)\b/,
      greedy: true,
    },
    boolean: /\b(?:true|false)\b/,
    number: /\b0x[\da-f]+\b|(?:\b\d+\.?\d*|\B\.\d+)(?:e[+-]?\d+)?/i,
    operator: {
      pattern: /[<>]=|=>|~>|[!=]=?=?|--?|\+\+?|&&?|\|\|?|[?*/~^%]/,
    },
    punctuation: /[{}[\];(),.:]/,
    // copied from prism-markup.js
    tag: {
      pattern: /<\/?(?!\d)[^\s>\/=$<%]+(?:\s(?:\s*[^\s>\/=]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s'">=]+(?=[\s>]))|(?=[\s/>])))+)?\s*\/?>/,
      greedy: true,
      inside: {
        tag: {
          pattern: /^<\/?[^\s>\/]+/,
          inside: {
            punctuation: /^<\/?/,
            namespace: /^[^\s>\/:]+:/,
          },
        },
        "attr-value": {
          pattern: /=\s*(?:"[^"]*"|'[^']*'|[^\s'">=]+)/,
          inside: {
            punctuation: [
              {
                pattern: /^=/,
                alias: "attr-equals",
              },
              /"|'/,
            ],
          },
        },
        punctuation: /\/?>/,
        "attr-name": {
          pattern: /[^\s>\/]+/,
          inside: {
            namespace: /^[^\s>\/:]+:/,
          },
        },
      },
    },
  };
};

module.exports = function (Prism) {
  Prism.languages.iele = {
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
    variable: {
      pattern: /(@|%)([A-Za-z0-9\\_\\.\\-\\$])[a-zA-Z\\.\\_\\$][0-9a-zA-Z\\.\\_\\-\\$]*/,
      greedy: true,
    },
    string: {
      pattern: /(["'])(?:\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/,
      greedy: true,
    },
    keyword: /\b(?:load|store|sload|sstore|iszero|not|add|mul|sub|div|exp|mod|addmod|mulmod|expmod|byte|sext|twos|and|or|xor|shift|lt|le|gt|ge|eq|ne|cmp|sha3|br|call|staticcall|at|send|gaslimit|ret|void|revert|log|create|copycreate|selfdestruct|contract|external|define|public|log2|bswap|calladdress)\b/,
    label: /(?!\d)(?:[-$.\w]|\\[a-f\d]{2})+:/i,
    boolean: /\b(?:true|false)\b/,
    number: /\b0x[\da-f]+\b|(?:\b\d+\.?\d*|\B\.\d+)(?:e[+-]?\d+)?/i,
    operator: /[<>]=?|[!=]=?=?|--?|\+\+?|&&?|\|\|?|[?*/~^%]/,
    punctuation: /[{}[\];(),.:]/,
  };
};

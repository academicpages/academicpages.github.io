/**
 * This file is a modified version of:
 * https://github.com/marmelab/highlight-search-term/blob/main/src/index.js
 * - We return the `nonMatchingElements`
 * - We fixed a bug: `getRangesForSearchTermInElement` got the `node.parentElement`, which is not working if there are multiple text nodes in one element.
 *
 * highlight-search-term is published under MIT License.
 *
 * MIT License
 *
 * Copyright (c) 2024 marmelab
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/**
 * Highlight search term in the selected elements
 *
 * @example
 * import { highlightSearchTerm } from "highlight-search-term";
 * const search = document.getElementById("search");
 * search.addEventListener("input", () => {
 *   highlightSearchTerm({ search: search.value, selector: ".content" });
 * });
 */
const highlightSearchTerm = ({ search, selector, customHighlightName = "search" }) => {
  if (!selector) {
    throw new Error("The selector argument is required");
  }

  if (!CSS.highlights) return; // disable feature on Firefox as it does not support CSS Custom Highlight API

  // remove previous highlight
  CSS.highlights.delete(customHighlightName);
  if (!search) {
    // nothing to highlight
    return;
  }
  // find all text nodes containing the search term
  const ranges = [];
  const nonMatchingElements = [];
  const elements = document.querySelectorAll(selector);
  Array.from(elements).map((element) => {
    let match = false;
    getTextNodesInElementContainingText(element, search).forEach((node) => {
      // Modified variant of highlight-search-term
      // We return the non-matching elements in addition.
      const rangesForSearch = getRangesForSearchTermInNode(node, search);
      ranges.push(...rangesForSearch);
      if (rangesForSearch.length > 0) {
        match = true;
      }
    });
    if (!match) {
      nonMatchingElements.push(element);
    }
  });
  if (ranges.length === 0) return nonMatchingElements; // modified: return `nonMatchingElements`
  // create a CSS highlight that can be styled with the ::highlight(search) pseudo-element
  const highlight = new Highlight(...ranges);
  CSS.highlights.set(customHighlightName, highlight);
  return nonMatchingElements; // modified: return `nonMatchingElements`
};

const getTextNodesInElementContainingText = (element, text) => {
  const nodes = [];
  const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
  let node;
  while ((node = walker.nextNode())) {
    if (node.textContent && node.textContent.toLowerCase().includes(text)) {
      nodes.push(node);
    }
  }
  return nodes;
};

// Fix: We changed this function to work on the node directly, rather than on its parent element.
const getRangesForSearchTermInNode = (node, search) => {
  const ranges = [];
  const text = (node.textContent ? node.textContent.toLowerCase() : "") || "";

  let start = 0;
  let index;
  while ((index = text.indexOf(search, start)) >= 0) {
    const range = new Range();
    range.setStart(node, index);
    range.setEnd(node, index + search.length);
    ranges.push(range);
    start = index + search.length;
  }
  return ranges;
};

export { highlightSearchTerm };

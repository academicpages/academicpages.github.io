'use strict';

/**
 * Array random slice with items count.
 * @param {Array} arr
 * @param {Number} num, number of sub items.
 * @return {Array}
 */
exports.randomSlice = function randomSlice(arr, num) {
  if (!num || num >= arr.length) {
    return arr.slice();
  }
  var index = Math.floor(Math.random() * arr.length);
  var a = [];
  for (var i = 0, j = index; i < num; i++) {
    a.push(arr[j++]);
    if (j === arr.length) {
      j = 0;
    }
  }
  return a;
};

/**
 * Remove one exists element from an array
 * @param {Array} arr
 * @param  {Number} index - remove element index
 * @return {Array} the array instance
 */
exports.spliceOne = function spliceOne(arr, index) {
  if (index < 0) {
    index = arr.length + index;
    // still negative, not found element
    if (index < 0) {
      return arr;
    }
  }

  // don't touch
  if (index >= arr.length) {
    return arr;
  }

  for (var i = index, k = i + 1, n = arr.length; k < n; i += 1, k += 1) {
    arr[i] = arr[k];
  }
  arr.pop();
  return arr;
};

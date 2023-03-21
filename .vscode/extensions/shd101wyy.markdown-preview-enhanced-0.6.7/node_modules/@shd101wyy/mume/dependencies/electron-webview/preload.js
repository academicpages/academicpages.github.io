// referred and modified from
// https://github.com/KidkArolis/electronic-post-message/blob/master/epm.js

const {ipcRenderer} = require('electron')

function dispatch (msgStr, source) {
  var message = new MessageEvent('message', {
    view: window.parent,
    bubbles: false,
    cancelable: false,
    data: msgStr,
    source: source
  })
  window.dispatchEvent(message)
}

// Please notice that host shoud have channelName: `_postMessage`
const channelName = '_postMessage'

// inside of webview
window.parent.postMessage = function (msgStr) {
  ipcRenderer.sendToHost(channelName, {
    data: msgStr
  })
}

ipcRenderer.on(channelName, function (event, msgStr) {
  dispatch(msgStr, window.parent)
})
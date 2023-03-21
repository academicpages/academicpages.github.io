<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">不相容或不相符的 C/C++ 延伸模組二進位檔</h1>

<p data-loc-id="incompat.extension.text1">C/C++ 延伸模組包含原生二進位檔。</p>

<p data-loc-id="incompat.extension.text2">在 VS Code 中透過市集 UI 安裝時，應包含正確的原生二進位檔。如果偵測到不相容的二進位檔，並且 C/C++ 延伸模組已透過 VS Code 中的市集 UI 安裝，<a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">請回報問題</a>。</p>

<h1 data-loc-id="reinstalling.extension.heading">重新安裝 C/C++ 延伸模組</h1>

<p data-loc-id="reinstall.extension.text1">重新安裝延伸模組的對等版本時，VS Code 可能會重複使用現有延伸模組目錄。為防止在重新安裝 C/C++ 延伸模組時發生這種情況，可能需要先删除現有延伸模組目錄。</p>

<p data-loc-id="reinstall.extension.text2">可在使用者目錄下的以下路徑之一 (Windows 上為 `%USERPROFILE%`，Linux 和 macOS 上為 `$HOME`) 下找到安裝的延伸模組目錄</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">在遠端連線上:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">安裝的 C/C++ 延伸模組目錄的範例路徑:</p>

<p data-loc-id="reinstall.extension.text5">在 Windows 上:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">在 Linux 上:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">然後藉由 VS Code 中的市集 UI 重新安裝。</p>

<p data-loc-id="reinstall.extension.text8">如果 VS Code 未能部署正確版本的延伸模組，則您系統的正確 VSIX 可能是 <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">從 VS Code 市集網站下載</a>，它是使用 VS Code 中市集 UI '...' 功能表下的 `從 VSIX 安裝...` 選項來進行安裝的。</p>
</body></html>
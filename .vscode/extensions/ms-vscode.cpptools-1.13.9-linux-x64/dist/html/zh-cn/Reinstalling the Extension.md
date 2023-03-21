<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">C/C++ 扩展二进制文件不兼容或不匹配</h1>

<p data-loc-id="incompat.extension.text1">C/C++ 扩展包括本机二进制文件。</p>

<p data-loc-id="incompat.extension.text2">通过 VS Code 中的市场 UI 安装时，应包含正确的本机二进制文件。如果检测到不兼容的二进制文件，并且已通过 VS Code 中的市场 UI 安装 C/C++ 扩展，则 <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">请报告问题</a>。</p>

<h1 data-loc-id="reinstalling.extension.heading">正在重新安装 C/C++ 扩展</h1>

<p data-loc-id="reinstall.extension.text1">重新安装等效版本的扩展时，VS Code 可能重用现有的扩展目录。如果要在重新安装 C/C++ 扩展时放置发生这种情况，可能需要先删除现有的扩展目录。</p>

<p data-loc-id="reinstall.extension.text2">可在用户目录下以下路径之一的下面找到已安装的扩展目录(Windows 上的 `%USERPROFILE%` 或 Linux 和 macOS 上的 `$HOME`)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">在远程连接中:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">已安装的 C/C++ 扩展目录的示例路径:</p>

<p data-loc-id="reinstall.extension.text5">在 Windows 上:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">在 Linux 上:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">然后通过 VS Code 中的市场 UI 重新安装。</p>

<p data-loc-id="reinstall.extension.text8">如果 VS Code 无法部署扩展的正确版本，则可以 <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">已从 VS Code 市场网站下载</a> 并使用 VS Code 中市场 UI 内 “...” 菜单下的 `从 VSIX... 安装` 选项安装系统的正确 VSIX。</p>
</body></html>
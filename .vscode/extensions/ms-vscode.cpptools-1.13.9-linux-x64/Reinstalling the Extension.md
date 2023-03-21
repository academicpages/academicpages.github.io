<h1 data-loc-id="incompatible.extension.heading">Incompatible or Mismatched C/C++ Extension Binaries</h1>

<p data-loc-id="incompat.extension.text1">The C/C++ extension includes native binaries.</p>

<p data-loc-id="incompat.extension.text2">When installed via the marketplace UI in VS Code, the correct native binaries should be included.  If incompatible binaries were detected and the C/C++ extension had been installed via the marketplace UI in VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&labels=&template=bug_report.md" data-loc-id="bug.report.link.title">please report the issue</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Reinstalling the C/C++ Extension</h1>

<p data-loc-id="reinstall.extension.text1">When reinstalling an equivalent version of an extension, VS Code may reuse the existing extension directory. To prevent this from occurring when reinstalling the C/C++ extension, it may be necessary to first delete the existing extension directory.</p>

<p data-loc-id="reinstall.extension.text2">Installed extension directories can be found under one of the following paths under your user directory (`%USERPROFILE%` on Windows, or `$HOME` on Linux and macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">In a remote connection:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Example paths to installed C/C++ extension directories:</p>

<p data-loc-id="reinstall.extension.text5">On Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">On Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Then reinstall via the marketplace UI in VS Code.</p>

<p data-loc-id="reinstall.extension.text8">If the correct version of the extension fails to be deployed by VS Code, the correct VSIX for your system can be <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">downloaded from the VS Code marketplace web site</a> and installed using the `Install from VSIX...` option under the '...' menu in the marketplace UI in VS Code.</p>

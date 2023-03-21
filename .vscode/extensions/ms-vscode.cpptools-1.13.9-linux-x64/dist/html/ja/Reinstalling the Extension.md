<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">互換性がない、または一致しない C/C++ 拡張バイナリ</h1>

<p data-loc-id="incompat.extension.text1">C/C++ 拡張機能には、ネイティブ バイナリが含まれています。</p>

<p data-loc-id="incompat.extension.text2">VS Codeのマーケットプレース UI を介してインストールする場合は、正しいネイティブ バイナリを含める必要があります。 互換性のないバイナリが検出され、VS Codeのマーケットプレース UI を介して C/C++ 拡張機能がインストールされている場合は、<a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">問題を報告してください</a>。</p>

<h1 data-loc-id="reinstalling.extension.heading">C/C++ 拡張機能の再インストール</h1>

<p data-loc-id="reinstall.extension.text1">同等のバージョンの拡張機能を再インストールする場合、VS Code は既存の拡張機能ディレクトリを再利用できます。C/C++ 拡張機能を再インストールするときにこの問題が発生しないようにするには、最初に既存の拡張ディレクトリを削除する必要がある場合があります。</p>

<p data-loc-id="reinstall.extension.text2">インストールされている拡張ディレクトリは、ユーザー ディレクトリ (Windows の場合は '%USERPROFILE%'、Linux および macOS では '$HOME') の下にある次のいずれかのパスにあります</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">リモート接続の場合:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">インストールされている C/C++ 拡張ディレクトリへのパスの例:</p>

<p data-loc-id="reinstall.extension.text5">Windows の場合:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">Linux の場合:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">次に、VS Code のマーケットプレース UI を使用して再インストールします。</p>

<p data-loc-id="reinstall.extension.text8">拡張機能の正しいバージョンを VS Code で展開できない場合は、。VS Codeのマーケットプレース UI のメニューにある '...' の下の [VSIX からインストールする...] オプションを使用して、システムの正しい VSIX を <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">VS Code マーケットプレイス Web サイトからダウンロードされました</a> し、インストールできます。</p>
</body></html>
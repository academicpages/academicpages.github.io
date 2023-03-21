<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Inkompatible oder nicht übereinstimmende Binärdateien der C/C++-Erweiterung</h1>

<p data-loc-id="incompat.extension.text1">Die C/C++-Erweiterung enthält native Binärdateien.</p>

<p data-loc-id="incompat.extension.text2">Bei der Installation über die Marketplace-Benutzeroberfläche in VS&nbsp;Code sollten die richtigen nativen Binärdateien enthalten sein. Wenn inkompatible Binärdateien erkannt wurden und die C/C++-Erweiterung über die Marketplace-Benutzeroberfläche in VS&nbsp;Code installiert wurde, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">Melden Sie das Problem</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">C/C++-Erweiterung wird neu installiert</h1>

<p data-loc-id="reinstall.extension.text1">Bei der Neuinstallation einer entsprechenden Version einer Erweiterung kann VS&nbsp;Code das vorhandene Erweiterungsverzeichnis wiederverwenden. Um zu verhindern, dass dies bei der Neuinstallation der C/C++-Erweiterung auftritt, ist es möglicherweise erforderlich, zuerst das vorhandene Erweiterungsverzeichnis zu löschen.</p>

<p data-loc-id="reinstall.extension.text2">Installierte Erweiterungsverzeichnisse finden Sie unter einem der folgenden Pfade unter Ihrem Benutzerverzeichnis („%USERPROFILE%“ unter Windows oder „$HOME“ unter Linux und macOS).</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">In einer Remoteverbindung:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Beispielpfade zu installierten C/C++-Erweiterungsverzeichnissen:</p>

<p data-loc-id="reinstall.extension.text5">Unter Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">Unter Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Installieren Sie dann über die Marketplace-Benutzeroberfläche in VS&nbsp;Code neu.</p>

<p data-loc-id="reinstall.extension.text8">Wenn die richtige Version der Erweiterung nicht von VS&nbsp;Code bereitgestellt werden kann, kann das richtige VSIX für Ihr System <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">von der Website „VS&nbsp;Code Marketplace“ heruntergeladen</a> und mithilfe der Option „Von VSIX installieren...“ unter dem Menü „...“ in der Marketplace-Benutzeroberfläche in VS&nbsp;Code installiert werden.</p>
</body></html>
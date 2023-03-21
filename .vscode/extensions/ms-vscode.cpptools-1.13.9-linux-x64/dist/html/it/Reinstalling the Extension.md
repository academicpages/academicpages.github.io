<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">file binari dell'estensione C/C++ incompatibili o non corrispondenti</h1>

<p data-loc-id="incompat.extension.text1">L'estensione C/C++ include file binari nativi.</p>

<p data-loc-id="incompat.extension.text2">Se installato tramite l'interfaccia utente del marketplace in VS Code, è necessario includere i file binari nativi corretti.  Se sono stati rilevati file binari incompatibili e l'estensione C/C++ è stata installata tramite l'interfaccia utente del Marketplace in VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">segnalare il problema</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Reinstallazione dell'estensione C/C++</h1>

<p data-loc-id="reinstall.extension.text1">Quando si reinstalla una versione equivalente di un'estensione, VS Code può riutilizzare la directory dell'estensione esistente. Per evitare che ciò si verifichi durante la reinstallazione dell'estensione C/C++, potrebbe essere necessario eliminare prima la directory dell'estensione esistente.</p>

<p data-loc-id="reinstall.extension.text2">Le directory delle estensioni installate si trovano in uno dei percorsi seguenti nella directory utente ('%USERPROFILE%' in Windows o '$HOME' in Linux e macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">In una connessione remota:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Percorsi di esempio per le directory dell'estensione C/C++ installate:</p>

<p data-loc-id="reinstall.extension.text5">In Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">In Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Reinstallare quindi tramite l'interfaccia utente del marketplace in VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Se la versione corretta dell'estensione non viene distribuita da VS Code, è possibile <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">scaricato dal sito Web del marketplace VS Code</a> e installare il file VSIX corretto per il sistema usando l'opzione 'Installa da VSIX...' nel menu '...' nell'interfaccia utente del marketplace in VS Code.</p>
</body></html>
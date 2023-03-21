<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Archivos binarios de extensión C/C++ incompatibles o no coincidentes</h1>

<p data-loc-id="incompat.extension.text1">La extensión C/C++ incluye archivos binarios nativos.</p>

<p data-loc-id="incompat.extension.text2">Cuando se instala a través de la interfaz de usuario de Marketplace en VS Code, se deben incluir los archivos binarios nativos correctos.  Si se detectaron archivos binarios incompatibles y se instaló la extensión C/C++ a través de la interfaz de usuario de Marketplace en VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">notifique el problema</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Reinstalando la extensión C/C++</h1>

<p data-loc-id="reinstall.extension.text1">Al reinstalar una versión equivalente de una extensión, VS Code puede reutilizar el directorio de extensión existente. Para evitar que esto ocurra al reinstalar la extensión C/C++, puede ser necesario eliminar primero el directorio de extensión existente.</p>

<p data-loc-id="reinstall.extension.text2">Los directorios de extensión instalados se pueden encontrar en una de las siguientes rutas de acceso en el directorio de usuario ('%USERPROFILE%' en Windows o '$HOME' en Linux y macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">En una conexión remota:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Rutas de acceso de ejemplo para los directorios de extensiones C/C++ instalados:</p>

<p data-loc-id="reinstall.extension.text5">En Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">En Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">A continuación, reinstale mediante la interfaz de usuario de Marketplace en VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Si VS Code no puede implementar la versión correcta de la extensión, el VSIX correcto para el sistema se puede <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">descargado del sitio web del Marketplace VS Code</a> e instalar mediante la opción \"Instalar desde VSIX...\", en el menú \"...\" en la interfaz de usuario de Marketplace en VS Code.</p>
</body></html>
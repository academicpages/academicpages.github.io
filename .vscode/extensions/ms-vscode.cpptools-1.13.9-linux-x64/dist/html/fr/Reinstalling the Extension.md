<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Fichiers binaires d’extension C/C++ incompatibles ou mal assortis</h1>

<p data-loc-id="incompat.extension.text1">L’extension C/C++ inclut des fichiers binaires natifs.</p>

<p data-loc-id="incompat.extension.text2">Lorsqu’ils sont installés via l’interface utilisateur de la Place de marché dans VS Code, les fichiers binaires natifs appropriés doivent être inclus.  Si des fichiers binaires incompatibles ont été détectés et que l’extension C/C++ a été installée via l’interface utilisateur marketplace dans VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">signalez le problème</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Réinstallation de l’extension C/C++</h1>

<p data-loc-id="reinstall.extension.text1">Lors de la réinstallation d’une version équivalente d’une extension, VS Code pouvez réutiliser le répertoire d’extension existant. Pour éviter que cela ne se produise lors de la réinstallation de l’extension C/C++, il peut être nécessaire de supprimer d’abord le répertoire d’extension existant.</p>

<p data-loc-id="reinstall.extension.text2">Les répertoires d’extension installés se trouvent sous l’un des chemins d’accès suivants sous votre répertoire utilisateur ('%USERPROFILE%' sur Windows, ou '$HOME' sur Linux et macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">Dans une connexion à distance&nbsp;:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Exemples de chemins d’accès aux répertoires d’extension C/C++ installés&nbsp;:</p>

<p data-loc-id="reinstall.extension.text5">Sur Windows&nbsp;:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">Sur Linux&nbsp;:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Réinstallez ensuite via l’interface utilisateur de la Place de marché dans VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Si la version correcte de l’extension ne peut pas être déployée par VS Code, le VSIX approprié pour votre système peut être <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">téléchargé à partir du site web de la place de marché VS Code</a> et installé à l’aide de l’option «&nbsp;Installer à partir de VSIX...&nbsp;» sous le menu «&nbsp;...&nbsp;» de l’interface utilisateur de la Place de marché dans VS Code.</p>
</body></html>
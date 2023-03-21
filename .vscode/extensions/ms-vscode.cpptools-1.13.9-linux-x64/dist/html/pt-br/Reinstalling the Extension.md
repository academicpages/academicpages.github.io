<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Binários de Extensão C/C++ Incompatíveis ou não Combinam</h1>

<p data-loc-id="incompat.extension.text1">A extensão C/C++ inclui binários nativos.</p>

<p data-loc-id="incompat.extension.text2">Quando instalado por meio da Interface do Usuário do marketplace VS Code, os binários nativos corretos devem ser incluídos.  Se os binários incompatíveis foram detectados e a extensão C/C++ foi instalada por meio da Interface do Usuário do marketplace no VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">relate o problema</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Reinstalando a Extensão C/C++</h1>

<p data-loc-id="reinstall.extension.text1">Ao reinstalar uma versão equivalente de uma extensão, VS Code pode reutilizar o diretório de extensão existente. Para evitar que isso ocorra ao reinstalar a extensão C/C++, talvez seja necessário excluir primeiro o diretório de extensão existente.</p>

<p data-loc-id="reinstall.extension.text2">Os diretórios de extensão instalados podem ser encontrados em um dos seguintes caminhos em seu diretório de usuário ('%USERPROFILE%' no Windows ou `$HOME` no Linux e macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">Em uma conexão remota:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Caminhos de exemplo para os diretórios de extensão C/C++ instalados:</p>

<p data-loc-id="reinstall.extension.text5">No Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">No Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Em seguida, reinstale por meio da Interface do Usuário do marketplace VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Se a versão correta da extensão não for implantada pelo VS Code, o VSIX correto para o sistema poderá ser <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">baixado do site VS Code marketplace</a> e instalado usando a opção 'Instalar do VSIX...' em '...' na Interface do Usuário do marketplace VS Code.</p>
</body></html>
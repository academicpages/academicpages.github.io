<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Nekompatibilní nebo neodpovídající binární soubory rozšíření C/C++</h1>

<p data-loc-id="incompat.extension.text1">Rozšíření C/C++ obsahuje nativní binární soubory.</p>

<p data-loc-id="incompat.extension.text2">Při instalaci přes rozhraní tržiště ve VS Code by měly být zahrnuty správné nativní binární soubory.  Pokud byly zjištěny nekompatibilní binární soubory a rozšíření C/C++ bylo nainstalováno prostřednictvím uživatelského rozhraní tržiště ve VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">nahlaste prosím problém</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Přeinstaluje se rozšíření C/C++.</h1>

<p data-loc-id="reinstall.extension.text1">Při přeinstalování ekvivalentní verze rozšíření může VS Code znovu použít stávající adresář rozšíření. Aby k tomu při přeinstalování rozšíření C/C++ nedošlo, může být nutné stávající adresář rozšíření nejprve odstranit.</p>

<p data-loc-id="reinstall.extension.text2">Nainstalované adresáře rozšíření najdete v jedné z následujících cest v uživatelském adresáři (`%USERPROFILE%` v systému Windows nebo `$HOME` v systémech Linux a macOS).</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">Ve vzdáleném připojení:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Ukázkové cesty k nainstalovaným adresářům rozšíření C/C++:</p>

<p data-loc-id="reinstall.extension.text5">Ve Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">V Linuxu:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Pak ji znovu nainstalujte přes uživatelské rozhraní Marketplace ve VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Pokud VS Code nenasadí správnou verzi rozšíření, můžete správný soubor VSIX pro váš systém <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">staženo z webu VS Code Marketplace</a> a nainstalovat pomocí možnosti Instalovat z VSIX.... v uživatelském rozhraní Marketplace ve VS Code.</p>
</body></html>
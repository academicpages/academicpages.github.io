<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Niekompatybilne lub niepasujące pliki binarne rozszerzenia C/C++</h1>

<p data-loc-id="incompat.extension.text1">Rozszerzenie C/C++ zawiera natywne pliki binarne.</p>

<p data-loc-id="incompat.extension.text2">Po zainstalowaniu za pośrednictwem interfejsu użytkownika platformy handlowej w programie VS Code należy uwzględnić poprawne natywne pliki binarne. Jeśli wykryto niezgodne pliki binarne i rozszerzenie C/C++ zostało zainstalowane za pośrednictwem interfejsu użytkownika platformy handlowej w programie VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">Zgłoś problem</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Ponowne instalowanie rozszerzenia C/C++</h1>

<p data-loc-id="reinstall.extension.text1">Podczas ponownego instalowania równoważnej wersji rozszerzenia, program VS Code może ponownie użyć istniejącego katalogu rozszerzeń. Aby temu zapobiec, podczas ponownej instalacji rozszerzenia C/C++, może być konieczne wstępne usunięcie istniejącego katalogu rozszerzeń.</p>

<p data-loc-id="reinstall.extension.text2">Zainstalowane katalogi rozszerzeń można znaleźć w jednej z następujących ścieżek w katalogu użytkownika (`%USERPROFILE%` w systemie Windows lub `$HOME` w systemach Linux i macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">W połączeniu zdalnym:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Przykładowe ścieżki do zainstalowanych katalogów rozszerzeń C/C++:</p>

<p data-loc-id="reinstall.extension.text5">W systemie Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">W systemie Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Następnie zainstaluj ponownie za pośrednictwem interfejsu użytkownika platformy handlowej w programie VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Jeśli prawidłowa wersja rozszerzenia nie zostanie wdrożona przez program VS Code, można <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">Pobrano z witryny internetowej platformy handlowej programu VS Code</a> i zainstalować poprawny plik VSIX dla Twojego systemu przy użyciu opcji „Zainstaluj z VISIX...“, w menu „...“, w interfejsie użytkownika platformy handlowej w programie VS Code.</p>
</body></html>
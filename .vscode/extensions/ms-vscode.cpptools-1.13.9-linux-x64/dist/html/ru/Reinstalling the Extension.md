<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Несовместимые или несоответствующие двоичные файлы расширения C/C++</h1>

<p data-loc-id="incompat.extension.text1">Расширение C/C++ включает собственные двоичные файлы.</p>

<p data-loc-id="incompat.extension.text2">При установке через пользовательский интерфейс Marketplace в VS Code должны быть включены подходящие собственные двоичные файлы. Если обнаружены несовместимые двоичные файлы и расширение C/C++ было установлено через пользовательский интерфейс Marketplace в VS Code, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">сообщите о проблеме</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">Переустановка расширения C/C++</h1>

<p data-loc-id="reinstall.extension.text1">При повторной установке эквивалентной версии расширения VS Code может повторно использовать существующий каталог расширений. Чтобы предотвратить переустановку расширения C/C++, может потребоваться сначала удалить существующий каталог расширений.</p>

<p data-loc-id="reinstall.extension.text2">Каталоги установленных расширений можно найти по одному из следующих путей в каталоге пользователя (“%USERPROFILE%” в Windows или “$HOME” в Linux и macOS)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">При удаленном подключении:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Примеры путей к каталогам установленного расширения C/C++:</p>

<p data-loc-id="reinstall.extension.text5">В Windows:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">В Linux:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Затем переустановите с помощью пользовательского интерфейса Marketplace в VS Code.</p>

<p data-loc-id="reinstall.extension.text8">Если не удается развернуть правильную версию расширения с помощью VS Code, правильный файл VSIX для системы можно <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">скачано с веб-сайта Marketplace VS Code</a> и установить с помощью параметра “Установить из VSIX...” в разделе “...” меню в пользовательском интерфейсе Marketplace в VS Code.</p>
</body></html>
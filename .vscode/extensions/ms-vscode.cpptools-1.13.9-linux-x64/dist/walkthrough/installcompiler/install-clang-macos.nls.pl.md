<h1 data-loc-id="walkthough.mac.install.compiler">Zainstaluj kompilator języka C++ w systemie macOS</h1>
<p data-loc-id="walkthough.mac.text1">Jeśli programujesz w języku C++ dla systemu macOS, zalecamy zainstalowanie kompilatora Clang. Wystarczy uruchomić następujące polecenie w oknie terminalu, aby zainstalować narzędzia deweloperskie wiersza polecenia:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">Następnie, aby sprawdzić, czy kompilator Clang jest zainstalowany, uruchom następujące polecenie w oknie terminalu. Powinien zostać wyświetlony komunikat z informacjami o używanej wersji kompilatora Clang.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

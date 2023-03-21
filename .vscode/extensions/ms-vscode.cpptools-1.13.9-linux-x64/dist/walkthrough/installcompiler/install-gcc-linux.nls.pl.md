<h1 data-loc-id="walkthrough.linux.install.compiler">Zainstaluj kompilator języka C++ w systemie Linux</h1>
<p data-loc-id="walkthrough.linux.text1">Jeśli programujesz w języku C++ dla systemu Linux, zalecamy zainstalowanie zestawu kompilatorów GCC. Instalowanie zestawu kompilatorów GCC jest proste. Wykonaj następujące trzy kroki:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Uruchom następujące polecenie w oknie terminalu, aby zaktualizować listy pakietów systemu Ubuntu. Nieaktualna dystrybucja systemu Linux czasami może zakłócać próby zainstalowania nowych pakietów.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Zainstaluj narzędzia kompilatora GNU i debuger GDB za pomocą następującego polecenia:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Sprawdź, czy zestaw kompilatorów GCC jest zainstalowany, uruchamiając następujące polecenie. Powinien zostać wyświetlony komunikat o prawach autorskich i informacje o używanej wersji zestawu kompilatorów GCC.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

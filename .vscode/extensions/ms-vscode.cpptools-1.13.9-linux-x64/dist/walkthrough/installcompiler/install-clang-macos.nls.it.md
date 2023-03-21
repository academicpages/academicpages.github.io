<h1 data-loc-id="walkthough.mac.install.compiler">Installa un compilatore C++ in macOS</h1>
<p data-loc-id="walkthough.mac.text1">Se si sviluppa con C++ per macOS, è consigliabile installare il compilatore Clang. A questo scopo, è sufficiente eseguire il comando seguente in una finestra di terminale per installare gli strumenti di sviluppo da riga di comando:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">Quindi, per verificare che Clang sia installato, eseguire il comando seguente in una finestra di terminale. Verrà visualizzato un messaggio contenente informazioni sulla versione di Clang in uso.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

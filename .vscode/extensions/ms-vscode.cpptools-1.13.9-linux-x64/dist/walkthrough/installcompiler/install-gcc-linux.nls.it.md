<h1 data-loc-id="walkthrough.linux.install.compiler">Installa un compilatore C++ in Linux</h1>
<p data-loc-id="walkthrough.linux.text1">Se si sviluppa in C++ per Linux, è consigliabile installare il compilatore GCC. L'installazione di GCC è semplice. Basta seguire questi tre passaggi:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Per aggiornare gli elenchi di pacchetti Ubuntu, eseguire il comando seguente dalla finestra del terminale. Una distribuzione Linux non aggiornata può talvolta interferire con i tentativi di installare nuovi pacchetti.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Per installare gli strumenti del compilatore GNU e il debugger GDB, usare questo comando:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Verificare che GCC sia installato eseguendo il comando seguente. Verranno visualizzati un messaggio di copyright e le informazioni sulla versione di GCC in uso.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

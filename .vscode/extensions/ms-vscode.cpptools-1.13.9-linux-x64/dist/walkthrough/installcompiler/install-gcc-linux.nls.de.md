<h1 data-loc-id="walkthrough.linux.install.compiler">C++-Compiler unter Linux installieren</h1>
<p data-loc-id="walkthrough.linux.text1">Wenn Sie mithilfe von C++ unter Linux entwickeln, empfehlen wir die Installation des GCC-Compilers. Die Installation von GCC ist einfach, führen Sie nur die folgenden drei Schritte aus:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Führen Sie den folgenden Befehl aus dem Terminalfenster aus, um die Ubuntu-Paketlisten zu aktualisieren. Eine veraltete Linux-Distribution kann manchmal die Installation neuer Pakete stören.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Installieren Sie die GNU-Compiler-Tools und den GDB-Debugger mit folgendem Befehl:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Überprüfen Sie, ob GCC installiert ist, indem Sie den folgenden Befehl ausführen. Es sollten ein Copyrighthinweis sowie Informationen zur verwendeten GCC-Version angezeigt werden.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

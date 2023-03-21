<h1 data-loc-id="walkthrough.linux.install.compiler">Installer un compilateur C++ sur Linux</h1>
<p data-loc-id="walkthrough.linux.text1">Si vous effectuez du développement C++ pour Linux, nous vous recommandons d'installer le compilateur GCC. L'installation de GCC est simple, il suffit de suivre ces trois étapes&nbsp;:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Exécutez la commande suivante à partir de la fenêtre du terminal pour mettre à jour les listes de packages Ubuntu. Une distribution Linux obsolète peut parfois interférer avec les tentatives d’installation de nouveaux packages.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Installez les outils du compilateur GNU et le débogueur GDB avec cette commande&nbsp;:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Vérifiez que GCC est installé en exécutant la commande suivante. Vous devez voir un message de copyright et des informations sur la version de GCC que vous utilisez.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

<h1 data-loc-id="walkthough.mac.install.compiler">Installer un compilateur C++ sur macOS</h1>
<p data-loc-id="walkthough.mac.text1">Si vous effectuez du développement C++ pour macOS, nous vous recommandons d'installer le compilateur Clang. Il vous suffit d'exécuter la commande suivante dans une fenêtre de Terminal pour installer les outils de développement en ligne de commande&nbsp;:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">Ensuite, pour vérifier que Clang est installé, exécutez la commande suivante dans une fenêtre de terminal. Vous devez voir un message contenant des informations sur la version de Clang que vous utilisez.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

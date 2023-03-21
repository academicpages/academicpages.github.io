<h1 data-loc-id="walkthrough.linux.install.compiler">Instalar um compilador C++ no Linux</h1>
<p data-loc-id="walkthrough.linux.text1">Se você estiver desenvolvendo em C++ para Linux, recomendamos instalar o compilador GCC. Instalar o GCC é simples, basta seguir estas três etapas:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Execute o seguinte comando na janela do terminal para atualizar as listas de pacotes do Ubuntu. Uma distribuição Linux desatualizada às vezes pode interferir nas tentativas de instalação de novos pacotes.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Instale as ferramentas do compilador GNU e o depurador GDB com este comando:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Verifique se o GCC está instalado executando o seguinte comando. Você deve ver uma mensagem de direitos autorais e informações sobre a versão do GCC que está usando.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

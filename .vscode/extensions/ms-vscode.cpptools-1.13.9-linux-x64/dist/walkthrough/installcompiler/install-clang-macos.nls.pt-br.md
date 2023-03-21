<h1 data-loc-id="walkthough.mac.install.compiler">Instalar um compilador C++ no macOS</h1>
<p data-loc-id="walkthough.mac.text1">Se você estiver desenvolvendo em C++ para macOS, recomendamos instalar o compilador Clang. Tudo o que você precisa fazer é executar o seguinte comando em uma janela do Terminal para instalar as ferramentas do desenvolvedor da linha de comando:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">Em seguida, para verificar se o clang está instalado, execute o seguinte comando em uma janela do Terminal. Você deverá ver uma mensagem com informações sobre a versão do Clang que está usando.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

<h1 data-loc-id="walkthough.mac.install.compiler">Instalación de un compilador de C++ en macOS</h1>
<p data-loc-id="walkthough.mac.text1">Si está realizando el desarrollo de C++ para macOS, se recomienda instalar el compilador de Clang. Todo lo que debe hacer es ejecutar el siguiente comando en una ventana del terminal para instalar las herramientas de desarrollo de la línea de comandos:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">A continuación, para comprobar que Clang está instalado, ejecute el siguiente comando en una ventana de Terminal. Debería ver un mensaje con información sobre la versión de Clang que está usando.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

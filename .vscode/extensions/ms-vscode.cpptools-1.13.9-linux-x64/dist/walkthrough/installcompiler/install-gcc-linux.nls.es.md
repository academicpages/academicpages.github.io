<h1 data-loc-id="walkthrough.linux.install.compiler">Instalación de un compilador de C++ en Linux</h1>
<p data-loc-id="walkthrough.linux.text1">Si va a realizar el desarrollo de C++ para Linux, se recomienda instalar el compilador GCC. La instalación de GCC es sencilla. Solo tiene que seguir estos tres pasos:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">Ejecute el siguiente comando desde la ventana del terminal para actualizar las listas de paquetes de Ubuntu. A veces, una distribución de Linux obsoleta puede interferir con los intentos de instalación de nuevos paquetes.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">Instale las herramientas del compilador GNU y el depurador de GDB con este comando:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">Ejecute el siguiente comando para comprobar que GCC está instalado. Debería ver un mensaje de copyright e información sobre la versión de GCC que usa.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

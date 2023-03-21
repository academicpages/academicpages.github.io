<h1 data-loc-id="walkthough.mac.install.compiler">Install a C++ compiler on macOS</h1>
<p data-loc-id="walkthough.mac.text1">If you&#39;re doing C++ development for macOS, we recommend installing the Clang compiler. All you need to do is run the following command in a Terminal window to install the command line developer tools:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">Then, to verify that clang is installed, run the following command in a Terminal window. You should see a message with information about the version of Clang you&#39;re using.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

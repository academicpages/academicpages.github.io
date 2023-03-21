<h1 data-loc-id="walkthough.mac.install.compiler">在 macOS 上安裝 C++ 編譯器</h1>
<p data-loc-id="walkthough.mac.text1">如果您執行 macOS 的 C++ 開發，建議您安裝 Clang 編譯器。您只需要在終端機視窗中執行下列命令，以安裝命令列開發人員工具:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">然後，若要確認是否已安裝 Clang，請在終端視窗中執行下列命令。您應該會看到一個訊息，其中包含您目前使用之 Clang 版本的資訊。</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

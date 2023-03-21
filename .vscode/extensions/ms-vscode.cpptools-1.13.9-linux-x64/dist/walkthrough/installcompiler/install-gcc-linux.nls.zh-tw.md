<h1 data-loc-id="walkthrough.linux.install.compiler">在 Linux 上安裝 C++ 編譯器</h1>
<p data-loc-id="walkthrough.linux.text1">如果您在執行 Linux 的 C++ 開發，建議您安裝 GCC 編譯器。安裝 GCC 很簡單，只須遵循下列三個步驟:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">從終端機視窗執行下列命令，以更新 Ubuntu 套件清單。過期的 Linux 發佈有時可能會干擾安裝新套件的嘗試。</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">使用此命令安裝 GNU 編譯器工具和 GDB 偵錯工具:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">執行下列命令，驗證 GCC 是否已安裝。您應該看到版權訊息以及您所使用之 GCC 版本的相關資訊。</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

<h1 data-loc-id="walkthrough.linux.install.compiler">在 Linux 上安装 C++ 编译器</h1>
<p data-loc-id="walkthrough.linux.text1">如果要为 Linux 进行 C++ 开发，建议安装 GCC 编译器。安装 GCC 十分简单，只需执行以下三个步骤:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">从终端窗口运行以下命令以更新 Ubuntu 包列表。过期的 Linux 分发有时会干扰尝试安装新包。</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">使用此命令安装 GNU 编译器工具和 GDB 调试器:</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">运行以下命令以验证 GCC 已安装。你应该会看到一条版权消息和有关所使用的 GCC 版本的信息。</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

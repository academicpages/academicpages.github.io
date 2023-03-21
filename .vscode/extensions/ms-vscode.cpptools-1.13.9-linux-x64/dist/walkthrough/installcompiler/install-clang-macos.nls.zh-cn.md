<h1 data-loc-id="walkthough.mac.install.compiler">在 macOS 上安装 C++ 编译器</h1>
<p data-loc-id="walkthough.mac.text1">如果要为 macOS 进行 C++ 开发，建议安装 Clang 编译器。只需在“终端”窗口中运行以下命令即可安装命令行开发人员工具:</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">然后，要验证已安装 clang，请在“终端”窗口中运行以下命令。你应该会看到一条消息，其中包含有关所使用的 Clang 版本的信息。</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

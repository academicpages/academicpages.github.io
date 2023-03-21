<h1 data-loc-id="walkthrough.linux.install.compiler">Linux で C++ コンパイラをインストールする</h1>
<p data-loc-id="walkthrough.linux.text1">Linux に C++ の開発を行う場合は、GCC コンパイラのインストールをお勧めします。GCC のインストールは簡単で、以下の 3 つの手順に従うだけです。</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">ターミナル ウィンドウで次のコマンドを実行すると、Ubuntu のパッケージ リストが更新されます。Linux ディストリビューションが以前のバージョンである場合は、新しいパッケージのインストールに支障をきたす場合があります。</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">以下のコマンドを使用して、GNU コンパイラ ツールと GDB デバッガーをインストールします。</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">次のコマンドを実行して、GCC がインストールされていることを確認します。著作権に関するメッセージと、使用している GCC のバージョンに関する情報が表示されます。</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

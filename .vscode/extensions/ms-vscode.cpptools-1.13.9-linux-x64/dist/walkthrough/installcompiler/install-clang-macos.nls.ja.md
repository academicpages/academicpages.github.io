<h1 data-loc-id="walkthough.mac.install.compiler">macOS で C++ コンパイラをインストールする</h1>
<p data-loc-id="walkthough.mac.text1">macOS 向け C++ 開発を行っている場合は、Clang コンパイラをインストールすることをお勧めします。コマンド ライン開発者ツールをインストールするのに必要な操作は、ターミナル ウィンドウで以下のコマンドを実行するだけです。</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">次に、Clang がインストールされていることを確認するために、ターミナル ウィンドウで次のコマンドを実行します。使用している Clang のバージョンに関する情報を含むメッセージが表示されます。</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

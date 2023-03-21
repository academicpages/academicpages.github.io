<h1 data-loc-id="walkthrough.windows.title.run.and.debug.your.file">Windows でお使いの C++ ファイルを実行してデバッグする</h1>
<p data-loc-id="walkthrough.windows.run.and.debug.your.file">VS Code でお使いの C++ ファイルを実行およびデバッグするには、次の操作に従います。</p>
<ol>
<li><p data-loc-id="walkthrough.windows.instructions1">実行してデバッグする C++ ソース ファイルを開きます。エディターで、このファイルがアクティブ (現在表示され、選択されている) であることを確認してください。</p>
</li>
<li><p data-loc-id="walkthrough.windows.press.f5"><code>F5</code> を押します。あるいは、メイン メニューで <strong><span data-loc-id="walkthrough.windows.run" data-loc-hint="Refers to Run command on main menu">実行</span> &gt; <span data-loc-id="walkthrough.windows.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">デバッグの開始</span></strong> を選択します。</p>
</li>
<li><p data-loc-id="walkthrough.windows.select.compiler"><strong>C++ (Windows)</strong> を選択します。</p>
</li>
<li><p data-loc-id="walkthrough.windows.choose.build.active.file"><strong>cl.exe - <span data-loc-id="walkthrough.windows.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">アクティブ ファイルのビルドとデバッグ</span></strong> を選択します。</p>
</li>
</ol>
<p data-loc-id="walkthrough.windows.after.running">C++ ファイルを最初に実行してデバッグした後、プロジェクトの <strong>.vscode</strong> フォルダーの内部に <strong>tasks.json</strong> と <strong>launch.json</strong> の 2 つの新しいファイルがあることがわかります。</p>

<p data-loc-id="walkthrough.windows.for.more.complex">より複雑なビルドとデバッグのシナリオについて、<span>tasks.json</span> と <span>launch.json</span> でビルド タスクとデバッグ設定をカスタマイズできます。たとえば、コマンド ラインでのビルド時、通常コンパイラに引数を渡す場合、<strong>compilerArgs</strong> プロパティを使用して <span>tasks.json</span> でそれらの引数を指定することができます。同様に、デバッグ時にプログラムに渡す引数を <span>launch.json</span> で定義することができます。</p>

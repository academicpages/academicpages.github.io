<h1 data-loc-id="walkthrough.linux.title.run.and.debug.your.file">在 Linux 上執行並偵錯您的 C++ 檔案</h1>
<p data-loc-id="walkthrough.linux.run.and.debug.your.file">若要在 VS Code 中執行和偵錯您的 C++ 檔案:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.instructions1">開啟您要執行及偵錯的 C++ 來源檔案。請確定此檔案在編輯器中為作用中 (目前顯示且已選取)。</p>
</li>
<li><p data-loc-id="walkthrough.linux.press.f5">按 <code>F5</code>。或者，從主功能表中選擇 <strong><span data-loc-id="walkthrough.linux.run" data-loc-hint="Refers to Run command on main menu">執行</span> &gt; <span data-loc-id="walkthrough.linux.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">開始偵錯</span></strong>。</p>
</li>
<li><p data-loc-id="walkthrough.linux.select.compiler">選取 <strong>C++ (GDB/LLDB)</strong>。</p>
</li>
<li><p data-loc-id="walkthrough.linux.choose.build.active.file">選擇 <strong>g++ - <span data-loc-id="walkthrough.linux.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">建置及偵錯使用中的檔案</span></strong>。</p>
</li>
</ol>
<p data-loc-id="walkthrough.linux.after.running">第一次執行並偵錯您的 C++ 檔案之後，您會注意到專案 <strong>.vscode</strong> 資料夾中有兩個新檔案: <strong>tasks.json</strong> 及 <strong>launch.json</strong>。</p>

<p data-loc-id="walkthrough.linux.for.more.complex">如需更複雜的組建和偵錯案例，您可以在 <span>tasks.json</span> 及 <span>launch.json</span> 中自訂群組建工作和偵錯設定。例如，如果您在從命令列組建時，通常會將引數傳遞給編譯器，可以使用 <strong>compilerArgs</strong> 屬性在 <span>tasks.json</span> 中指定這些引數。類似地，您可以定義要傳遞給程式的引數，以便在 <span>launch.json</span> 進行偵錯。</p>

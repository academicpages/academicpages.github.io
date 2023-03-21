<h1 data-loc-id="walkthrough.mac.title.run.and.debug.your.file">Esegui con debug il file C++ in macOS</h1>
<p data-loc-id="walkthrough.mac.run.and.debug.your.file">Per eseguire con debug il file C++ in VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.mac.instructions1">Aprire il file di origine C++ che si vuole eseguire con debug. Assicurarsi che il file sia attivo (attualmente visualizzato e selezionato) nell'editor.</p>
</li>
<li><p data-loc-id="walkthrough.mac.press.f5">Premere <code>F5</code>. In alternativa, scegliere <strong><span data-loc-id="walkthrough.mac.run" data-loc-hint="Refers to Run command on main menu">Esegui</span> &gt; <span data-loc-id="walkthrough.mac.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Avvia debug</span></strong> dal menu principale.</p>
</li>
<li><p data-loc-id="walkthrough.mac.select.compiler">Selezionare <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.choose.build.active.file">Scegliere <strong>clang++ - <span data-loc-id="walkthrough.mac.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Compila ed esegui il debug del file attivo</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.mac.after.running">Dopo l'esecuzione e il debug del file C++ per la prima volta, verranno rilevati due nuovi file nella cartella <strong>.vscode</strong> del progetto: <strong>tasks.json</strong> e <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.mac.for.more.complex">Per scenari di compilazione e debug più complessi, è possibile personalizzare le attività di compilazione e le configurazioni di debug in <span>tasks.json</span> e <span>launch.json</span>. Ad esempio, se durante la compilazione dalla riga di comando si passano argomenti al compilatore, è possibile specificare tali argomenti in <span>tasks.json</span> usando la proprietà <strong>compilerArgs</strong>. Analogamente, è possibile definire argomenti da passare al programma per il debug in <span>launch.json</span>.</p>

<h1 data-loc-id="walkthrough.mac.title.run.and.debug.your.file">Uruchom i debuguj plik C++ w systemie macOS</h1>
<p data-loc-id="walkthrough.mac.run.and.debug.your.file">Aby uruchomić i debugować plik C++ w programie VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.mac.instructions1">Otwórz plik źródłowy języka C++, który chcesz uruchomić i debugować. Upewnij się, że ten plik jest aktywny (obecnie wyświetlany i zaznaczony) w edytorze.</p>
</li>
<li><p data-loc-id="walkthrough.mac.press.f5">Naciśnij pozycję <code>F5</code>. Ewentualnie z menu głównego wybierz pozycję <strong><span data-loc-id="walkthrough.mac.run" data-loc-hint="Refers to Run command on main menu">Uruchom</span> &gt; <span data-loc-id="walkthrough.mac.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Rozpocznij debugowanie</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.select.compiler">Wybierz kompilator <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.choose.build.active.file">Wybierz kompilację <strong>clang++ - <span data-loc-id="walkthrough.mac.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Kompiluj i debuguj aktywny plik</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.mac.after.running">Po uruchomieniu i debugowaniu pliku C++ po raz pierwszy zobaczysz dwa nowe pliki w folderze <strong>.vscode</strong> projektu: <strong>tasks.json</strong> i <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.mac.for.more.complex">W przypadku bardziej złożonych scenariuszy kompilacji i debugowania można dostosować zadania kompilacji i konfiguracje debugowania w pozycjach <span>tasks.json</span> i <span>launch.json</span>. Na przykład jeśli zwykle przekazujesz argumenty do kompilatora podczas kompilowania z poziomu wiersza polecenia, możesz określić te argumenty w pozycji<span>tasks.json</span> przy użyciu właściwości <strong>compilerArgs</strong>. Podobnie można zdefiniować argumenty do przekazania do programu na potrzeby debugowania w pozycji<span>launch.json</span>.</p>

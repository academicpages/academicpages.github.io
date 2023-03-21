<h1 data-loc-id="walkthrough.windows.install.compiler">Zainstaluj kompilator języka C++ w systemie Windows</h1>
<p data-loc-id="walkthrough.windows.text1">Jeśli programujesz w języku C++ dla systemu Windows, zalecamy zainstalowanie zestawu narzędzi kompilatora Microsoft Visual C++ (MSVC). Jeśli korzystasz z systemu Linux z systemu Windows, zapoznaj się z <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Używanie języka C++ i podsystemu Windows dla systemu Linux (WSL) w programie VS Code</a>. Możesz też <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">Zainstaluj zestaw kompilatorów GCC w systemie Windows z funkcją MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Aby zainstalować program MSVC, pobierz <strong data-loc-id="walkthrough.windows.build.tools1">Build Tools for Visual Studio 2019</strong> ze strony programu Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Pliki do pobrania</a>.</p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">W instalatorze programu Visual Studio sprawdź obciążenie <strong data-loc-id="walkthrough.windows.build.tools2">Narzędzia kompilacji języka C++</strong> i wybierz pozycję <strong data-loc-id="walkthrough.windows.link.install">Zainstaluj</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Uwaga</strong>: <span data-loc-id="walkthrough.windows.note1.text">Zestawu narzędzi języka C++ z narzędzi Visual Studio Build Tools wraz z programem Visual Studio Code można używać do kompilowania, tworzenia i weryfikowania dowolnej bazy kodu języka C++, o ile masz również ważną licencję programu Visual Studio (Community, Pro lub Enterprise), której aktywnie używasz do opracowywania tej bazy kodu języka C++.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Otwórz pozycję <strong data-loc-id="walkthrough.windows.command.prompt.name1">Wiersz polecenia dla deweloperów dla programu VS</strong>, wpisując „deweloper” w menu Start systemu Windows.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Sprawdź instalację programu MSVC, wpisując <code>cl</code> w wierszu polecenia dewelopera dla programu VS. Powinien zostać wyświetlony komunikat o prawach autorskich z wersją i opisem użycia podstawowego.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Uwaga</strong>: <span data-loc-id="walkthrough.windows.note2.text">Aby użyć programu MSVC z wiersza polecenia lub programu VS Code, należy uruchomić z <strong data-loc-id="walkthrough.windows.command.prompt.name2">Wiersz polecenia dla deweloperów dla programu VS</strong>. Zwykła powłoka, taka jak <span>PowerShell</span>, <span>Bash</span> lub wiersz polecenia systemu Windows, nie ma ustawionych wymaganych zmiennych środowiskowych ścieżki.</span></p>
</blockquote>
</li>
</ol>

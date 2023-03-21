<h1 data-loc-id="walkthrough.windows.install.compiler">C++-Compiler unter Windows installieren</h1>
<p data-loc-id="walkthrough.windows.text1">Wenn Sie mithilfe von C++ unter Windows entwickeln, empfehlen wir die Installation des Microsoft Visual C++-Compiler-Toolsets (MSVC). Wenn Sie Linux aus Windows verwenden, lesen Sie <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Verwenden von C++ und Windows-Subsystem für Linux (WSL) in VS Code</a>. Oder Sie können <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">Installieren Sie GCC unter Windows mit MinGW.</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Um MSVC zu installieren, laden Sie <strong data-loc-id="walkthrough.windows.build.tools1">Buildtools für Visual Studio 2019</strong> von der Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Downloads</a>-Seite herunter. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">Überprüfen Sie im Visual Studio-Installer den <strong data-loc-id="walkthrough.windows.build.tools2">C++-Buildtools</strong> Workload, und wählen Sie <strong data-loc-id="walkthrough.windows.link.install">Installieren</strong> aus.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Hinweis</strong>: <span data-loc-id="walkthrough.windows.note1.text">Sie können das C++-Toolset aus Visual Studio Build Tools zusammen mit Visual Studio Code zum Kompilieren, Erstellen und Überprüfen von C++-Codebasis verwenden, sofern Sie auch über eine gültige Visual Studio-Lizenz (Community, Pro oder Enterprise) verfügen, die Sie aktiv zum Entwickeln dieser C++-Codebasis verwenden.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Öffnen Sie die <strong data-loc-id="walkthrough.windows.command.prompt.name1">Developer-Eingabeaufforderung für VS</strong>, indem Sie im Windows-Startmenü "Developer" eingeben.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Überprüfen Sie die MSVC-Installation, indem Sie <code>cl</code> in die Developer-Eingabeaufforderung für VS eingeben. Es sollten ein Copyrighthinweis mit der Version und der grundlegenden Nutzungsbeschreibung angezeigt werden.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Hinweis</strong>: <span data-loc-id="walkthrough.windows.note2.text">Um MSVC mithilfe der Befehlszeile oder mit VS Code zu verwenden, müssen Sie von einem <strong data-loc-id="walkthrough.windows.command.prompt.name2">Developer-Eingabeaufforderung für VS</strong> aus ausführen. Für eine normale Shell wie <span>PowerShell</span>, <span>Bash</span> oder die Windows-Eingabeaufforderung sind die erforderlichen PATH-Umgebungsvariablen nicht festgelegt.</span></p>
</blockquote>
</li>
</ol>

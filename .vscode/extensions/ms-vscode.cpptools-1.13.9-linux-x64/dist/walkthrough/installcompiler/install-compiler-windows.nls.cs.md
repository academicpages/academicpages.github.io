<h1 data-loc-id="walkthrough.windows.install.compiler">Instalace kompilátoru jazyka C++ v systému Windows</h1>
<p data-loc-id="walkthrough.windows.text1">Pokud provádíte vývoj C++ pro Windows, doporučujeme nainstalovat sadu nástrojů kompilátoru Microsoft Visual C++ (MSVC). Pokud cílíte na Linux z Windows, podívejte se na <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Použití C++ a subsystému Windows pro Linux (WSL) ve VS Code</a>. Nebo můžete <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">instalovat GCC na Windows pomocí MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Pokud chcete nainstalovat MSVC, stáhněte <strong data-loc-id="walkthrough.windows.build.tools1">Build Tools for Visual Studio 2019</strong> ze stránky Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Položky ke stažení</a>.</p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">V Instalační program pro Visual Studio zkontrolujte <strong data-loc-id="walkthrough.windows.build.tools2">C++ Build Tools</strong> úlohy a vyberte <strong data-loc-id="walkthrough.windows.link.install">Nainstalovat</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Poznámka</strong>: <span data-loc-id="walkthrough.windows.note1.text">Můžete použít sadu nástrojů C++ z Visual Studio Build Tools spolu s Visual Studio Code ke kompilaci, sestavení a ověření jakékoli kódové báze C++, pokud máte také platnou licenci Visual Studio (buď Community, Pro nebo Enterprise), kterou aktivně používáte k vývoji kódové báze C++.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Otevřete <strong data-loc-id="walkthrough.windows.command.prompt.name1">Developer Command Prompt for VS</strong> zadáním příkazu „developer“ do nabídky Start systému Windows.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">MSVC instalaci zkontrolujte tak, že zadáte <code>cl</code> do Developer Command Prompt for VS. Měla by se zobrazit zpráva o autorských právech v popisu verze a základního použití.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Poznámka</strong>: <span data-loc-id="walkthrough.windows.note2.text">Pokud chcete použít MSVC z příkazového řádku nebo VS Code, musíte spouštět z <strong data-loc-id="walkthrough.windows.command.prompt.name2">Developer Command Prompt for VS</strong>. Běžné prostředí, jako je <span>PowerShell</span>, <span>Bash</span> nebo příkazový řádek Windows, nemá nastavenou nezbytnou proměnnou prostředí cesty.</span></p>
</blockquote>
</li>
</ol>

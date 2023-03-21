<h1 data-loc-id="walkthrough.windows.install.compiler">Install a C++ compiler on Windows</h1>
<p data-loc-id="walkthrough.windows.text1">If you&#39;re doing C++ development for Windows, we recommend installing the Microsoft Visual C++ (MSVC) compiler toolset. If you&#39;re targeting Linux from Windows, check out <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Using C++ and Windows Subsystem for Linux (WSL) in VS Code</a>. Or, you could <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">install GCC on Windows with MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">To install MSVC, download <strong data-loc-id="walkthrough.windows.build.tools1">Build Tools for Visual Studio 2019</strong> from the Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Downloads</a> page. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">In the Visual Studio Installer, check the <strong data-loc-id="walkthrough.windows.build.tools2">C++ build tools</strong> workload and select <strong data-loc-id="walkthrough.windows.link.install">Install</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Note</strong>: <span data-loc-id="walkthrough.windows.note1.text">You can use the C++ toolset from Visual Studio Build Tools along with Visual Studio Code to compile, build, and verify any C++ codebase as long as you also have a valid Visual Studio license (either Community, Pro, or Enterprise) that you are actively using to develop that C++ codebase.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Open the <strong data-loc-id="walkthrough.windows.command.prompt.name1">Developer Command Prompt for VS</strong> by typing &#39;developer&#39; in the Windows Start menu.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Check your MSVC installation by typing <code>cl</code> into the Developer Command Prompt for VS. You should see a copyright message with the version and basic usage description.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Note</strong>: <span data-loc-id="walkthrough.windows.note2.text">To use MSVC from the command line or VS Code, you must run from a <strong data-loc-id="walkthrough.windows.command.prompt.name2">Developer Command Prompt for VS</strong>. An ordinary shell such as <span>PowerShell</span>, <span>Bash</span>, or the Windows command prompt does not have the necessary path environment variables set.</span></p>
</blockquote>
</li>
</ol>

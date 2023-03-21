<h1 data-loc-id="walkthrough.windows.install.compiler">在 Windows 上安裝 C++ 編譯器</h1>
<p data-loc-id="walkthrough.windows.text1">如果您正在執行 Windows 的 C++ 開發，建議您安裝 Microsoft Visual C++ (MSVC) 編譯器工具組。如果您是以 Windows 的 Linux 為目標，請查看 <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">在 VS Code 中使用 C++ 與 Windows 子系統 Linux 版 (WSL) </a>。或者，您也可以 <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">使用 MinGW 在 Windows 安裝 GCC</a>。</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">若要安裝 MSVC，請 <strong data-loc-id="walkthrough.windows.build.tools1">Build Tools for Visual Studio 2019</strong>從 Visual Studio<a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">下載</a> 頁面下載。</p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">在 Visual Studio 安裝程式中，檢查 <strong data-loc-id="walkthrough.windows.build.tools2">C++ 組建工具</strong> 工作負載，然後選取 <strong data-loc-id="walkthrough.windows.link.install">安裝</strong>。</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">備註</strong>: <span data-loc-id="walkthrough.windows.note1.text">您可以使用 Visual Studio Build Tools 中的 C++ 工具組以及 Visual Studio Code 來編譯、組建及驗證任何 C++ 程式碼基底，只要您也擁有有效的 Visual Studio 授權 (社群版、專業版或企業版)，且您正積極開發該 C++ 程式碼基底。</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">在 Windows 開始頁面功能表中鍵入「開發人員」，以開啟 <strong data-loc-id="walkthrough.windows.command.prompt.name1">VS 的開發人員命令提示</strong>。</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">在 VS 的開發人員命令提示字元中輸入 <code>cl</code>，以檢查您的 MSVC 安裝。您應該會看到内附版本及基本使用說明的著作權訊息。</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">備註</strong>: <span data-loc-id="walkthrough.windows.note2.text">若要從命令列或 VS Code 使用 MSVC，您必須從 <strong data-loc-id="walkthrough.windows.command.prompt.name2">VS 的開發人員命令提示</strong> 執行。一般殼層，例如 <span>PowerShell</span>、<span>Bash</span> 或 Windows 命令提示字元，沒有設定必要的路徑環境變數集。</span></p>
</blockquote>
</li>
</ol>

<h1 data-loc-id="walkthrough.windows.install.compiler">在 Windows 上安装 C++ 编译器</h1>
<p data-loc-id="walkthrough.windows.text1">如果要对 Windows 进行 C++ 开发，建议安装Microsoft Visual C++ (MSVC)编译器工具集。如果从 Windows 面向 Linux，请检查 <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">在 VS Code 中使用 C++ 和 适用于 Linux 的 Windows 子系统(WSL)</a>，或可以 <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">在带 MinGW 的 Windows 上安装 GCC</a>。</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">要安装 MSVC，请从 Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">下载</a> 页面下载 <strong data-loc-id="walkthrough.windows.build.tools1">Visual Studio 2019 生成工具</strong>。</p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">在 Visual Studio 安装程序中，检查 <strong data-loc-id="walkthrough.windows.build.tools2">C++ 生成工具</strong> 工作负载并选择 <strong data-loc-id="walkthrough.windows.link.install">安装</strong>。</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">注意</strong>: <span data-loc-id="walkthrough.windows.note1.text">可以使用 Visual Studio 生成工具中的 C++ 工具集以及 Visual Studio Code 以编译、生成并验证任何 C++ 代码库，前提是同时具有有效的 Visual Studio 许可证(社区版、专业版或企业版)，且正积极将其用于开发该 C++ 代码库。</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">在 Windows“开始”菜单中键入‘开发人员’以打开 <strong data-loc-id="walkthrough.windows.command.prompt.name1">VS 的开发人员命令提示</strong>。</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">在 VS 的开发人员命令提示中键入 <code>cl</code> 以检查 MSVC 安装。你应该会看到包含版本和基本使用情况说明的版权消息。</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">注意</strong>: <span data-loc-id="walkthrough.windows.note2.text">要从命令行或 VS Code 使用 MSVC，必须从 <strong data-loc-id="walkthrough.windows.command.prompt.name2">VS 的开发人员命令提示</strong> 运行。普通 shell (例如 <span>PowerShell</span>、 <span>Bash</span>)或 Windows 命令提示符未设置必要的路径环境变量。</span></p>
</blockquote>
</li>
</ol>

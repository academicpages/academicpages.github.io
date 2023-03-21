<h1 data-loc-id="walkthrough.mac.title.run.and.debug.your.file">在 macOS 上运行并调试 C++ 文件</h1>
<p data-loc-id="walkthrough.mac.run.and.debug.your.file">要在 VS Code 中运行并调试 C++ 文件:</p>
<ol>
<li><p data-loc-id="walkthrough.mac.instructions1">打开要运行和调试的 C++ 源文件。请确保此文件在编辑器中处于活动状态(当前已显示并选择)。</p>
</li>
<li><p data-loc-id="walkthrough.mac.press.f5">按 <code>F5</code>，或从主菜单中选择 <strong><span data-loc-id="walkthrough.mac.run" data-loc-hint="Refers to Run command on main menu">运行</span> &gt; <span data-loc-id="walkthrough.mac.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">开始调试</span></strong>。</p>
</li>
<li><p data-loc-id="walkthrough.mac.select.compiler">选择 <strong>C++ (GDB/LLDB)</strong>。</p>
</li>
<li><p data-loc-id="walkthrough.mac.choose.build.active.file">选择 <strong>clang++ - <span data-loc-id="walkthrough.mac.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">生成和调试活动文件</span></strong>。</p>
</li>
</ol>
<p data-loc-id="walkthrough.mac.after.running">首次运行和调试 C++ 文件后，你将注意到项目 <strong>.vscode</strong> 的文件夹内有两个新文件: <strong>tasks.json</strong> 和 <strong>launch.json</strong>。</p>

<p data-loc-id="walkthrough.mac.for.more.complex">对于更复杂的生成和调试场景，可以在 <span>tasks.json</span> 和 <span>launch.json</span> 中自定义生成任务和调试配置。例如，如果在从命令行生成时通常会将参数传递给编译器，则可以使用 <strong>compilerArgs</strong> 属性以在 <span>tasks.json</span> 中指定这些参数。同样，可以定义要传递给程序的参数，以在 <span>launch.json</span>中进行调试。</p>

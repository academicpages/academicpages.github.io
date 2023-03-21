<h1 data-loc-id="walkthrough.mac.title.run.and.debug.your.file">Run and debug your C++ file on macOS</h1>
<p data-loc-id="walkthrough.mac.run.and.debug.your.file">To run and debug your C++ file in VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.mac.instructions1">Open the C++ source file that you want to run and debug. Make sure this file is active (currently displayed and selected) in the editor.</p>
</li>
<li><p data-loc-id="walkthrough.mac.press.f5">Press <code>F5</code>. Or, from the main menu, choose <strong><span data-loc-id="walkthrough.mac.run" data-loc-hint="Refers to Run command on main menu">Run</span> &gt; <span data-loc-id="walkthrough.mac.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Start Debugging</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.select.compiler">Select <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.choose.build.active.file">Choose <strong>clang++ - <span data-loc-id="walkthrough.mac.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Build and debug active file</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.mac.after.running">After running and debugging your C++ file for the first time, you&#39;ll notice two new files inside your project&#39;s <strong>.vscode</strong> folder: <strong>tasks.json</strong> and <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.mac.for.more.complex">For more complex build and debug scenarios, you can customize your build tasks and debug configurations in <span>tasks.json</span> and <span>launch.json</span>. For example, if you normally pass arguments to your compiler when building from the command line, you can specify those arguments in <span>tasks.json</span> using the <strong>compilerArgs</strong> property. Similarly, you can define arguments to pass to your program for debugging in <span>launch.json</span>.</p>

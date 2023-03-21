<h1 data-loc-id="walkthrough.linux.title.run.and.debug.your.file">Executar e depurar seu arquivo C++ no Linux</h1>
<p data-loc-id="walkthrough.linux.run.and.debug.your.file">Para executar e depurar seu arquivo C++ no VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.instructions1">Abra o arquivo de origem C++ que você deseja executar e depurar. Certifique-se de que este arquivo esteja ativo (atualmente exibido e selecionado) no editor.</p>
</li>
<li><p data-loc-id="walkthrough.linux.press.f5">Pressione <code>F5</code>. Ou, no menu principal, escolha <strong><span data-loc-id="walkthrough.linux.run" data-loc-hint="Refers to Run command on main menu">Executar</span> &gt; <span data-loc-id="walkthrough.linux.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Iniciar Depuração</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.linux.select.compiler">Selecione <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.linux.choose.build.active.file">Escolha <strong>g++ - <span data-loc-id="walkthrough.linux.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Criar e depurar o arquivo ativo</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.linux.after.running">Depois de executar e depurar seu arquivo C++ pela primeira vez, você notará dois novos arquivos dentro da pasta <strong>.vscode</strong> do seu projeto: <strong>tasks.json</strong> e <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.linux.for.more.complex">Para cenários de compilação e depuração mais complexos, você pode personalizar suas tarefas de compilação e configurações de depuração em <span>tasks.json</span> e <span>launch.json</span>. Por exemplo, se você normalmente passa argumentos para seu compilador ao compilar a partir da linha de comando, você pode especificar esses argumentos em <span>tasks.json</span> usando a propriedade <strong>compilerArgs</strong>. Da mesma forma, você pode definir argumentos para passar para seu programa para depuração em <span>launch.json</span>.</p>

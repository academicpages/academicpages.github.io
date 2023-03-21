<h1 data-loc-id="walkthrough.mac.title.run.and.debug.your.file">Spusťte a nalaďte soubor C++ v systému macOS</h1>
<p data-loc-id="walkthrough.mac.run.and.debug.your.file">Pokud chcete spustit a ladit váš soubor C++ ve VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.mac.instructions1">Otevřete zdrojový soubor C++, který chcete spustit a ladit. Ujistěte se, že je tento soubor aktivní (aktuálně zobrazený a vybraný) v editoru.</p>
</li>
<li><p data-loc-id="walkthrough.mac.press.f5">Stiskněte klávesu <code>F5</code>. Nebo v hlavní nabídce zvolte <strong><span data-loc-id="walkthrough.mac.run" data-loc-hint="Refers to Run command on main menu">Spustit</span> &gt; <span data-loc-id="walkthrough.mac.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Spustit ladění</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.select.compiler">Vyberte <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.mac.choose.build.active.file">Zvolte <strong>clang++ - <span data-loc-id="walkthrough.mac.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Sestavit a ladit aktivní soubor</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.mac.after.running">Po prvním spuštění a ladění vašeho souboru C++ si všimnete dvou nových souborů ve složce projektu <strong>.vscode</strong>: <strong>tasks.json</strong> a <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.mac.for.more.complex">Pro složitější scénáře sestavení a ladění můžete přizpůsobit úlohy sestavení a konfigurace ladění v <span>tasks.json</span> a <span>launch.json</span>. Například, pokud obvykle předáváte argumenty kompilátoru při sestavování z příkazového řádku, můžete zadat tyto argumenty v <span>tasks.json</span> pomocí vlastnosti <strong>compilerArgs</strong>. Podobně můžete definovat argumenty, které budou předány vašemu programu pro ladění v <span>launch.json</span>.</p>

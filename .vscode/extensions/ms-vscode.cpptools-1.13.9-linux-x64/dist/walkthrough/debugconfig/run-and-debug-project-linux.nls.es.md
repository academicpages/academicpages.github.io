<h1 data-loc-id="walkthrough.linux.title.run.and.debug.your.file">Ejecución y depuración del archivo de C++ en Linux</h1>
<p data-loc-id="walkthrough.linux.run.and.debug.your.file">Para ejecutar y depurar el archivo de C++ en VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.linux.instructions1">Abra el archivo de origen de C++ que desea ejecutar y depurar. Asegúrese de que este archivo esté activo (que se muestre y esté seleccionado en el momento) en el editor.</p>
</li>
<li><p data-loc-id="walkthrough.linux.press.f5">Presione <code>F5</code>. O bien, en el menú principal, elija <strong><span data-loc-id="walkthrough.linux.run" data-loc-hint="Refers to Run command on main menu">Ejecutar</span> &gt; <span data-loc-id="walkthrough.linux.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Iniciar depuración</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.linux.select.compiler">Seleccionar <strong>C++ (GDB/LLDB)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.linux.choose.build.active.file">Elija <strong>g++ - <span data-loc-id="walkthrough.linux.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Compilar y depurar el archivo activo</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.linux.after.running">Después de ejecutar y depurar el archivo de C++ por primera vez, observará dos archivos nuevos dentro del folder <strong>.vscode</strong> del proyecto: <strong>tasks.json</strong> y <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.linux.for.more.complex">Para escenarios de compilación y depuración más complejos, puede personalizar las tareas de compilación y las configuraciones de depuración en <span>tasks.json</span> y <span>launch.json</span>. Por ejemplo, si, por lo general, pasa argumentos al compilador al compilar desde la línea de comandos, puede especificar esos argumentos en <span>tasks.json</span> usando la propiedad <strong>compilerArgs</strong>. Del mismo modo, puede definir argumentos para pasar al programa para la depuración en <span>launch.json</span>.</p>

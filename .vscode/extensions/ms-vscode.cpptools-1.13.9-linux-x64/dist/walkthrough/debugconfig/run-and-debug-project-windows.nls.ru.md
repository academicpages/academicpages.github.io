<h1 data-loc-id="walkthrough.windows.title.run.and.debug.your.file">Запуск и отладка файла C++ в Windows</h1>
<p data-loc-id="walkthrough.windows.run.and.debug.your.file">Запуск и отладка файла C++ в VS Code:</p>
<ol>
<li><p data-loc-id="walkthrough.windows.instructions1">Откройте файл исходного кода C++, который необходимо запустить и отладить. Убедитесь, что этот файл активен (в настоящий момент отображается и выделен) в редакторе.</p>
</li>
<li><p data-loc-id="walkthrough.windows.press.f5">Нажмите <code>F5</code> или выберите <strong><span data-loc-id="walkthrough.windows.run" data-loc-hint="Refers to Run command on main menu">Запустить</span> &gt; <span data-loc-id="walkthrough.windows.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Начать отладку</span></strong> в главном меню.</p>
</li>
<li><p data-loc-id="walkthrough.windows.select.compiler">Выберите <strong>C++ (Windows)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.windows.choose.build.active.file">Выберите <strong>cl.exe - <span data-loc-id="walkthrough.windows.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Сборка и отладка активного файла</span></strong>.</p>
</li>
</ol>
<p data-loc-id="walkthrough.windows.after.running">После первого запуска и отладки вашего файла C++ вы увидите два новых файла в папке проекта <strong>.vscode</strong>: <strong>tasks.json</strong> и <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.windows.for.more.complex">Для более сложных сценариев сборки и отладки можно настроить ваши задачи сборки и конфигурации отладки в <span>tasks.json</span> и <span>launch.json</span>. Например, если обычно вы передаете аргументы в компилятор при сборке из командной строки, можно указать эти аргументы в <span>tasks.json</span> с помощью свойств <strong>compilerArgs</strong>. Аналогичным образом можно определить передаваемые программе аргументы для отладки в <span>launch.json</span>.</p>

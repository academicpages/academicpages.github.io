<h1 data-loc-id="walkthrough.windows.install.compiler">Установка компилятора C++ в Windows</h1>
<p data-loc-id="walkthrough.windows.text1">Если вы занимаетесь разработкой на C++ для Windows, рекомендуем установить набор инструментов компилятора Microsoft Visual C++ (MSVC). Если вы разрабатываете решения для Linux в Windows, попробуйте использовать <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Использование C++ и подсистемы Windows для Linux в VS Code</a> или <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">Установка GCC в Windows с помощью MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Чтобы установить MSVC, скачайте <strong data-loc-id="walkthrough.windows.build.tools1">Build&nbsp;Tools для Visual Studio&nbsp;2019</strong> со страницы Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Загрузки</a>. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">В Visual Studio Installer выберите рабочую нагрузку <strong data-loc-id="walkthrough.windows.build.tools2">Средства сборки C++</strong> и выберите <strong data-loc-id="walkthrough.windows.link.install">Установка</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Примечание</strong>: <span data-loc-id="walkthrough.windows.note1.text">Вы можете использовать набор инструментов C++ из пакета Visual Studio Build Tools вместе с Visual Studio Code для компиляции, сборки и проверки любой базы кода C++, если у вас есть действующая лицензия Visual Studio (Community, Pro или Enterprise), которой вы активно пользуетесь для разработки этой базы кода C++.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Откройте <strong data-loc-id="walkthrough.windows.command.prompt.name1">Командная строка разработчика для VS</strong>, введя команду "developer" в меню "Пуск" в Windows.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Проверьте установку MSVC, введя <code>cl</code> в командной строке разработчика для VS. Должно появиться сообщение об авторских правах с номером версии и кратким описанием использования.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Примечание</strong>: <span data-loc-id="walkthrough.windows.note2.text">Чтобы использовать MSVC из командной строки или VS Code, требуется запуск из <strong data-loc-id="walkthrough.windows.command.prompt.name2">Командная строка разработчика для VS</strong>. В обычной среде, например в <span>PowerShell</span>, в <span>Bash</span> или в командной строке Windows, не заданы необходимые переменные среды "path".</span></p>
</blockquote>
</li>
</ol>

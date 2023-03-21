<h1 data-loc-id="walkthrough.windows.title.run.and.debug.your.file">Windows에서 C++ 파일 실행 및 디버그</h1>
<p data-loc-id="walkthrough.windows.run.and.debug.your.file">VS Code에서 C++ 파일을 실행하고 디버그하려면:</p>
<ol>
<li><p data-loc-id="walkthrough.windows.instructions1">실행하고 디버그할 C++ 원본 파일을 엽니다. 이 파일이 편집기에서 활성화되어 있는지(현재 표시되고 선택되어 있는지) 확인하세요.</p>
</li>
<li><p data-loc-id="walkthrough.windows.press.f5"><code>F5</code>을(를) 누릅니다. 또는 기본 메뉴에서 <strong><span data-loc-id="walkthrough.windows.run" data-loc-hint="Refers to Run command on main menu">실행</span> &gt; <span data-loc-id="walkthrough.windows.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">디버깅 시작</span></strong>을(를) 선택합니다.</p>
</li>
<li><p data-loc-id="walkthrough.windows.select.compiler"><strong>C++ (Windows)</strong>을(를) 선택합니다.</p>
</li>
<li><p data-loc-id="walkthrough.windows.choose.build.active.file"><strong>cl.exe - <span data-loc-id="walkthrough.windows.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">활성 파일 빌드 및 디버그</span></strong>을(를) 선택합니다.</p>
</li>
</ol>
<p data-loc-id="walkthrough.windows.after.running">처음으로 C++ 파일을 실행하고 디버깅한 후 프로젝트의 <strong>.vscode</strong> 폴더 안에 <strong>tasks.json</strong> 및 <strong>launch.json</strong>(이)라는 두 개의 새 파일이 있음을 알 수 있습니다.</p>

<p data-loc-id="walkthrough.windows.for.more.complex">더 복잡한 빌드 및 디버그 시나리오의 경우 <span>tasks.json</span> 및 <span>launch.json</span>에서 빌드 작업 및 디버그 구성을 사용자 지정할 수 있습니다. 예를 들어 명령줄에서 빌드할 때 일반적으로 컴파일러에 인수를 전달하는 경우 <strong>compilerArgs</strong> 속성을 사용하여 <span>tasks.json</span>에서 해당 인수를 지정할 수 있습니다. 마찬가지로 <span>launch.json</span>에서 디버깅을 위해 프로그램에 전달할 인수를 정의할 수 있습니다.</p>

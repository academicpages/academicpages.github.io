<h1 data-loc-id="walkthrough.windows.install.compiler">Windows에 C++ 컴파일러 설치</h1>
<p data-loc-id="walkthrough.windows.text1">Windows용 C++ 개발을 수행하는 경우 MSVC(Microsoft Visual C++) 컴파일러 도구 집합을 설치하는 것이 좋습니다. Windows에서 Linux를 대상으로 하는 경우 <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">VS Code에서 C++ 및 Linux용 Windows 하위 시스템(WSL) 사용</a>을(를) 확인하세요. 또는 <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">MinGW로 Windows에 GCC 설치</a>할 수 있습니다.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">MSVC를 설치하려면 Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">다운로드</a> 페이지에서 <strong data-loc-id="walkthrough.windows.build.tools1">Visual Studio 2019용 Build Tools</strong>을(를) 다운로드합니다.</p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">Visual Studio 설치 프로그램에서 <strong data-loc-id="walkthrough.windows.build.tools2">C++ 빌드 도구</strong> 워크로드를 확인하고 <strong data-loc-id="walkthrough.windows.link.install">설치</strong>을(를) 선택합니다.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">메모</strong>: <span data-loc-id="walkthrough.windows.note1.text">현재 C++ 코드베이스를 개발하는 데 적극적으로 사용 중인 유효한 Visual Studio 라이선스(Community, Pro 또는 Enterprise)가 있는 한 Visual Studio Build Tools의 C++ 도구 집합을 Visual Studio Code와 함께 사용하여 모든 C++ 코드베이스를 컴파일, 빌드 및 확인할 수 있습니다.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Windows 시작 메뉴에서 '개발자'를 입력하여 <strong data-loc-id="walkthrough.windows.command.prompt.name1">VS용 개발자 명령 프롬프트</strong>을(를) 엽니다.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">VS용 개발자 명령 프롬프트에 <code>cl</code>을(를) 입력하여 MSVC 설치를 확인합니다. 버전 및 기본 사용 설명과 함께 저작권 메시지가 표시되어야 합니다.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">메모</strong>: <span data-loc-id="walkthrough.windows.note2.text">명령줄 또는 VS Code에서 MSVC를 사용하려면 <strong data-loc-id="walkthrough.windows.command.prompt.name2">VS용 개발자 명령 프롬프트</strong>에서 실행해야 합니다. <span>PowerShell</span>, <span>Bash</span> 또는 Windows 명령 프롬프트와 같은 일반 셸에는 필요한 경로 환경 변수가 설정되어 있지 않습니다.</span></p>
</blockquote>
</li>
</ol>

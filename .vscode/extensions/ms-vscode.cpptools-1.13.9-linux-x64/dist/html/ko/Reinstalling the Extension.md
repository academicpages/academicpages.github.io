<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">호환되지 않거나 일치하지 않는 C/C++ 확장 이진 파일</h1>

<p data-loc-id="incompat.extension.text1">C/C++ 확장에는 기본 이진 파일이 포함되어 있습니다.</p>

<p data-loc-id="incompat.extension.text2">VS Code의 마켓플레이스 UI를 통해 설치하는 경우 올바른 기본 이진 파일이 포함되어야 합니다. 호환되지 않는 이진 파일이 감지되고 C/C++ 확장이 VS Code의 마켓플레이스 UI를 통해 설치된 경우 <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">문제를 보고하세요</a>.</p>

<h1 data-loc-id="reinstalling.extension.heading">C/C++ 확장 다시 설치</h1>

<p data-loc-id="reinstall.extension.text1">동등한 버전의 확장을 다시 설치할 때 VS Code는 기존 확장 디렉터리를 재사용할 수 있습니다. C/C++ 확장을 다시 설치할 때 이러한 문제가 발생하지 않도록 하려면 먼저 기존 확장 디렉터리를 삭제해야 할 수 있습니다.</p>

<p data-loc-id="reinstall.extension.text2">설치된 확장 디렉터리는 사용자 디렉터리 아래의 다음 경로 중 하나에서 찾을 수 있습니다(Windows의 경우 `%USERPROFILE%`, Linux 및 macOS의 경우 `$HOME`).</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">원격 연결에서:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">설치된 C/C++ 확장 디렉터리의 경로 예:</p>

<p data-loc-id="reinstall.extension.text5">Windows에서:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">Linux에서:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">그런 다음 VS Code의 마켓플레이스 UI를 통해 다시 설치합니다.</p>

<p data-loc-id="reinstall.extension.text8">확장 프로그램의 올바른 버전이 VS Code에 의해 배포되지 않으면 시스템에 올바른 VSIX가 <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">VS Code 마켓플레이스 웹 사이트에서 다운로드</a>일 수 있고 VS Code의 마켓플레이스 UI의 '...' 메뉴 아래 'VSIX에서 설치...' 옵션을 사용하여 설치할 수 있습니다.</p>
</body></html>
<h1 data-loc-id="walkthrough.linux.install.compiler">Linux에 C++ 컴파일러 설치</h1>
<p data-loc-id="walkthrough.linux.text1">Linux용 C++ 개발을 하는 경우 GCC 컴파일러를 설치하는 것이 좋습니다. GCC 설치 작업은 간단합니다. 다음 세 단계를 따르세요.</p>
<ol>
<li><p data-loc-id="walkthrough.linux.text2">터미널 창에서 다음 명령을 실행하여 Ubuntu 패키지 목록을 업데이트합니다. 구식 Linux 배포판은 경우에 따라 새 패키지를 설치하려는 시도에 방해가 될 수 있습니다.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-built_in">get</span> <span class="hljs-keyword">update</span>
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text3">다음 명령을 사용하여 GNU 컴파일러 도구와 GDB 디버거를 설치하세요.</p>
<pre><code class="lang-bash"> sudo apt-<span class="hljs-meta">get</span> install <span class="hljs-keyword">build-essential </span>gdb
</code></pre>
</li>
<li><p data-loc-id="walkthrough.linux.text4">다음 명령을 실행하여 GCC가 설치되었는지 확인합니다. 사용 중인 GCC 버전에 대한 저작권 메시지와 정보가 표시되어야 합니다.</p>
<pre><code class="lang-bash"> gcc <span class="hljs-comment">--version</span>
</code></pre>
</li>
</ol>

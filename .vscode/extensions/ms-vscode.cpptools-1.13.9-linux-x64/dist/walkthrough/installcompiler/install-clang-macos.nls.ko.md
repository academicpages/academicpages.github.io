<h1 data-loc-id="walkthough.mac.install.compiler">macOS에 C++ 컴파일러 설치</h1>
<p data-loc-id="walkthough.mac.text1">macOS용 C++ 개발을 하는 경우 Clang 컴파일러를 설치하는 것이 좋습니다. 터미널 창에서 다음 명령을 실행하여 명령줄 개발자 도구를 설치하기만 하면 됩니다.</p>
<pre><code class="lang-bash">xcode-<span class="hljs-keyword">select</span> <span class="hljs-comment">--install</span>
</code></pre>
<p data-loc-id="walkthough.mac.text2">그런 다음 Clang이 설치되었는지 확인하려면 터미널 창에서 다음 명령을 실행합니다. 사용 중인 Clang 버전에 대한 정보가 포함된 메시지가 표시되어야 합니다.</p>
<pre><code class="lang-bash">clang <span class="hljs-comment">--version</span>
</code></pre>

<h1 data-loc-id="walkthrough.windows.install.compiler">Instalar um compilador C++ no Windows</h1>
<p data-loc-id="walkthrough.windows.text1">Se você estiver desenvolvendo C++ para Windows, recomendamos instalar o conjunto de ferramentas do compilador Microsoft Visual C++ (MSVC). Se você está segmentando o Linux a partir do Windows, verifique <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Usando C++ e Subsistema Windows para Linux (WSL) no código VS</a>. Ou você poderia <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">instalar GCC no Windows com MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Para instalar o MSVC, faça download de <strong data-loc-id="walkthrough.windows.build.tools1">Ferramentas de Build para Visual Studio 2019</strong> na página do Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Downloads</a>. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">No Instalador do Visual Studio, verifique a <strong data-loc-id="walkthrough.windows.build.tools2">Ferramentas de construção C++</strong> carga de trabalho e selecione <strong data-loc-id="walkthrough.windows.link.install">Instalar</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Observação</strong>: <span data-loc-id="walkthrough.windows.note1.text">Você pode usar o conjunto de ferramentas C++ das Ferramentas de Build do Visual Studio junto com o Visual Studio Code para compilar, construir e verificar qualquer base de código C++, contanto que também tenha uma licença válida do Visual Studio (Community, Pro ou Enterprise) que esteja ativamente usando para desenvolver essa base de código C++.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Abra o <strong data-loc-id="walkthrough.windows.command.prompt.name1">Prompt de comando do desenvolvedor para VS</strong> digitando 'desenvolvedor' no menu Iniciar do Windows.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Verifique a instalação do MSVC digitando <code>cl</code> no Prompt de comando do desenvolvedor para VS. Você deve ver uma mensagem de copyright com a versão e a descrição básica de uso.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Observação</strong>: <span data-loc-id="walkthrough.windows.note2.text">Para usar o MSVC a partir da linha de comando ou Código VS, você deve executar a partir de um <strong data-loc-id="walkthrough.windows.command.prompt.name2">Prompt de comando do desenvolvedor para VS</strong>. Um shell comum como <span>PowerShell</span>, <span>Bash</span> ou o prompt de comando do Windows não possui as variáveis ​​de ambiente de caminho necessárias definidas.</span></p>
</blockquote>
</li>
</ol>

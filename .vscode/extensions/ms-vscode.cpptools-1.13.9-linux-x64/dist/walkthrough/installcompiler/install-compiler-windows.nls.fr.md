<h1 data-loc-id="walkthrough.windows.install.compiler">Installer un compilateur C++ sur Windows</h1>
<p data-loc-id="walkthrough.windows.text1">Si vous utilisez le développement C++ pour Windows, nous vous recommandons d’installer l’ensemble d’outils du compilateur Microsoft Visual C++ (MSVC). Si vous ciblez Linux à partir de Windows, consultez <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">Utilisation de C++ et du Sous-système Windows pour Linux (WSL) dans VS Code</a>. Vous pouvez également <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">installer GCC sur Windows avec MinGW</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">Pour installer MSVC, téléchargez <strong data-loc-id="walkthrough.windows.build.tools1">Build Tools pour Visual Studio 2019</strong> à partir de la page Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">Téléchargements</a>. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">Dans le Visual Studio Installer, vérifiez la charge de travail <strong data-loc-id="walkthrough.windows.build.tools2">C++ Build Tools</strong> et sélectionnez <strong data-loc-id="walkthrough.windows.link.install">Installer</strong>.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Remarque</strong>: <span data-loc-id="walkthrough.windows.note1.text">Vous pouvez utiliser l’ensemble d’outils C++ à partir de Visual Studio Build Tools avec Visual Studio Code pour compiler, générer et vérifier n’importe quelle base de code C++, tant que vous disposez également d’une licence Visual Studio valide (Community, Pro ou Enterprise) que vous utilisez activement pour développer cette base de code C++.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Ouvrez le <strong data-loc-id="walkthrough.windows.command.prompt.name1">Invite de commandes développeur pour VS</strong> en tapant «&nbsp;développeur&nbsp;» dans le menu Démarrer de Windows.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">Vérifiez l’installation de votre MSVC en tapant <code>cl</code> dans la Invite de commandes développeur pour VS. Vous devez voir un message de Copyright avec la version et la description de l’utilisation de base.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Remarque</strong>: <span data-loc-id="walkthrough.windows.note2.text">Pour utiliser MSVC à partir de la ligne de commande ou VS Code, vous devez exécuter à partir d’un <strong data-loc-id="walkthrough.windows.command.prompt.name2">Invite de commandes développeur pour VS</strong>. Un interpréteur de commandes ordinaire, tel que <span>PowerShell</span>, <span>Bash</span> ou l’invite de commandes Windows, n’a pas les variables d’environnement de chemin d’accès nécessaires définies.</span></p>
</blockquote>
</li>
</ol>

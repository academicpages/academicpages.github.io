<h1 data-loc-id="walkthrough.windows.title.run.and.debug.your.file">Exécutez et déboguez votre fichier C++ sur Windows</h1>
<p data-loc-id="walkthrough.windows.run.and.debug.your.file">Pour exécuter et déboguer votre fichier C++ dans VS Code&nbsp;:</p>
<ol>
<li><p data-loc-id="walkthrough.windows.instructions1">Ouvrez le fichier source C++ que vous voulez exécuter et déboguer. Assurez-vous que ce fichier est actif (actuellement affiché et sélectionné) dans l'éditeur.</p>
</li>
<li><p data-loc-id="walkthrough.windows.press.f5">Appuyez sur <code>F5</code>. Ou, dans le menu principal, choisissez <strong><span data-loc-id="walkthrough.windows.run" data-loc-hint="Refers to Run command on main menu">Exécuter</span> &gt; <span data-loc-id="walkthrough.windows.start.debugging" data-loc-hint="Refers to Start Debugging command under Run menu on main menu">Démarrer le débogage</span></strong>.</p>
</li>
<li><p data-loc-id="walkthrough.windows.select.compiler">Sélectionner <strong>C++ (Windows)</strong>.</p>
</li>
<li><p data-loc-id="walkthrough.windows.choose.build.active.file">Choisir <strong>cl.exe - <span data-loc-id="walkthrough.windows.build.and.debug.active.file" data-loc-hint="Should be the same as translation for build.and.debug.active.file in extension.ts">Générer et déboguer le fichier actif</span></strong></p>
</li>
</ol>
<p data-loc-id="walkthrough.windows.after.running">Après l’exécution et le débogage de votre fichier C++ pour la première fois, vous remarquerez deux nouveaux fichiers dans <strong>.vscode</strong> de votre projet&nbsp;: <strong>tasks.json</strong> et <strong>launch.json</strong>.</p>

<p data-loc-id="walkthrough.windows.for.more.complex">Pour les scénarios de génération et de débogage plus complexes, vous pouvez personnaliser vos tâches de génération et déboguer les configurations dans <span>tasks.json</span> et <span>launch.json</span>. Par exemple, si vous passez normalement des arguments à votre compilateur lors de la génération à partir de la ligne de commande, vous pouvez spécifier ces arguments dans <span>tasks.json</span> à l’aide de la propriété <strong>compilerArgs</strong>. De même, vous pouvez définir des arguments à transférer à votre programme pour le débogage dans <span>launch.json</span>.</p>

<h1 data-loc-id="walkthrough.windows.install.compiler">Windows'a C++ derleyicisi yükleme</h1>
<p data-loc-id="walkthrough.windows.text1">Windows için C++ geliştirmesi yapıyorsanız Microsoft Visual C++ (MSVC) derleyici araç takımını yüklemenizi öneririz. Windows'tan Linux'u hedefliyorsanız <a href="https://code.visualstudio.com/docs/cpp/config-wsl" data-loc-id="walkthrough.windows.link.title1">VS Code'da Linux için C++’yı ve Windows Alt Sistemi’ni (WSL) kullanma</a> bölümüne göz atabilir veya şunu yapabilirsiniz: <a href="https://code.visualstudio.com/docs/cpp/config-mingw" data-loc-id="walkthrough.windows.link.title2">MinGW ile Windows’a GCC'yi yükleme</a>.</p>
<ol>
<li><p data-loc-id="walkthrough.windows.text2">MSVC’yi yüklemek için Visual Studio <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019" data-loc-id="walkthrough.windows.link.downloads">İndirmeler</a> sayfasından <strong data-loc-id="walkthrough.windows.build.tools1">Visual Studio 2019 için Derleme Araçları</strong> indirin. </p>
</li>
<li><p data-loc-id="walkthrough.windows.text3">Visual Studio Yükleyicisi’nde <strong data-loc-id="walkthrough.windows.build.tools2">C++ derleme araçları</strong> iş yükünü denetleyip <strong data-loc-id="walkthrough.windows.link.install">Yükle</strong> seçin.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note1">Not</strong>: <span data-loc-id="walkthrough.windows.note1.text">Herhangi bir C++ kod temelini derlemek, oluşturmak ve doğrulamak için Visual Studio Code ile birlikte Visual Studio Derleme Araçları’nda bulunan C++ araç takımını kullanabilirsiniz. Bunun yanı sıra, bu C++ kod temelini geliştirmek için etkin olarak kullandığınız geçerli bir Visual Studio lisansına (Community, Pro veya Enterprise) sahip olursunuz.</span></p>
</blockquote>
</li>
<li><p data-loc-id="walkthrough.windows.open.command.prompt">Windows Başlat menüsüne 'geliştirici' yazarak <strong data-loc-id="walkthrough.windows.command.prompt.name1">VS için Geliştirici Komut İstemi</strong> açın.</p>
</li>
<li><p data-loc-id="walkthrough.windows.check.install">VS için Geliştirici Komut İstemi’ne <code>cl</code> yazarak MSVC yüklemenizi denetleyin. Sürüm ve temel kullanım açıklamasını içeren bir telif hakkı iletisi göreceksiniz.</p>
<blockquote>
<p><strong data-loc-id="walkthrough.windows.note2">Not</strong>: <span data-loc-id="walkthrough.windows.note2.text">Komut satırından veya VS Code’dan MSVC’yi kullanmak için şuradan çalıştırmanız gerek: <strong data-loc-id="walkthrough.windows.command.prompt.name2">VS için Geliştirici Komut İstemi</strong>. <span>PowerShell</span>, <span>Bash</span> veya Windows komut istemi gibi sıradan bir kabuk gerekli yol ortam değişkenleri kümesi içermez.</span></p>
</blockquote>
</li>
</ol>

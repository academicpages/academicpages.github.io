<html><head></head><body><h1 data-loc-id="incompatible.extension.heading">Uyumsuz veya Uyumsuz C/C++ Uzantısı İkililer</h1>

<p data-loc-id="incompat.extension.text1">C/C++ uzantısı yerel ikililer içeriyor.</p>

<p data-loc-id="incompat.extension.text2">VS Code’da pazar yeri kullanıcı arabirimi aracılığıyla kurulduğunda, doğru yerel ikili dosyalar dahil edilmelidir. Uyumsuz ikili dosyalar algılandıysa ve C/C++ uzantısı, <a href="https://github.com/microsoft/vscode/issues/new?assignees=&amp;labels=&amp;template=bug_report.md" data-loc-id="bug.report.link.title">lütfen sorunu bildirin</a> VS Code’unda pazar yeri kullanıcı arabirimi aracılığıyla yüklendiyse.</p>

<h1 data-loc-id="reinstalling.extension.heading">C/C++ Uzantısı yeniden yükleniyor</h1>

<p data-loc-id="reinstall.extension.text1">Bir uzantının eşdeğer bir sürümünü yeniden yüklerken, VS Code mevcut uzantı dizinini yeniden kullanabilir. C/C++ uzantısını yeniden yüklerken bunun olmasını önlemek için önce mevcut uzantı dizinini silmek gerekebilir.</p>

<p data-loc-id="reinstall.extension.text2">Yüklü uzantı dizinleri, kullanıcı dizininizin altındaki aşağıdaki yollardan biri altında bulunabilir (Windows'ta `%USERPROFILE%` veya Linux ve macOS'ta `$HOME`)</p>

<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-insiders\extensions</code></pre>
<pre><code class="lang-bash">%USERPROFILE%\.vscode-exploration\extensions</code></pre>

<p data-loc-id="reinstall.extension.text3">Uzak bir bağlantıda:</p>
<pre><code class="lang-bash">$HOME/.vscode-server/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-insiders/extensions</code></pre>
<pre><code class="lang-bash">$HOME/.vscode-server-exploration/extensions</code></pre>

<p data-loc-id="reinstall.extension.text4">Yüklü C/C++ uzantı dizinlerine örnek yollar:</p>

<p data-loc-id="reinstall.extension.text5">Windows üzerinde:</p>
<pre><code class="lang-bash">%USERPROFILE%\.vscode\extensions\ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text6">Linux'ta:</p>
<pre><code class="lang-bash">$HOME/.vscode/extensions/ms-vscode.cpptools-1.9.0</code></pre>

<p data-loc-id="reinstall.extension.text7">Ardından, VS Code’daki pazar yeri kullanıcı arabirimi aracılığıyla yeniden yükleyin.</p>

<p data-loc-id="reinstall.extension.text8">Uzantının doğru sürümü VS Code tarafından dağıtılamazsa, sisteminiz için doğru VSIX <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools" data-loc-id="download.vsix.link.title">VS Code market web sitesinden indirildi</a> olabilir ve VS Code’daki market kullanıcı arabirimindeki “...” menüsü altındaki “VSIX'ten Yükle...” seçeneği kullanılarak yüklenebilir.</p>
</body></html>
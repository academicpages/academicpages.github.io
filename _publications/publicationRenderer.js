async function fetchAndParseBibtex(url) {
    try {
        const response = await fetch(url);
        const bibtexText = await response.text();

        let parsedData = parseBibtex(bibtexText); 

        return parsedData

        console.log(parsedData);
    } catch (error) {
        console.error("Error fetching or parsing BibTeX file:", error);
    }
}
  
function parseBibtex(bibtex) {
    let entries = [];
    let lines = bibtex.split('\n');
    let currentEntry = {};

    lines.forEach(line => {
        line = line.trim();
        if (line.startsWith('@')) {
            if (Object.keys(currentEntry).length !== 0) {
                entries.push(currentEntry);
                currentEntry = {};
            }
            currentEntry.type = line.match(/@(\w+)/)[1];
        } else if (line.includes('=')) {
            let [key, value] = line.split('=').map(s => s.trim());
            value = value.replace(/[{}]/g, ''); 
            currentEntry[key] = value;
        }
    });

    if (Object.keys(currentEntry).length !== 0) {
        entries.push(currentEntry);
    }

    return entries;
}

function generateArticleHtml(articles) {

    let html = '<ul>';
    articles.forEach(article => {
        console.log(article.authors)
        let authorsArray = article.authors.split("and ");
        let authorHtml = "";
        authorsArray.forEach((author, index) => {
            author = author.trim();
            if (author === "Wei, Dongtao") {
                if (article.mark) { // first author
                    authorHtml += `<strong>${author}</strong><sup>${article.mark}</sup>, `;
                } else { // 
                    authorHtml += `<strong>${author}</strong>`;
                }
            } else {
                authorHtml += `${author}`;
            }
        });
        authorHtml = authorHtml.trim().replace(/,\s*$/, "");

        html += `<li><a class='article-link' target='_blank' href='https://doi.org/${article.doi}'>${article.title}</a><a class='pdf-link' target='_blank' href="${article.pdflink}">[PDF]</a></li>`;
        if (article.if) {
            html += `<p>${article.authors}. (${article.year}). <i>${article.journal}</i>>(<strong>IF=${article.if}</strong>).</p>`;
        } else {
            html += `<p>${article.authors}. (${article.year}). <i>${article.journal}</i>.</p>`;
        }
        
    });
    html += '</ul>';
    return html
}

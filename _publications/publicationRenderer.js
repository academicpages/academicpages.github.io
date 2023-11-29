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
                removeTrailingComma(currentEntry);
                entries.push(currentEntry);
                currentEntry = {};
            }
            currentEntry.type = line.match(/@(\w+)/)[1];
        } else if (line.includes('=')) {
            let [key, value] = line.split('=').map(s => s.trim());
            value = value.replace(/[{}]/g, ''); 
            currentEntry[key] = value;
        } else if (line === '}') {
            removeTrailingComma(currentEntry);
            entries.push(currentEntry);
            currentEntry = {};
        }
    });

    if (Object.keys(currentEntry).length !== 0) {
        removeTrailingComma(currentEntry);
        entries.push(currentEntry);
    }

    return entries;
}

function removeTrailingComma(entry) {
    for (let key in entry) {
        if (entry.hasOwnProperty(key)) {
            entry[key] = entry[key].replace(/,\s*$/, '');
        }
    }
}


function generateArticleHtml(articles) {

    let html = '<ul>';
    articles.forEach(article => {
        let authorsArray = article.author.split(" and ");
        let authorHtml = "";
        authorsArray.forEach((author_, index) => {
            let name = convertBibAuthorToApa(author_.trim());
            if (authorsArray.length >  1 && index === authorsArray.length - 1) {
                authorHtml += "& ";
            }
            if (name === "Wei, D.") {
                if (article.mark == '#') { // first author
                    authorHtml += `<strong>${name}</strong><sup class='hash'>${article.mark}</sup>, `;
                } else if (article.mark == '*')
                {authorHtml += `<strong>${name}</strong><sup class='aterisk'>${article.mark}</sup>, `
                } else { // 
                    authorHtml += `<strong>${name}</strong>, `;
                }
            } else {
                authorHtml += `${name}, `;
            }
        });
        authorHtml = authorHtml.trim().replace(/,\s*$/, "");

        html += `<li><a class='article-link' target='_blank' href='https://doi.org/${article.doi}'>${article.title}</a><a class='pdf-link' target='_blank' href="${article.pdflink}">[PDF].</a></li>`;
        if (article.if) {
            html += `<p>${authorHtml} (${article.year}). <span class='journal'>${article.journal}</span>(<strong>IF=${article.if}</strong>).</p>`;
        } else {
            html += `<p>${authorHtml}(${article.year}). <span class='journal'>${article.journal}</span>.</p>`;
        }
        
    });
    html += '</ul>';
    return html
}

function convertBibAuthorToApa(fullName) {

    let parts = fullName.split(", ");
    let lastName = parts[0];
    let firstNames = parts[1] ? parts[1].split(" ").map(name => name.charAt(0).toUpperCase() + ".").join(" ") : "";
    return `${lastName}, ${firstNames}`;

}
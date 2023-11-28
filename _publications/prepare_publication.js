async function fetchAndParseBibtex(url) {
    try {
        const response = await fetch(url);
        const bibtexText = await response.text();

        let parsedData = parseBibtex(bibtexText); // 假设 parseBibtex 是你的解析函数

        console.log(parsedData);
    } catch (error) {
        console.error("Error fetching or parsing BibTeX file:", error);
    }
}

fetchAndParseBibtex('./2023-paper.bib');

  
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
            // 获取条目类型
            currentEntry.type = line.match(/@(\w+)/)[1];
        } else if (line.includes('=')) {
            let [key, value] = line.split('=').map(s => s.trim());
            value = value.replace(/[{}]/g, ''); // 移除花括号
            currentEntry[key] = value;
        }
    });

    if (Object.keys(currentEntry).length !== 0) {
        entries.push(currentEntry);
    }

    return entries;
}
  
  // 转换为JSON
  let jsonResult = parseBibtex(bibtexString);
  console.log(jsonResult);
  
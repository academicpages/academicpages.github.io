---
date: '2016-06-23'
slug: cronenberg-documents-or-how-i-typeset-my-thesis
title: 'Cronenberg documents: or, How I typeset my thesis'
---

I'm writing a PhD thesis for MIT, which specifies that the entire thesis must have a single, continuous page numbering. This is a pain, because my thesis is going to consist of a bunch of documents [cobbled](https://www.youtube.com/watch?v=RgvNNHFhPck) [together](https://en.wikipedia.org/wiki/Rick_Potion_No._9). The front matter, intro, and conclusion will be in the MIT latex template, but the three main chapters will be from publications. One is a published _PLoS_ paper, so I can just paste the pdf of the official paper right in there. Another is a Word document, since Word was the only way I could work on the document with my collaborator. The third is a latex document using a different, journal-provided template. How do I mash these things into one?

I was impressed with Chloé-Agathe Azencott's [solution](http://cazencott.info/index.php/post/2015/04/30/Numbering-PDF-Pages): turn all the documents into pdfs, concatenate them using [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/), make a separate latex document that is empty except for page numbers, split the "content" document and the "numbers" document each into individual pages, then "stamp" each numbers page onto each content page, and finally concatenate all those stamped pages into the final documents.

Though effective, I found this method ungraceful. I considered trying to get everything into the thesis latex by using [pandoc](http://pandoc.org/) to try to convert the Word document into latex and trimming and doctoring the manuscript latex to make it fit. My few experiences trying to convert complex latex files into complex Word files or vice versa have taught me that this is an error-prone process that requires a lot of manual curation. Thumbs down.

I settled on using latex's [pdfpages](https://www.ctan.org/pkg/pdfpages?lang=en), which lets you drop other pdfs wholesale into a latex document using the includepdf command. For the published paper, for example, I needed to include all the pages (the pages option), make the main document's page numbers actually appear (pagecommand option), and scale it down so that the main document's page number didn't stamp over any of the contents of the published paper (scale option):



    \includepdf[pages=-, pagecommand={\thispagestyle{plain}}, scale=0.95]{drop_in_pdf_filename}



I found this a lot simpler than any other option.
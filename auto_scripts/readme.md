This website and my [CV](samsledje.github.io/cv) build themselves with [PyYAML](https://pyyaml.org/) and [Jekyll](https://jekyllrb.com/). The following scripts are used to generate Jekyll markdown files:

* [`publicationsToMarkdown`](samsledje.github.io/auto_scripts/01a-publicationsToMarkdown.py)
* [`softwareToMarkdown`](samsledje.github.io/auto_scripts/02-softwareToMarkdown.py)
* [`talksToMarkdown`](samsledje.github.io/auto_scripts/03-talksToMarkdown.py)
* [`teachingToMarkdown`](samsledje.github.io/auto_scripts/04-teachingToMarkdown.py)
* [`cvToMarkdown`](samsledje.github.io/auto_scripts/cvToMarkdown.py)

These markdown files are then converted into HTML using the [academicpages template](https://github.com/academicpages/academicpages.github.io)

I also use scripts to [generate a BibTex file](samsledje.github.io/auto_scripts/01b-publicationsToBibtex.py) of my publications and [generate a LaTeX file](samsledje.github.io/auto_scripts/05b-cvToLatex.py) and [PDF](samsledje.github.io/auto_scripts/05c-cvToPDF.sh) of my CV.


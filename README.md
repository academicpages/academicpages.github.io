# Knevel Lab Pages Repository

Website can be found at https://knevel-lab.github.io/

## Guide to maintaining and updating

### Group tab

Per individual the following information should be entered into the ~/_pages/group.html document:

* Square profile picture in .jpg format
* Small biography
* LinkedIn profile link
* GitHub profile link
* PubMed author search
* OrcID

See below for template block: 

	<div style="height: 150px;">
	<img src="/images/Marc.jpg" alt="Marc Maurits" class="biopic">
	<h2>Marc Maurits</h2>
	PhD Candidate, pseudo-bioinformatician, expert in the field of being really picky and annoying about research, also website developer/maintainer
	<br>
	<a href="www.linkedin.com/in/marc-maurits-711889115"><i class="fab fa-fw fa-linkedin" aria-hidden="true"></i> LinkedIn</a>
	<a href="https://github.com/MarcMaurits"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>
	<a href="https://pubmed.ncbi.nlm.nih.gov/?term=Maurits+MP%5BAuthor%5D&sort=date"><i class="ai ai-pubmed-square ai-fw"></i> PubMed</a>
	<a href="https://orcid.org/0000-0002-3266-6232"><i class="ai ai-orcid-square ai-fw"></i> ORCID</a>
	</div>
	<hr>

N.B. The &lt;hr&gt; could be omitted for the last entry.

### Publications Tab

Per publication the following information should be entered into the ~/markdown_generator/publications.tsv document:

* Publication date
* Title
* Journal
* Short summary
* Short citation of the format Author, 1st. (Year) "title" &lt;i&gt;Journal&lt;/i&gt;
* Short name for paper
* Link to paper

See below for example entry:

| pub_date   | title                                                                                             | venue                          | excerpt            | citation                                                                                                                                                        | url_slug | paper_url                                                |
|------------|---------------------------------------------------------------------------------------------------|--------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------|
| 27/05/2020 | Using genetics to prioritize diagnoses for rheumatology outpatients with   inflammatory arthritis | Science Translational Medicine | short summary here | Knevel, R. (2020). "Using genetics to prioritize diagnoses for   rheumatology outpatients with inflammatory arthritis" <i>Science   Translational Medicine</i>. | gprob    | https://www.science.org/doi/10.1126/scitranslmed.aay1548 |

The easiest way to alter the .tsv file is using MS Excel, as a normal text editor messes up on the tabs a bit.

N.B. avoid any symbols in the short summary as UTF-8 encoding will be enforced!

After altering the publications.tsv one should run the ~/markdown_generator/publications.py script to convert the new information to a proper entry.

### Talks Tab

Per talk the following information should be entered into the ~/markdown_generator/talks.tsv document:

* Title
* Type of talk (oral/poster/postertour)
* Short name for talk
* Venue (e.g. EULAR 20xx)
* Date
* Location
* Link to talk
* Short summary

See below for example entry:

| title                              | type | url_slug | venue      | date       | location            | talk_url              | description                                                                                                                                 |
|------------------------------------|------|----------|------------|------------|---------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| EULAR 2022 Abstract EHR Clustering | Talk | talk-1   | EULAR 2022 | 01/06/2022 | Copenhagen, Denmark | http://exampleurl.com | Poster presentation of the work performed by Tjardo Maarseveen on the   clustering of Rheumatoid Arthritis patients using baseline EHR data |

The easiest way to alter the .tsv file is using MS Excel, as a normal text editor messes up on the tabs a bit.

N.B. avoid any symbols in the short summary as UTF-8 encoding will be enforced!

After altering the talks.tsv one should run the ~/markdown_generator/talks.py script to convert the new information to a proper entry.

### Applications Tab

Per application the following information should be entered into ~/_pages/applications.html document:

* Title
* Link to GitHub
* Square thumbnail in .jpg format
* Short description
* Developer name

See below for template block: 

	<h4>Dx Extraction</h4>

	<div style="height: 200px;">
	<a href="https://github.com/levrex/DiagnosisExtraction_ML">
	<img src="/images/DxE_img.jpg" alt="Dx Extraction" class="applink">
	</a>
	<p>Pipeline for the extraction of diagnoses from free-written text fields in electronic health records.</p>
	<p>Developed by TD Maarseveen</p>
	</div>
	<hr>

N.B. The &lt;hr&gt; could be omitted for the last entry.


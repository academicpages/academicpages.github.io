from pybtex.database import parse_file, BibliographyData
import os
from functools import reduce

FIELD_TO_DELETE = ["AUTHOR+an", "keywords", "note", "arXiv", "video", "code","venue", "link"]

def delete_fields(database):
    for entry in database.entries:
        for key in FIELD_TO_DELETE:
            if  database.entries[entry].fields.get(key) is not None:
                del database.entries[entry].fields[key]

def get_person_name(person):
    return " ".join(person.bibtex_first_names)  +" "+ " ".join(person.last_names)

def database_to_textfile(database, fname):
    # TODO: implement
    # get entries and sort by year
    entries = [database.entries[entry] for entry in database.entries]
    # print(entries)
    entries = sorted(
        entries, key=lambda x: int(
        x.fields.get("year", "0000") + x.fields.get("month", "00")
        ),
        reverse=True
    )

    string = ""
    for entry in entries:

        string += f'<div class= "paper">\n'
        string += f'<div class="paper_title">{entry.fields["title"].strip("{}")}</div>\n'

        string += f'<div class="paper_authors">'
        names = []
        annotation = entry.fields.get("AUTHOR+an","").split("=")
        if len(annotation)>=2 and annotation[1]=="highlight":
            author_num = int(annotation[0])
        for i, x in enumerate(entry.persons["author"]):
            if i+1==author_num:
                names.append(f'<b>{get_person_name(x)}</b>')
            else:
                names.append(get_person_name(x))

        string += f'{", ".join(names)}'
        string += f'</div>\n'

        if entry.fields.get("note"):
            string += f"<p class='note'>{entry.fields.get('note')}</p>"


        string += f'<ul>'
        string += f'\n <li class="paper_venue_year">{entry.fields["venue"]}</li>\n'
        if os.path.exists(f"assets/bib/{entry.key}.bib.txt"):
            string += f'<li class="paper_bib"><a href="/assets/bib/{entry.key}.bib.txt">.bib</a></li>\n'

        if os.path.exists(f"assets/papers/{entry.key}.pdf"):
            string += f'<li class="paper_pdf"><a href="/assets/papers/{entry.key}.pdf" >PDF</a></li>\n'

        if os.path.exists(f"assets/posters/{entry.key}.pdf"):
            string += f'<li class="paper_pdf"><a href="/assets/posters/{entry.key}.pdf" >poster</a></li>\n'

        if entry.fields.get("link"):
            string += f'<li class="paper_link"><a href="{entry.fields["link"]}">link</a></li> '

        if entry.fields.get("video"):
            string += f'<li class="paper_video"><a href="{entry.fields["video"]}">video</a></li>'

        if entry.fields.get("code"):
            string += f'<li class="paper_code"><a href="{entry.fields["code"]}">code</a></li>'

        string+='</ul>'


        string += "</div>"

        string += "\n \n"
    with open(fname, "w") as f:
        f.write(string)



if __name__=="__main__":
    FILE = 'assets/files/ref.bib'
    BIB_PATH = "assets/bib"
    database = parse_file(FILE, bib_format="bibtex")


    # generate selected.md
    # get database with selected entries only
    selected_entries = {}
    for entry in database.entries:
        # print(entry)
        # print(database.entries[entry].fields.get('keywords', "").split(","))
        if "selected" in list(
            map(
                lambda x: x.strip(),
                database.entries[entry].fields.get('keywords', "").split(",")
            )
        ):
            selected_entries[entry] = database.entries[entry]
    selected_db = BibliographyData(entries=selected_entries)
    database_to_textfile(selected_db, "_pages/selected_publications.md")

    selected_entries = {}
    for entry in database.entries:
        # print(entry)
        # print(database.entries[entry].fields.get('keywords', "").split(","))
        if "peer-reviewed" in list(
            map(
                lambda x: x.strip(),
                database.entries[entry].fields.get('keywords', "").split(",")
            )
        ):
            selected_entries[entry] = database.entries[entry]
    selected_db = BibliographyData(entries=selected_entries)
    database_to_textfile(selected_db, "_pages/peer-reviewed.md")

    selected_entries = {}
    for entry in database.entries:
        if "peer-reviewed" in list(map(
            lambda x: x.strip(),
            database.entries[entry].fields.get('keywords', "").split(",")
            )) and int(database.entries[entry].fields.get("year"))>2016:

            selected_entries[entry] = database.entries[entry]
    selected_db = BibliographyData(entries=selected_entries)
    database_to_textfile(selected_db, "_pages/peer-reviewed.md")

    selected_entries = {}
    for entry in database.entries:
        if int(database.entries[entry].fields.get("year"))<2016:
            selected_entries[entry] = database.entries[entry]
    selected_db = BibliographyData(entries=selected_entries)
    database_to_textfile(selected_db, "_pages/before_phd.md")

    selected_entries = {}
    for entry in database.entries:
        if "peer-reviewed" not in list(map(
            lambda x: x.strip(),
            database.entries[entry].fields.get('keywords', "").split(",")
            )) and int(database.entries[entry].fields.get("year"))>2016:

            selected_entries[entry] = database.entries[entry]
    selected_db = BibliographyData(entries=selected_entries)
    database_to_textfile(selected_db, "_pages/other_pubs.md")


    # create bib file for each entry
    try:
        os.makedirs(BIB_PATH)
    except Exception as e:
        print("bib folder already exists")

    for entry in database.entries:
        print(f"Processing {entry}")
        fname = f"{BIB_PATH}/{entry}.bib.txt"
        singledb = BibliographyData(entries={entry:database.entries[entry]})
        delete_fields(singledb)
        singledb.to_file(fname, bib_format="bibtex")


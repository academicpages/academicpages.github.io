#!/usr/bin/env python

# conference html generator for academicpages
#
# Takes bibtex of conference presentations and converts them for use with [academicpages.github.io](academicpages.github.io).


# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
#

import os
from time import strptime
from pybtex.database.input import bibtex



publist = {
        "file": "conference_talks.bib",  # replace with .bib name
        "venuekey": "booktitle",
        "venue-pretext": "",
        "collection": {"name": "talks", "permalink": "/talks/"},
}


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    "--": "&ndash;",
    }


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


all_citations = []

parser = bibtex.Parser()
bibdata = parser.parse_file(publist["file"])
raw_bib = bibdata.to_string('bibtex').split("\n@conference")

# loop through the individual references in a given bibtex file
for idx, bib_id in enumerate(bibdata.entries):
    # reset default date
    pub_year = "1900"
    pub_month = "01"
    pub_day = "01"

    b = bibdata.entries[bib_id].fields

    try:
        pub_year = f'{b["year"]}'

        # todo: this hack for month and day needs some cleanup
        if "month" in b.keys():
            if len(b["month"]) < 3:
                pub_month = "0" + b["month"]
                pub_month = pub_month[-2:]
            elif b["month"] not in range(12):
                tmnth = strptime(b["month"][:3], '%b').tm_mon
                pub_month = "{:02d}".format(tmnth)
            else:
                pub_month = str(b["month"])
        if "day" in b.keys():
            pub_day = str(b["day"])

        pub_date = pub_year + "-" + pub_month + "-" + pub_day

        # Build Citation from text
        citation = ""

        # add authors to citation
        for author in bibdata.entries[bib_id].persons["author"]:
            #print(author.first_names)
            first_name = author.first_names[0]
            middle_name = None if not author.middle_names else author.middle_names[0]
            # uncomment below if pre-last names exist i.e. 'van ...'
            # prelast_name = None if not author.prelast_names else author.prelast_names[0]
            last_name = " ".join([str(x) for x in author.last_names])
            full_name = first_name + " " + " ".join(filter(None, (middle_name, last_name)))

            citation = citation + full_name + ", "
        # citation now has all authors
        # add presentation title, with possible href
        clean_title = html_escape(b["title"].replace("{", "").replace("}", "").replace("\\", ""))
        if b["url"] != "":
            citation = citation + '<a href="' + b["url"].replace("{", "").replace("}", "") + '"> ' + clean_title + "</a>, "
        else:
            citation = citation + clean_title + ", "

        # add conference name
        venue = b[publist["venuekey"]].replace("{", "").replace("}", "").replace("\\", "")
        # deal with superscript tags
        super_loc = venue.find("textsuperscript")
        if super_loc != -1:
            super_s = venue.replace("textsuperscript", "<sup>")
            loc = super_s.find("<sup>")
            venue = super_s[:loc+7] + "</sup>" + super_s[loc+7:]


        # if "&" in venue:
        #     print(venue)
        #     venue = venue.replace("\&", "&amp;")
        # else:
        #     venue = venue.replace("\\", "")

        citation = citation + html_escape(venue) + ", "
        # add location
        citation = citation + " " + html_escape(b["address"].replace("{", "").replace("}", "").replace("\\", ""))
        # add date
        citation = citation + " (" + b["month"] + " " + b["year"] + ")"
        all_citations.append(citation)
    except KeyError as e:
        print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30], "..." * (len(b['title']) > 30), "\"")
        continue
###################################


# start making file
html = "---\nlayout: archive\n"
html += 'title: "Talks and presentations"\n'
html += "permalink: " + publist["collection"]["permalink"]
html += "\nauthor_profile: true\n---\n\n\n"


html += "<b>Invited Talks</b>\n"
# start section
html += "\n<ul>\n"

#invited_talks = []

# do reverse chronological order
for inv_talk in all_citations[::-1]:
    html += "  <li> " + inv_talk + " </li>\n"

# end section
html += "</ul>\n"

with open("../_pages/talks2.html", 'w', encoding="utf-8") as f:
    f.write(html)

#html += "\n<b>Talks</b>\n"


#html += "\n<b>Posters</b>\n"














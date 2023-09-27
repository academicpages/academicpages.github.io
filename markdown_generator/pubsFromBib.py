#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

# Build a .bib file from the individual bib entries in files/bib:
from pathlib import Path
parentdir = str(Path(os.getcwd()).parent.absolute())
with open("proceedings.bib", "w") as procfile, open("pubs.bib", "w") as pubsfile, open ("dissertation.bib", "w") as dissertationfile:
    for bib_file in os.listdir(parentdir + '/files/bib'):
        with open(parentdir + '/files/bib/' + bib_file, 'r') as bf:
            lines = bf.readlines()
            if lines[0].strip().startswith('@inproceedings'):
                procfile.writelines(lines)
            elif lines[0].strip().startswith('@article'):
                pubsfile.writelines(lines)
            elif lines[0].strip().startswith('@phdthesis'):
                dissertationfile.writelines(lines)

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "proceeding": {
        "file" : "proceedings.bib",
        "authorkey": "author",
        "venuekey": "booktitle",
        "venue-pretext": "",
        "links": "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "journal":{
        "file": "pubs.bib",
        "authorkey": "author",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "dissertation":{
        "file": "dissertation.bib",
        "authorkey": "author",
        "venuekey" : "school",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    }
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def locate_resource(parentdir: str, resource_type: str, bib_id: str):
    resource_available = False
    resource_dir = f"{parentdir}/files/{resource_type}"
    resource_url = ""
    if f"{bib_id}.txt" in os.listdir(resource_dir):
        resource_available = True
        extended_version_url = open(f"{resource_dir}/{bib_id}.txt").readlines()[0].strip()
    elif f"{bib_id}.pdf" in os.listdir(resource_dir):
        resource_available = True
        resource_url = f"https://github.com/latower/latower.github.io/raw/master/files/{resource_type}/{bib_id}.pdf"
    return resource_available, resource_url


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            authors = ""
            for author in bibdata.entries[bib_id].persons["author"]:
                authors = authors+" "+author.first_names[0]+" "+author.last_names[0].replace('{', '').replace('}', '')+", "
            authors = authors[:-2]
            citation += authors

            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            note = False
            if "note" in b.keys():
                if len(str(b["note"])) > 5:
                    md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                    note = True

            md += "\ndate: " + str(pub_date)

            md += "\nyear: " + str(pub_year)

            md += "\nauthor: '" + html_escape(authors) + "'"

            md += "\nvenue: '" + html_escape(venue) + "'"

            if 'abstract' in bibdata.entries[bib_id].fields:
                md += "\nabstract: '" + html_escape(bibdata.entries[bib_id].fields['abstract']) + "'"

            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            paper_available, paper_url = locate_resource(parentdir=parentdir, resource_type="paper", bib_id=bib_id)
            slides_available, slides_url = locate_resource(parentdir=parentdir, resource_type="slides", bib_id=bib_id)
            video_available, video_url = locate_resource(parentdir=parentdir, resource_type="video", bib_id=bib_id)
            poster_available, poster_url = locate_resource(parentdir=parentdir, resource_type="code", bib_id=bib_id)
            code_available, code_url = locate_resource(parentdir=parentdir, resource_type="code", bib_id=bib_id)
            blog_available, blog_url = locate_resource(parentdir=parentdir, resource_type="blog", bib_id=bib_id)
            extended_version_available, extended_version_url = locate_resource(parentdir=parentdir, resource_type="extended-version", bib_id=bib_id)

            # Create links for these materials
            available_material = []
            if paper_available:
                available_material.append(('pdf', paper_url))
            if extended_version_available:
                available_material.append(('extended version', extended_version_url))
            if slides_available:
                available_material.append(('slides', slides_url))
            if poster_available:
                available_material.append(('poster', poster_url))
            if video_available:
                available_material.append(('video', video_url))
            if code_available:
                available_material.append(('code', code_url))
            if blog_available:
                available_material.append(('blog', blog_url))

            available_material.append(('bib', f"https://github.com/latower/latower.github.io/raw/master/files/bib/{bib_id}.bib"))
            links = "\nlinks: "
            # links += ", ".join(["<a href=\"" + text_url + "\" target=\"_blank\">" + text + "</a>" for (text, text_url) in available_material])
            links_list = []
            for (text, text_url) in available_material:
                if text_url.endswith('.bib') or text_url.endswith('.pdf'):
                    links_list.append("<a href=\"" + text_url + "\" download target=\"_blank\">" + text + "</a>")
                else:
                    links_list.append("<a href=\"" + text_url + "\" target=\"_blank\">" + text + "</a>")
            links += ", ".join(links_list)
            links += ""
            # links = "\nlinks: \["
            # links += ", ".join(["[" + text + "](" + text_url + "){:target=\"_blank\"}" for (text, text_url) in available_material])
            # links += "\]"

            md += links

            # links = html_escape(links)
            # publist[pubsource][links] = links
            # md += "\ncitation: '" + html_escape(citation) + "'"

            md += "\n---"

            
            ## Markdown description for individual page
            if note:
                md += "\n" + html_escape(b["note"]) + "\n"

            # if url:
            #     md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n"
            # else:
            #     md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"



            md_filename = os.path.basename(md_filename)

            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
                # f.write(links)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue

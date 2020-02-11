import re
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

pubData = load(open("data/publications.yaml", "r"), Loader=Loader)

for paper in pubData:
    try:
        title = paper['title']
        year = paper['year']
        authors = paper['authors']
        venue = paper['journal']
        link = paper['pdf-link']
    except KeyError:
        continue

    with open(f"../_publications/{year}-{re.split(',|:| ',title)[0].md}", "w+") as f:
        f.write("---\n")
        f.write(f"title: '{title}'\n")
        f.write(f"collection: publication\n")
        f.write(f"permalink: publications/{year}-{title.split(',|:| ')}\n")
        f.write(f"date: {year}\n")
        f.write(f"venue: '{venue}''\n")
        f.write(f"paperurl: {link}\n")
        f.write("---")

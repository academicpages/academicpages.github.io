import sys
import pandas as pd
from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry

if sys.argv[1].endswith(".bib"):

    parser = bibtex.Parser()
    bibdata = parser.parse_file(sys.argv[1])

    entries = []

    for tag in bibdata.entries.keys():
        d = {}
        entry = bibdata.entries[tag]
        fields = entry.fields

        d["tag"] = tag
        for k in fields.keys():
            d[k.lower()] = fields[k]

        d["bibtex.string"] = BibliographyData({tag: entry}).to_string("bibtex")

        entries.append(d)

    df = pd.DataFrame(entries)
    df = df.set_index("tag")

    fName = sys.argv[1].split(".")[0]
    df.to_csv(fName+".converted.csv")

elif sys.argv[1].endswith(".csv"):

    outfile = open(sys.argv[1].split(".")[0]+".converted.bib", "w+")

    df = pd.read_csv(sys.argv[1])
    df = df.set_index("tag")

    bd = {}

    for ref in df.iterrows():
        tag = ref[0]
        entry = ref[1].drop("bibtex.string").dropna().astype(str)

        pybEntry = Entry("article", entry)
        bd[tag] = pybEntry

    outfile.write(BibliographyData(bd).to_string("bibtex"))
    outfile.close()

else:
    print("Unable to handle that file extension.")
    sys.exit(1)

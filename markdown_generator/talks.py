#!/usr/bin/env python
# coding: utf-8

# Talks markdown generator for academicpages
#
# Takes a TSV or CSV of talks with metadata and converts them for use with
# the academicpages GitHub Pages template.
# Usage: python3 talks.py talks.tsv
#        python3 talks.py talks.csv
#        python3 talks.py talks.tsv _talks/
#
# Uses the Python standard library (csv) so it has no external dependencies.

import csv
import os
import sys

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    if isinstance(text, str):
        return "".join(html_escape_table.get(c, c) for c in text)
    else:
        return ""


def main(input_file, output_dir=None):
    if output_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "..", "_talks")

    os.makedirs(output_dir, exist_ok=True)

    ext = os.path.splitext(input_file)[1].lower()
    delimiter = "\t" if ext in (".tsv", ".txt") else ","

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            title = row.get("title", "").strip()
            url_slug = row.get("url_slug", "").strip()
            date = row.get("date", "").strip()
            talk_type = row.get("type", "").strip()
            venue = row.get("venue", "").strip()
            location = row.get("location", "").strip()
            talk_url = row.get("talk_url", "").strip()
            description = row.get("description", "").strip()

            if not title or not url_slug or not date:
                print("Skipping row: missing required field (title, url_slug, or date)", file=sys.stderr)
                continue

            md_filename = date + "-" + url_slug + ".md"
            md_path = os.path.join(output_dir, md_filename)

            md = "---\n"
            md += "title: \"" + title + "\"\n"
            md += "collection: talks\n"
            if len(talk_type) > 3:
                md += 'type: "' + talk_type + '"\n'
            else:
                md += 'type: "Talk"\n'
            md += "permalink: /talks/" + date + "-" + url_slug + "\n"
            if venue:
                md += 'venue: "' + venue + '"\n'
            md += "date: " + date + "\n"
            if location:
                md += 'location: "' + location + '"\n'
            md += "---\n"

            if talk_url:
                md += "\n[More information here](" + talk_url + ")\n"
            if description:
                md += "\n" + html_escape(description) + "\n"

            with open(md_path, "w", encoding="utf-8") as out:
                out.write(md)
            print("Created: " + md_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 talks.py <input_file> [output_dir]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    main(input_file, output_dir)

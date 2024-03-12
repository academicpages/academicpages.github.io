# Code written by ChatGPT and adapted by Florian Blanc on Oct. 3, 2023


import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-b","--bib_file",type=str)
args = parser.parse_args()


def parse_bib_file(file_path):
    entries = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        entry = None

        for line in lines:
            line = line.strip()

            if line.startswith('@'):
                if entry is not None:
                    entries.append(entry)
                entry = {'type': line.split('{')[0][1:], 'key': line.split('{')[1][:-1]}
            elif '=' in line:
                key, value = map(str.strip, line.split('=', 1))
                if value[0] == '{' and value[-1] == '}':
                    value = value[1:-1]
                entry[key] = value

    if entry is not None:
        entries.append(entry)

    # Remove curly brackets and final comma from values
    for entry in entries:
        for key, value in entry.items():
            if value.startswith('{') and value.endswith('},'):
                entry[key] = value[1:-2]

    return entries


def generate_markdown(entry):
    markdown_content = f"""---
title: "{entry['title']}"
collection: publications
permalink: /publication/{entry['key']}
abstract: '{entry.get('abstract', 'No abstract available')}'
year: {entry.get('year', 'YYYY-MM-DD')}
venue: '{entry.get('journal', 'Conference')}' 
doi: '{entry.get('doi','No DOI available')}'
paperurl: 'https://doi.org/{entry.get('doi', '')}'
citation: '{entry.get('author', 'Unknown')} ({entry.get('year', 'YYYY')}). "{entry.get('title', 'Untitled')}." <i>{entry.get('journal', 'Conference')}</i>. {entry.get('volume', 'Volume')}{entry.get('number', '(Number)')}.'
---

[Link](https://doi.org/{entry.get('doi', '')})

Citation: {entry.get('author', 'Unknown')} ({entry.get('year', 'YYYY')}). "{entry.get('title', 'Untitled')}." <i>{entry.get('journal', 'Conference')}</i>. {entry.get('volume', 'Volume')}{entry.get('number', '(Number)')}.
"""

    return markdown_content

def convert_bib_to_markdown(bib_file):
    entries = parse_bib_file(bib_file)

    for entry in entries:
        markdown_content = generate_markdown(entry)

        # Create a directory if it doesn't exist
        if not os.path.exists('_publications'):
            os.makedirs('_publications')

        # Write the content to a markdown file
        with open(f'_publications/{entry["key"]}.md', 'w', encoding='utf-8') as file:
            file.write(markdown_content)

# Example usage
convert_bib_to_markdown(args.bib_file)


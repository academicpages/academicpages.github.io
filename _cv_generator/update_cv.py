'''
update_cv.py

reads in any changes from zotero subcollections of personal citations, and then
writes and creates new cv.html and cv.pdf files. It also updates the pdfs in the
files directory to be the attached pdfs from zotero

John Ragland, July 2023
'''

from pyzotero import zotero
import bibtexparser
from jinja2 import Template, Environment, FileSystemLoader
import re
import subprocess
#from ironpdf import *
import os
import cv_tools

print('loading citations from zotero...')

# Set up your Zotero API credentials (specific to user)
library_id = '5442436'
library_type = 'user'  # 'user' or 'group'
api_key = '4beyxpmgVHhZavP45bkLf5vG'

# Create a Zotero API client
zot = zotero.Zotero(library_id, library_type, api_key)

# These keys can be found in the URL of the collection
talks_id = 'ZRKYJLDM'
papers_id = '8QEDMTRG'
thesi_id = '9PJCMLTU'
invited_id = 'I4375JL3'

# Get the items in the collection
talks = zot.collection_items(talks_id)
papers = zot.collection_items(papers_id)
thesi = zot.collection_items(thesi_id)
invited = zot.collection_items(invited_id)

# Parse attachments and entries
talk_attachments = []
for talk in talks:
    if talk['data']['itemType'] == 'attachment':
        talk_attachments.append(talk)
        talks.remove(talk)

paper_attachments = []
for paper in papers:
    if paper['data']['itemType'] == 'attachment':
        paper_attachments.append(paper)
        papers.remove(paper)

thesi_attachments = []
for thesis in thesi:
    if thesis['data']['itemType'] == 'attachment':
        thesi_attachments.append(thesis)
        thesi.remove(thesis)

invited_attachments = []
for invite in invited:
    if invite['data']['itemType'] == 'attachment':
        invited_attachments.append(invite)
        invited.remove(invite)

# Create List of Bibliography Entries
talks_bib_entries = []
for talk in talks:
    talks_bib_entries.append(zot.item(talk['data']['key'], content='bib', style='bibtex'))

papers_bib_entries = []
for paper in papers:
    papers_bib_entries.append(zot.item(paper['data']['key'], content='bib', style='bibtex'))

thesi_bib_entries = []
for thesis in thesi:
    thesi_bib_entries.append(zot.item(thesis['data']['key'], content='bib', style='bibtex'))

invited_bib_entries = []
for invite in invited:
    invited_bib_entries.append(zot.item(invite['data']['key'], content='bib', style='bibtex'))

# save attachments to files directory
zot_dir = '/Users/jhrag/Library/CloudStorage/OneDrive-UW/zotero_library/'
files_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'files/'))

cv_tools.delete_files_in_directory(files_dir)

# Skipping attachment handling for now
"""
for talk_attachment in talk_attachments:
    fn = talk_attachment['data']['path'][12:]
    os.system(
        f"cp '{zot_dir}{fn}' '{files_dir}/{fn.replace(' ','_')}'"
    )
for paper_attachment in paper_attachments:
    fn = paper_attachment['data']['path'][12:]
    os.system(
        f"cp '{zot_dir}{fn}' '{files_dir}/{fn.replace(' ','_')}'"
    )
for thesi_attachment in thesi_attachments:
    fn = thesi_attachment['data']['path'][12:]
    os.system(
        f"cp '{zot_dir}{fn}' '{files_dir}/{fn.replace(' ','_')}'"
    )
for invited_attachment in invited_attachments:
    fn = invited_attachment['data']['path'][12:]
    os.system(
        f"cp '{zot_dir}{fn}' '{files_dir}/{fn.replace(' ','_')}'"
    )
"""
for k,i in enumerate(talks_bib_entries):
    start = i[0].index("@") 
    if k == 0:
        talks_bib = i[0][start:-6]
    else:
        talks_bib += i[0][start:-6]
    talks_bib += '\n'

for k, i in enumerate(papers_bib_entries):
    start = i[0].index("@")
    if k == 0:
        papers_bib = i[0][start:-6]
    else:
        papers_bib += i[0][start:-6]
    papers_bib += '\n'


for k, i in enumerate(thesi_bib_entries):
    start = i[0].index("@")
    if k == 0:
        thesi_bib = i[0][start:-6]
    else:
        thesi_bib += i[0][start:-6]
    thesi_bib += '\n'

for k, i in enumerate(invited_bib_entries):
    start = i[0].index("@")
    if k == 0:
        invited_bib = i[0][start:-6]
    else:
        invited_bib += i[0][start:-6]
    invited_bib += '\n'
# Add the attachments to the BibTeX entries

files_dir_url = 'https://john-ragland.github.io/files'

for k, paper in enumerate(papers):
    for paper_attachment in paper_attachments:
        if paper['key'] == paper_attachment['data']['parentItem']:
            fn = f"{files_dir_url}/{paper_attachment['data']['path'][12:].replace(' ','_')}"
            papers_bib_entries[k] = cv_tools.insert_string_before_last_brace(papers_bib_entries[k][0], f'filepath={ {fn} }')

for k, talk in enumerate(talks):
    for talk_attachment in talk_attachments:
        if talk['key'] == talk_attachment['data']['parentItem']:
            fn = f"{files_dir_url}/{talk_attachment['data']['path'][12:].replace(' ','_')}"
            talks_bib_entries[k] = cv_tools.insert_string_before_last_brace(talks_bib_entries[k][0], f'filepath={ {fn} }')

for k, thesis in enumerate(thesi):
    for thesis_attachment in thesi_attachments:
        if thesis['key'] == thesis_attachment['data']['parentItem']:
            fn = f"{files_dir_url}/{thesis_attachment['data']['path'][12:].replace(' ','_')}"
            thesi_bib_entries[k] = cv_tools.insert_string_before_last_brace(thesi_bib_entries[k][0], f'filepath={ {fn} }')

for k, invite in enumerate(invited):
    for invite_attachment in invited_attachments:
        if invite['key'] == invite_attachment['data']['parentItem']:
            fn = f"{files_dir_url}/{invite_attachment['data']['path'][12:].replace(' ','_')}"
            invited_bib_entries[k] = cv_tools.insert_string_before_last_brace(invited_bib_entries[k][0], f'filepath={ {fn} }')

# Write Bibtex files
with open('talks.bib', 'w', encoding='utf-8') as file:
    file.write(talks_bib)
with open('papers.bib', 'w', encoding='utf-8') as file:
    file.write(papers_bib)
with open('thesi.bib', 'w', encoding='utf-8') as file:
    file.write(thesi_bib)
with open('invited.bib', 'w', encoding='utf-8') as file:
    file.write(invited_bib)

# Remove problematic characters from the citation keys
cv_tools.edit_citation_keys('talks.bib')
cv_tools.edit_citation_keys('papers.bib')
cv_tools.edit_citation_keys('thesi.bib')
cv_tools.edit_citation_keys('invited.bib')

print('Bibtex files written')

# Create Markdown files
print('creating cv...')

# Read the BibTeX file using bibtexparser
with open('papers.bib') as file:
    papers = bibtexparser.load(file).entries
with open('talks.bib') as file:
    talks = bibtexparser.load(file).entries
with open('invited.bib') as file:
    invited = bibtexparser.load(file).entries
with open('thesi.bib') as file:
    thesi = bibtexparser.load(file).entries

# Load the Markdown template
with open('template.md') as file:
    template_content = file.read()

# Create a Jinja2 Template object
template = Template(template_content)

# Render the template with the publications data
markdown_output = template.render(papers=papers, talks=talks, thesi=thesi, invited=invited)

# Save the rendered Markdown content to a file
with open('cv.md', 'w') as file:
    file.write(markdown_output)

# Bold every instance of my name
def bold_string_in_markdown(markdown_content, target_string):
    markdown_new = markdown_content.replace(target_string, '**' + target_string + '**')

    return markdown_new

# Read the Markdown content from file
with open('cv.md') as file:
    markdown_content = file.read()

# Bold the target string in the Markdown content
bolded_content = bold_string_in_markdown(markdown_content, 'Ragland, John')

# Save the bolded Markdown content to a new file
with open('cv.md', 'w') as file:
    file.write(bolded_content)

print('markdown file written')

## write HTML file
# Read the Markdown content from file
with open('cv.md') as file:
    markdown_content = file.read()

# Create a Jinja2 environment and load the template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cv_template.html')

# Render the template with the Markdown content
rendered_content = template.render(content=markdown_content)

# Write the rendered content to a temporary Markdown file
with open('temp.md', 'w') as file:
    file.write(rendered_content)

# Convert the temporary Markdown file to HTML using Pandoc
subprocess.run(['pandoc', 'temp.md', '-o', 'cv.html'])

# Remove the temporary Markdown file
subprocess.run(['rm', 'temp.md'])

print('HTML file written')

## write PDF using wkhtmltopdf
print('writing pdf...')
os.system(
    'wkhtmltopdf --page-size Letter --margin-top 25.4mm --margin-bottom 25.4mm --margin-left 25.4mm --margin-right 25.4 cv.html cv.pdf'
)
print('PDF written.\nCV update complte.')

                
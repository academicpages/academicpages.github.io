# This is just the second half of update_cv copied for when there isn't internet

from pyzotero import zotero
import bibtexparser
from jinja2 import Template, Environment, FileSystemLoader
import re
import subprocess
#from ironpdf import *
import os

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
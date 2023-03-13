# Convert _pages/cv.md to pdf and save in files/JohnRagland_cv.pdf
import markdown
import pdfkit
from weasyprint import HTML

# Read the markdown file content
with open('../_pages/cv.md', 'r') as file:
    markdown_content = file.read()

# Convert the markdown to HTML
html_content = markdown.markdown(markdown_content)

# Use weasyprint to convert the HTML to PDF
HTML(string=html_content).write_pdf('../files/JohnRagland_cv.pdf')

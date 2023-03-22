from selenium.webdriver.common.by import By

from nbformat.v4 import new_markdown_cell


def get_rendered_contents(nb):
    cl = ["text_cell", "render"]
    rendered_cells = [cell.find_element(By.CLASS_NAME, "text_cell_render")
                      for cell in nb.cells 
                      if all([c in cell.get_attribute("class") for c in cl])]
    return [x.get_attribute('innerHTML').strip()
            for x in rendered_cells 
            if x is not None]

            
def test_markdown_cell(prefill_notebook):
    nb = prefill_notebook([new_markdown_cell(md) for md in [
        '# Foo', '**Bar**', '*Baz*', '```\nx = 1\n```', '```aaaa\nx = 1\n```',
        '```python\ns = "$"\nt = "$"\n```'
    ]])

    assert get_rendered_contents(nb) == [
        '<h1 id="Foo">Foo<a class="anchor-link" href="#Foo">¶</a></h1>',
        '<p><strong>Bar</strong></p>',
        '<p><em>Baz</em></p>',
        '<pre><code>x = 1</code></pre>',
        '<pre><code class="cm-s-ipython language-aaaa">x = 1</code></pre>',
        '<pre><code class="cm-s-ipython language-python">' + 
        '<span class="cm-variable">s</span> <span class="cm-operator">=</span> <span class="cm-string">"$"</span>\n' +
        '<span class="cm-variable">t</span> <span class="cm-operator">=</span> <span class="cm-string">"$"</span></code></pre>'
    ]

def test_markdown_headings(notebook):
    lst = list([1, 2, 3, 4, 5, 6, 2, 1])
    for i in lst:
        notebook.add_markdown_cell()
        cell_text = notebook.browser.execute_script(f"""
            var cell = IPython.notebook.get_cell(1);
            cell.set_heading_level({i});
            cell.get_text();
        """)
        assert notebook.get_cell_contents(1) == "#" * i + " "
        notebook.delete_cell(1)


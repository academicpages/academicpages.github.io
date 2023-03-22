"""Test saving a notebook with escaped characters
"""

from tkinter import E
from urllib.parse import quote
from .utils import EDITOR_PAGE, TREE_PAGE

# TODO: REWORK from polling => async
def check_display_name(nb, nbname):
    display_updated = False
    count_check = 0

    while not display_updated and count_check < 5:
        displayed_name = nb.locate('#notebook_name', page=EDITOR_PAGE).get_inner_text()
        if displayed_name + '.ipynb' == nbname:
            display_updated = True
        count_check += 1
    assert displayed_name + '.ipynb' == nbname

def test_save(notebook_frontend):
    # don't use unicode with ambiguous composed/decomposed normalization
    # because the filesystem may use a different normalization than literals.
    # This causes no actual problems, but will break string comparison.
    nbname = "has#hash and space and unicø∂e.ipynb"
    escaped_name = quote(nbname)

    notebook_frontend.edit_cell(index=0, content="s = '??'")

    set_nb_name = f"() => Jupyter.notebook.set_notebook_name('{nbname}')"
    notebook_frontend.evaluate(set_nb_name, page=EDITOR_PAGE)

    model = notebook_frontend.evaluate("() => Jupyter.notebook.save_notebook()", page=EDITOR_PAGE)
    assert model['name'] == nbname

    current_name = notebook_frontend.evaluate("() => Jupyter.notebook.notebook_name", page=EDITOR_PAGE)
    assert current_name == nbname

    current_path = notebook_frontend.evaluate("() => Jupyter.notebook.notebook_path", page=EDITOR_PAGE)
    assert current_path == nbname

    check_display_name(notebook_frontend, nbname)

    notebook_frontend.evaluate("() => Jupyter.notebook.save_checkpoint()", page=EDITOR_PAGE)

    checkpoints = notebook_frontend.evaluate("() => Jupyter.notebook.checkpoints", page=EDITOR_PAGE)
    assert len(checkpoints) == 1

    notebook_frontend.try_click_selector('#ipython_notebook a', page=EDITOR_PAGE)
    notebook_frontend.wait_for_selector('.item_link', page=EDITOR_PAGE)

    hrefs_nonmatch = []
    all_links = notebook_frontend.locate_all('a.item_link', page=EDITOR_PAGE)
    
    for link in all_links:
        href = link.get_attribute('href')

        if escaped_name in href:
            href = href.split('/a@b/')
            notebook_frontend.navigate_to(page=EDITOR_PAGE, partial_url=href[1])
            notebook_frontend.wait_for_selector('.cell', page=EDITOR_PAGE)
            break
        hrefs_nonmatch.append(href)
    else:
        raise AssertionError(f"{escaped_name!r} not found in {hrefs_nonmatch!r}")

    current_name = notebook_frontend.evaluate("() => Jupyter.notebook.notebook_name", page=EDITOR_PAGE)
    assert current_name == nbname

    notebook_frontend.edit_cell(index=0, content="")
    notebook_frontend.delete_all_cells()
    
"""Test display isolation.

An object whose metadata contains an "isolated" tag must be isolated
from the rest of the document.
"""


from .utils import EDITOR_PAGE


def test_display_isolation(notebook_frontend):
    import_ln = "from IPython.core.display import HTML, SVG, display, display_svg"
    notebook_frontend.edit_cell(index=0, content=import_ln)
    notebook_frontend.execute_cell(0)
    try:
        isolated_html(notebook_frontend)
        isolated_svg(notebook_frontend)
    finally:
        # Ensure we switch from iframe back to default content even if test fails
        notebook_frontend._editor_page.main_frame  # TODO:


def isolated_html(notebook):
    """Test HTML display isolation.

    HTML styling rendered without isolation will affect the whole
    document, whereas styling applied with isolation will affect only
    the local display object.
    """
    red = 'rgb(255, 0, 0)'
    blue = 'rgb(0, 0, 255)'
    test_str = "<div id='test'>Should turn red from non-isolation</div>"
    notebook.add_and_execute_cell(content=f"display(HTML({test_str!r}))")
    non_isolated = (
        f"<style>div{{color:{red};}}</style>"
        f"<div id='non-isolated'>Should be red</div>")
    display_ni = f"display(HTML({non_isolated!r}), metadata={{'isolated':False}})"
    notebook.add_and_execute_cell(content=display_ni)
    isolated = (
        f"<style>div{{color:{blue};}}</style>"
        f"<div id='isolated'>Should be blue</div>")
    display_i = f"display(HTML({isolated!r}), metadata={{'isolated':True}})"
    notebook.add_and_execute_cell(content=display_i)

    # The non-isolated div will be in the body
    non_isolated_div = notebook.locate('#non-isolated', page=EDITOR_PAGE)
    assert non_isolated_div.get_computed_property('color') == red

    # The non-isolated styling will have affected the output of other cells
    test_div = notebook.locate('#test', page=EDITOR_PAGE)
    assert test_div.get_computed_property('color') == red

    # The isolated div will be in an iframe, only that element will be blue
    notebook.wait_for_frame(count=2, page=EDITOR_PAGE)
    isolated_div = notebook.locate_in_frame('#isolated', page=EDITOR_PAGE, frame_index=1)
    assert isolated_div.get_computed_property("color") == blue


def isolated_svg(notebook):
    """Test that multiple isolated SVGs have different scopes.

    Asserts that there no CSS leaks between two isolated SVGs.
    """
    yellow = "rgb(255, 255, 0)"
    black = "rgb(0, 0, 0)"
    svg_1_str = f"""s1 = '''<svg width="1cm" height="1cm" viewBox="0 0 1000 500"><defs><style>rect {{fill:{yellow};}}; </style></defs><rect id="r1" x="200" y="100" width="600" height="300" /></svg>'''"""
    svg_2_str = """s2 = '''<svg width="1cm" height="1cm" viewBox="0 0 1000 500"><rect id="r2" x="200" y="100" width="600" height="300" /></svg>'''"""

    notebook.add_and_execute_cell(content=svg_1_str)
    notebook.add_and_execute_cell(content=svg_2_str)
    notebook.add_and_execute_cell(
        content="display_svg(SVG(s1), metadata=dict(isolated=True))")
    notebook.add_and_execute_cell(
        content="display_svg(SVG(s2), metadata=dict(isolated=True))")
    iframes = notebook.wait_for_tag("iframe", page=EDITOR_PAGE)

    # The first rectangle will be red
    notebook.wait_for_frame(count=2, page=EDITOR_PAGE)
    isolated_svg_1 = notebook.locate_in_frame('#r1', page=EDITOR_PAGE, frame_index=2)
    assert isolated_svg_1.get_computed_property("fill") == yellow
    
    # The second rectangle will be black
    notebook.wait_for_frame(count=3, page=EDITOR_PAGE)
    isolated_svg_2 = notebook.locate_in_frame('#r2', page=EDITOR_PAGE, frame_index=3)
    assert isolated_svg_2.get_computed_property("fill") == black

    # Clean up the svg test cells
    for i in range(1, len(notebook.cells)):
        notebook.delete_cell(1)

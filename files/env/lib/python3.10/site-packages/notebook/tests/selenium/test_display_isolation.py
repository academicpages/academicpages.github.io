"""Test display isolation.

An object whose metadata contains an "isolated" tag must be isolated
from the rest of the document.
"""

from selenium.webdriver.common.by import By

from .utils import wait_for_tag


def test_display_isolation(notebook):
    import_ln = "from IPython.core.display import HTML, SVG, display, display_svg"
    notebook.edit_cell(index=0, content=import_ln)
    notebook.execute_cell(notebook.current_cell)
    try:
        isolated_html(notebook)
        isolated_svg(notebook)
    finally:
        # Ensure we switch from iframe back to default content even if test fails
        notebook.browser.switch_to.default_content()


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

    iframe = wait_for_tag(notebook.browser, "iframe", single=True)

    # The non-isolated div will be in the body
    non_isolated_div = notebook.body.find_element(By.ID, "non-isolated")
    assert non_isolated_div.value_of_css_property("color") == red

    # The non-isolated styling will have affected the output of other cells
    test_div = notebook.body.find_element(By.ID, "test")
    assert test_div.value_of_css_property("color") == red

    # The isolated div will be in an iframe, only that element will be blue
    notebook.browser.switch_to.frame(iframe)
    isolated_div = notebook.browser.find_element(By.ID, "isolated")
    assert isolated_div.value_of_css_property("color") == blue
    notebook.browser.switch_to.default_content()
    # Clean up the html test cells
    for i in range(1, len(notebook.cells)):
        notebook.delete_cell(1)


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
    iframes = wait_for_tag(notebook.browser, "iframe", wait_for_n=2)

    # The first rectangle will be red
    notebook.browser.switch_to.frame(iframes[0])
    isolated_svg_1 = notebook.browser.find_element(By.ID, 'r1')
    assert isolated_svg_1.value_of_css_property("fill") == yellow
    notebook.browser.switch_to.default_content()

    # The second rectangle will be black
    notebook.browser.switch_to.frame(iframes[1])
    isolated_svg_2 = notebook.browser.find_element(By.ID, 'r2')
    assert isolated_svg_2.value_of_css_property("fill") == black

    # Clean up the svg test cells
    for i in range(1, len(notebook.cells)):
        notebook.delete_cell(1)

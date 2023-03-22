"""Test multiselect toggle

TODO: This changes the In []: label preceding the cell,
      what's the purpose of this? Update the docstring
"""


def test_prompt_numbers(prefill_notebook):
    notebook_frontend = prefill_notebook(['print("a")'])

    def get_prompt():
        return (
            notebook_frontend.cells[0].locate('.input')
            .locate('.input_prompt')
            .get_inner_html().strip()
        )

    def set_prompt(value):
        notebook_frontend.set_cell_input_prompt(0, value)

    assert get_prompt() == "<bdi>In</bdi>&nbsp;[&nbsp;]:"

    set_prompt(2)
    assert get_prompt() == "<bdi>In</bdi>&nbsp;[2]:"

    set_prompt(0)
    assert get_prompt() == "<bdi>In</bdi>&nbsp;[0]:"

    set_prompt("'*'")
    assert get_prompt() == "<bdi>In</bdi>&nbsp;[*]:"

    set_prompt("undefined")
    assert get_prompt() == "<bdi>In</bdi>&nbsp;[&nbsp;]:"

    set_prompt("null")
    assert get_prompt() == "<bdi>In</bdi>&nbsp;[&nbsp;]:"

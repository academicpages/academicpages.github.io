INITIAL_CELLS = ["hello", "hellohello", "abc", "ello"]

def test_find_and_replace(prefill_notebook):
    """ test find and replace on all the cells """
    notebook = prefill_notebook(INITIAL_CELLS)

    find_str = "ello"
    replace_str = "foo"

    # replace the strings
    notebook.find_and_replace(index=0, find_txt=find_str, replace_txt=replace_str)

    # check content of the cells
    assert notebook.get_cells_contents() == [
        s.replace(find_str, replace_str) for s in INITIAL_CELLS
    ]

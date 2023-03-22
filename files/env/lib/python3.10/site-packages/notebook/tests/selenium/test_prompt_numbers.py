from selenium.webdriver.common.by import By


def test_prompt_numbers(prefill_notebook):
    notebook = prefill_notebook(['print("a")'])

    def get_prompt():
        return (
            notebook.cells[0].find_element(By.CLASS_NAME, 'input')
            .find_element(By.CLASS_NAME, 'input_prompt')
            .get_attribute('innerHTML').strip()
        )

    def set_prompt(value):
        notebook.set_cell_input_prompt(0, value)

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

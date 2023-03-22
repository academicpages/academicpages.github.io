"""Test display of images

The effect of shape metadata is validated, using Image(retina=True)
"""

from selenium.webdriver.common.by import By

from .utils import wait_for_tag


# 2x2 black square in b64 jpeg and png
b64_image_data = {
    "image/png" : b'iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAC0lEQVR4nGNgQAYAAA4AAamRc7EA\\nAAAASUVORK5CYII',
    "image/jpeg" : b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a\nHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy\nMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAACAAIDASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/ooo\noAoo2Qoo'
}


def imports(notebook):
    commands = [
        'import base64',
        'from IPython.display import display, Image',
    ]
    notebook.edit_cell(index=0, content="\n".join(commands))
    notebook.execute_cell(0)


def validate_img(notebook, cell_index, image_fmt, retina):
    """Validate that image renders as expected."""

    b64data = b64_image_data[image_fmt]
    commands = [
        f'b64data = {b64data}',
        'data = base64.decodebytes(b64data)',
        f'display(Image(data, retina={retina}))'
    ]
    notebook.append("\n".join(commands))
    notebook.execute_cell(cell_index)

    # Find the image element that was just displayed
    wait_for_tag(notebook.cells[cell_index], "img", single=True)
    img_element = notebook.cells[cell_index].find_element(By.TAG_NAME, "img")

    src = img_element.get_attribute("src")
    prefix = src.split(',')[0]
    expected_prefix = f"data:{image_fmt};base64"
    assert prefix == expected_prefix

    expected_size = 1 if retina else 2
    assert img_element.size["width"] == expected_size
    assert img_element.size["height"] == expected_size
    assert img_element.get_attribute("width") == str(expected_size)
    assert img_element.get_attribute("height") == str(expected_size)


def test_display_image(notebook):
    imports(notebook)
    # PNG, non-retina
    validate_img(notebook, 1, "image/png", False)

    # PNG, retina display
    validate_img(notebook, 2, "image/png", True)

    # JPEG, non-retina
    validate_img(notebook, 3, "image/jpeg", False)

    # JPEG, retina display
    validate_img(notebook, 4, "image/jpeg", True)

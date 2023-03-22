"""Test display of images

The effect of shape metadata is validated, using Image(retina=True)
"""


import re


# 2x2 black square in b64 jpeg and png
b64_image_data = {
    "image/png": b'iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAC0lEQVR4nGNgQAYAAA4AAamRc7EA\\nAAAASUVORK5CYII',
    "image/jpeg": b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a\nHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy\nMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAACAAIDASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/ooo\noAoo2Qoo'
}


def imports(notebook_frontend):
    commands = [
        'import base64',
        'from IPython.display import display, Image',
    ]
    notebook_frontend.edit_cell(index=0, content="\n".join(commands))
    notebook_frontend.execute_cell(0)


def validate_img(notebook_frontend, cell_index, image_fmt, retina):
    """Validate that image renders as expected."""

    # Show our test image in the notebook
    b64data = b64_image_data[image_fmt]
    commands = [
        f'b64data = {b64data}',
        'data = base64.decodebytes(b64data)',
        f'display(Image(data, retina={retina}))'
    ]
    notebook_frontend.append("\n".join(commands))
    notebook_frontend.execute_cell(cell_index)

    # Find the image element that was just displayed
    img_element = notebook_frontend.wait_for_tag("img", cell_index=cell_index)

    # Check image format
    src = img_element.get_attribute("src")
    prefix = src.split(',')[0]
    expected_prefix = f"data:{image_fmt};base64"
    assert prefix == expected_prefix

    # JS for obtaining img element dimensions
    computed_width_js = ("(element) => { return window.getComputedStyle(element)"
                         ".getPropertyValue('width') }")
    computed_height_js = ("(element) => { return window.getComputedStyle(element)"
                         ".getPropertyValue('height') }")

    # Obtain digit only string values for width/height
    computed_width_raw = img_element.evaluate(computed_width_js)
    computed_height_raw = img_element.evaluate(computed_height_js)
    computed_width = re.search(r'[0-9]+', computed_width_raw)
    computed_height = re.search(r'[0-9]+', computed_height_raw)
    computed_width = None if computed_width is None else computed_width.group(0)
    computed_height = None if computed_height is None else computed_height.group(0)

    # Check image dimensions
    expected_size = "1" if retina else "2"
    assert computed_width == expected_size
    assert computed_height == expected_size


def test_display_image(notebook_frontend):
    imports(notebook_frontend)
    # PNG, non-retina
    validate_img(notebook_frontend, 1, "image/png", False)

    # PNG, retina display
    validate_img(notebook_frontend, 2, "image/png", True)

    # JPEG, non-retina
    validate_img(notebook_frontend, 3, "image/jpeg", False)

    # JPEG, retina display
    validate_img(notebook_frontend, 4, "image/jpeg", True)

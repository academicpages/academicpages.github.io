"""Test the notification area and widgets"""


import pytest
from .utils import EDITOR_PAGE


def get_widget(notebook, name):
    return notebook.evaluate(
        f"() => {{ return IPython.notification_area.get_widget('{name}') !== undefined }}",
        page=EDITOR_PAGE
    )


def widget(notebook, name):
    return notebook.evaluate(
        f"() => {{ return IPython.notification_area.widget('{name}') !== undefined }}",
        page=EDITOR_PAGE
    )


def new_notification_widget(notebook, name):
    return notebook.evaluate(
        f"() => {{ return IPython.notification_area.new_notification_widget('{name}') !== undefined }}",
        page=EDITOR_PAGE
    )


def widget_has_class(notebook, name, class_name):
    return notebook.evaluate(
        f"""() => {{
        var w = IPython.notification_area.get_widget('{name}');
        return w.element.hasClass('{class_name}'); }}
        """,
        page=EDITOR_PAGE
    )


def widget_message(notebook, name):
    return notebook.evaluate(
        f"""() => {{
        var w = IPython.notification_area.get_widget('{name}');
        return w.get_message(); }}
        """,
        page=EDITOR_PAGE
    )


def test_notification(notebook_frontend):
    # check that existing widgets are there
    assert get_widget(notebook_frontend, "kernel") and widget(notebook_frontend, "kernel"),\
        "The kernel notification widget exists"
    assert get_widget(notebook_frontend, "notebook") and widget(notebook_frontend, "notebook"),\
        "The notebook notification widget exists"

    # try getting a non-existent widget
    with pytest.raises(Exception):
        get_widget(notebook_frontend, "foo")

    # try creating a non-existent widget
    assert widget(notebook_frontend, "bar"), "widget: new widget is created"

    # try creating a widget that already exists
    with pytest.raises(Exception):
        new_notification_widget(notebook_frontend, "kernel")

    # test creating 'info', 'warning' and 'danger' messages
    for level in ("info", "warning", "danger"):
        notebook_frontend.evaluate(
            f"""
            var tnw = IPython.notification_area.widget('test');
            tnw.{level}('test {level}');
            """,
            page=EDITOR_PAGE
        )
        notebook_frontend.wait_for_selector("#notification_test", page=EDITOR_PAGE)

        assert widget_has_class(notebook_frontend, "test", level), f"{level}: class is incorrect"
        assert widget_message(notebook_frontend, "test") == f"test {level}", f"{level}: message is incorrect"

    # test message timeout
    notebook_frontend.evaluate(
        """
        var tnw = IPython.notification_area.widget('test');
        tnw.set_message('test timeout', 1000);
        """,
        page=EDITOR_PAGE
    )
    notebook_frontend.wait_for_selector("#notification_test", page=EDITOR_PAGE)
    assert widget_message(notebook_frontend, "test") == "test timeout", "timeout: message is incorrect"

    notebook_frontend.wait_for_selector("#notification_test", EDITOR_PAGE, state='hidden')
    assert widget_message(notebook_frontend, "test") == "", "timeout: message was not cleared"

    # test click callback
    notebook_frontend.evaluate(
        """
        var tnw = IPython.notification_area.widget('test');
        tnw._clicked = false;
        tnw.set_message('test click', undefined, function () {
            tnw._clicked = true;
            return true;
        });
        """,
        page=EDITOR_PAGE
    )
    notebook_frontend.locate("#notification_test", page=EDITOR_PAGE)
    assert widget_message(notebook_frontend, "test") == "test click", "callback: message is correct"

    notebook_frontend.locate("#notification_test", page=EDITOR_PAGE).click()
    notebook_frontend.wait_for_condition(
        lambda: notebook_frontend.evaluate(
            '() => { return IPython.notification_area.widget("test")._clicked; }', page=EDITOR_PAGE
        )
    )

    notebook_frontend.wait_for_selector("#notification_test", EDITOR_PAGE, state='hidden')
    assert widget_message(notebook_frontend, "test") == "", "callback: message was not cleared"

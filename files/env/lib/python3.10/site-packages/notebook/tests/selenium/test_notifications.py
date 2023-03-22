"""
Test the notification area and widgets
"""
import pytest
from selenium.webdriver.common.by import By

from .utils import wait_for_selector, wait_for_script_to_return_true


def get_widget(notebook, name):
    return notebook.browser.execute_script(
        f"return IPython.notification_area.get_widget('{name}') !== undefined"
    )


def widget(notebook, name):
    return notebook.browser.execute_script(
        f"return IPython.notification_area.widget('{name}') !== undefined"
    )


def new_notification_widget(notebook, name):
    return notebook.browser.execute_script(
        f"return IPython.notification_area.new_notification_widget('{name}') !== undefined"
    )


def widget_has_class(notebook, name, class_name):
    return notebook.browser.execute_script(
        f"""
        var w = IPython.notification_area.get_widget('{name}');
        return w.element.hasClass('{class_name}');
        """
    )


def widget_message(notebook, name):
    return notebook.browser.execute_script(
        f"""
        var w = IPython.notification_area.get_widget('{name}');
        return w.get_message();
        """
    )


def test_notification(notebook):
    # check that existing widgets are there
    assert get_widget(notebook, "kernel") and widget(notebook, "kernel"),\
        "The kernel notification widget exists"
    assert get_widget(notebook, "notebook") and widget(notebook, "notebook"),\
        "The notebook notification widget exists"

    # try getting a non-existent widget
    with pytest.raises(Exception):
        get_widget(notebook, "foo")

    # try creating a non-existent widget
    assert widget(notebook, "bar"), "widget: new widget is created"

    # try creating a widget that already exists
    with pytest.raises(Exception):
        new_notification_widget(notebook, "kernel")

    # test creating 'info', 'warning' and 'danger' messages
    for level in ("info", "warning", "danger"):
        notebook.browser.execute_script(f"""
            var tnw = IPython.notification_area.widget('test');
            tnw.{level}('test {level}');
        """)
        wait_for_selector(notebook.browser, "#notification_test", visible=True)

        assert widget_has_class(notebook, "test", level), f"{level}: class is correct"
        assert widget_message(notebook, "test") == f"test {level}", f"{level}: message is correct"

    # test message timeout
    notebook.browser.execute_script("""
        var tnw = IPython.notification_area.widget('test');
        tnw.set_message('test timeout', 1000);
        """)
    wait_for_selector(notebook.browser, "#notification_test", visible=True)

    assert widget_message(notebook, "test") == "test timeout", "timeout: message is correct"
    wait_for_selector(notebook.browser, "#notification_test", obscures=True)
    assert widget_message(notebook, "test") == "", "timeout: message was cleared"

    # test click callback
    notebook.browser.execute_script("""
        var tnw = IPython.notification_area.widget('test');
        tnw._clicked = false;
        tnw.set_message('test click', undefined, function () {
            tnw._clicked = true;
            return true;
        });
        """)
    wait_for_selector(notebook.browser, "#notification_test", visible=True)

    assert widget_message(notebook, "test") == "test click", "callback: message is correct"

    notebook.browser.find_element(By.ID, "notification_test").click()
    wait_for_script_to_return_true(notebook.browser,
                                   'return IPython.notification_area.widget("test")._clicked;')
    wait_for_selector(notebook.browser, "#notification_test", obscures=True)

    assert widget_message(notebook, "test") == "", "callback: message was cleared"

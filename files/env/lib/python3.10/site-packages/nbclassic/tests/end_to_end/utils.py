"""Utility module for end_to_end testing.

The primary utilities are:
    * NotebookFrontend
    * FrontendElement

Users should use these utilities to write their tests,
and avoid calling the underlying testing library directly.
If you need to do something that isn't currently available,
try to build it onto the utility classes instead of using
playwright functionality/objects directly.

This module was converted and refactored from the older
selenium test suite.
"""
import copy
import datetime
import os
import time
import traceback

from playwright.sync_api import ElementHandle, JSHandle
from playwright.sync_api import expect


# Key constants for browser_data
BROWSER_CONTEXT = 'BROWSER_CONTEXT'
TREE_PAGE = 'TREE_PAGE'
EDITOR_PAGE = 'EDITOR_PAGE'
SERVER_INFO = 'SERVER_INFO'
BROWSER_OBJ = 'BROWSER_OBJ'
# Other constants
CELL_OUTPUT_SELECTOR = '.output_subarea'


class TimeoutError(Exception):

    def get_result(self):
        return None if not self.args else self.args[0]


class CellTypeError(ValueError):

    def __init__(self, message=""):
        self.message = message


class FrontendError(Exception):
    pass


class FrontendElement:
    """Performs high level tasks on frontend interface components

    FrontendElement serves these goals:
    - Offers some abstraction/hiding of the underlying testing
      library (with the goal of making future refactors easier
      through providing a single point of reimplementation via
      this utility class rather than exposing implementation
      details of the web library to individual tests)
    - Unifies disparate library syntax for common functionalities

    FrontendElement wraps JSHandle, Locator and ElementHandle from
    playwright, and provides a unified endpoint for test writers
    to grab attributes, inner text, find child elements etc.
    """

    def __init__(self, item, user_data=None):
        """Wrap a frontend item.

        :param item: JSHandle, Locator or ElementHandle
        :param user_data: Mainly intended to hold cell data (like cell index),
            pass a dict in and put what you want inside.
        """
        self._raw = item
        self._element = item
        self._bool = True  # Was the item created successfully?
        self._user_data = {} if user_data is None else user_data

        # We need either a locator or an ElementHandle for most ops, obtain it
        if item is None:
            self._bool = False
        if hasattr(item, 'count') and item.count() == 0:
            self._bool = False
        if not isinstance(item, ElementHandle) and isinstance(item, JSHandle):
            as_element = item.as_element()
            if as_element:
                self._element = as_element
            else:
                self._bool = False
        if isinstance(item, FrontendElement):
            self._raw = item
            self._element = item._element
            self._bool = item._bool
            self._user_data = copy.deepcopy(item._user_data)
            self._user_data.update(user_data)

    def __bool__(self):
        """Returns True if construction succeeded"""
        # (Quick/dirty )We can debug on failures by deferring bad inits and testing for them here
        return self._bool

    def click(self):
        return self._element.click()

    def get_inner_text(self):
        return self._element.inner_text()

    def get_inner_html(self):
        return self._element.inner_html()

    def get_attribute(self, attribute):
        return self._element.get_attribute(attribute)

    def get_computed_property(self, prop_name):
        js = ("(element) => { return window.getComputedStyle(element)"
              f".getPropertyValue('{prop_name}') }}")
        return self._element.evaluate(js)

    def evaluate(self, text):
        return self._element.evaluate(text)

    def wait_for(self, state):
        if hasattr(self._element, 'wait_for_element_state'):
            return self._element.wait_for_element_state(state=state)
        elif hasattr(self._element, 'wait_for'):
            return self._element.wait_for(state=state)
        else:
            raise FrontendError('Could not wait for state on element')

    def focus(self):
        self._element.focus()

    def locate(self, selector):
        """Locate child elements with the given selector"""
        element = self._element

        if hasattr(element, 'locator'):
            result = element.locator(selector)
        elif hasattr(element, 'query_selector'):
            result = element.query_selector(selector)
        else:
            # TODO: FIX these - Raise exception or return None
            result = None

        return FrontendElement(result)

    def locate_all(self, selector):
        """Locate all child elements with the given selector"""
        element = self._element

        if hasattr(element, 'query_selector_all'):
            matches = element.query_selector_all(selector)
            element_list = [FrontendElement(item) for item in matches]
        elif hasattr(element, 'locator'):
            matches = element.locator(selector)
            element_list = [FrontendElement(matches.nth(index)) for index in range(matches.count())]
        else:
            # TODO: FIX these - Raise exception or return None
            element_list = None

        return element_list

    def type(self, text):
        """Sends the given text as key presses to the element"""
        return self._element.type(text)

    def press(self, key):
        """Send a key press to the element"""
        return self._element.press(key)

    def get_user_data(self):
        """Currently this is an unmanaged user data area, use it as you please"""
        return self._user_data

    def expect_not_to_be_visible(self):
        try:
            expect(self._element).not_to_be_visible()
        except ValueError as err:
            raise Exception('Cannot expect not_to_be_visible on this type!') from err

    def expect_to_have_text(self, text):
        try:
            expect(self._element).to_have_text(text)
        except ValueError as err:
            raise Exception('Cannot expect to have text on this type!') from err

    def is_visible(self):
        return self._element.is_visible()


class NotebookFrontend:
    """Performs high level Notebook tasks for automated testing.

    NotebookFrontend serves these goals:
    - Drives high level application tasks for testing
    - Offers some encapsulation of the underlying testing
      library, to allow test writers to focus their efforts
      on application features rather than implementation
      details for any given testing task

    NotebookFrontend holds a _tree_page (Jupyter file browser), and
    an _editor_page (a Python 3 notebook editor page), with the goal
    of allowing test writers to drive any desired application tasks,
    with the option of selecting a page in most methods.

    Many tasks are accomplished by using the evaluate method to run
    frontend Jupyter Javascript code on a selected page.

    A cells property returns a list of the current notebook cells.

    Other design notes: This class works together with FrontendElement
    to abstract the testing library implementation away from test
    writers. NotebookFrontend holds (private) handles to the underlying
    browser/context.

    TODO:
    Possible future improvements, current limitations, etc
    """

    # Some constants for users of the class
    TREE_PAGE = TREE_PAGE
    EDITOR_PAGE = EDITOR_PAGE
    CELL_OUTPUT_SELECTOR = CELL_OUTPUT_SELECTOR

    def __init__(self, browser_data, existing_file_name=None):
        """Start the Notebook app via the web UI or from a file.

        If an existing_file_name is provided, the web interface
        looks for and clicks the notebook entry in the tree page.
        If not, the web interface will start a new Python3 notebook
        from the kernel selection menu.

        :param browser_data: Interfacing object to the web UI
        :param str existing_file_name: An existing notebook filename to open
        """
        # Keep a reference to source data
        self._browser_data = browser_data

        # Define tree and editor attributes
        self._tree_page = browser_data[TREE_PAGE]
        self._editor_page = self._open_notebook_editor_page(existing_file_name)

        # Do some needed frontend setup
        self._wait_for_start()
        self.disable_autosave_and_onbeforeunload()
        self.current_cell = None  # Defined/used below  # TODO refactor/remove

    def _wait_for_start(self):
        """Wait until the notebook interface is loaded and the kernel started"""
        def check_is_kernel_running():
            try:
                status = (self.is_jupyter_defined()
                        and self.is_notebook_defined()
                        and self.is_kernel_running())
            except Exception:
                return False

            return status

        self.wait_for_condition(check_is_kernel_running)

    @property
    def body(self):
        return self._editor_page.locator("body")

    @property
    def _cells(self):
        """Return a list of the current Notebook cells."""
        return self._editor_page.query_selector_all(".cell")

    @property
    def cells(self):
        """User facing cell list, gives a list of FrontendElement's"""
        cells = [
            FrontendElement(cell, user_data={'index': index})
            for index, cell in enumerate(self._cells)
        ]

        return cells

    @property
    def current_index(self):
        return self.index(self.current_cell)

    def index(self, cell):
        return self._cells.index(cell)

    def press(self, keycode, page, modifiers=None):
        """Press a key on the specified page

        :param str keycode: The keycode value, see MDN
        :param str page: The page name to run on
        :param modifiers: A list of modifier keycode strings to press
        """
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        mods = ""
        if modifiers is not None:
            mods = "+".join(m for m in modifiers)
            mods += "+"

        specified_page.keyboard.press(mods + keycode)

    def type(self, text, page):
        """Mimics a user typing the given text on the specified page"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')
        specified_page.keyboard.type(text)

    def insert_text(self, text, page):
        """ """
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        specified_page.keyboard.insert_text(text)

    def press_active(self, keycode, modifiers=None):
        """Press a key on the current_cell"""
        mods = ""
        if modifiers is not None:
            mods = "+".join(m for m in modifiers)
            mods += "+"

        self.current_cell.press(mods + keycode)

    def type_active(self, text):
        """Mimics a user typing the given text on the current_cell"""
        self.current_cell.type(text)

    def try_click_selector(self, selector, page):
        """Attempts to find and click an element with the selector on the given page"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')
        elem = specified_page.locator(selector)

        elem.click()

    def wait_for_selector(self, selector, page, state=None):
        """Wait for the given selector (in the given state) on the specified page"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')
        if state is not None:
            return FrontendElement(specified_page.wait_for_selector(selector, state=state))

        return FrontendElement(specified_page.wait_for_selector(selector))

    def get_platform_modifier_key(self):
        """Jupyter Notebook uses different modifier keys on win (Control) vs mac (Meta)"""
        if os.uname()[0] == "Darwin":
            return "Meta"
        else:
            return "Control"

    def evaluate(self, text, page):
        """Run some Javascript on the frontend in the given page

        :param text: JS to evaluate
        :param page: Page (str constant) to evaluate JS in
        :return: The result of the evaluated JS
        """
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        return specified_page.evaluate(text)

    def _pause(self):
        self._editor_page.pause()

    def locate(self, selector, page):
        """Find an element matching selector on the given page"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to locate from!')

        return FrontendElement(specified_page.locator(selector))

    def locate_all(self, selector, page):
        """Find a list of elements matching the selector on the given page"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to locate from!')

        # Get a locator, make a list of FrontendElement's for each match
        result = specified_page.locator(selector)
        element_list = [FrontendElement(result.nth(index)) for index in range(result.count())]
        return element_list

    def locate_and_focus(self, selector, page):
        """Find selector in page and focus"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to locate from!')

        locator = specified_page.locator(selector)
        locator.focus()
        return FrontendElement(locator)

    def wait_for_frame(self, count=None, name=None, page=None):
        """Waits for availability of a frame with the given name"""
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to wait for frame from!')

        if name is not None:
            def frame_wait():
                frames = [f for f in specified_page.frames if f.name == name]
                return frames
        if count is not None:
            def frame_wait():
                frames = [f for f in specified_page.frames]
                return len(frames) >= count

        self.wait_for_condition(frame_wait)

    def locate_in_frame(self, selector, page, frame_name=None, frame_index=None):
        """Finds an element inside a frame"""
        if frame_name is None and frame_index is None:
            raise Exception('Error, must provide a frame name or frame index!')
        if frame_name is not None and frame_index is not None:
            raise Exception('Error, provide only one either frame name or frame index!')

        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to locate in frame from!')

        if frame_name is not None:
            frame_matches = [f for f in specified_page.frames if f.name == frame_name]
            if not frame_matches:
                raise Exception('No frames found!')
            frame = frame_matches[0]
        if frame_index is not None:
            frame = specified_page.frames[frame_index]

        element = frame.wait_for_selector(selector)
        return FrontendElement(element)

    def wait_for_tag(self, tag, page=None, cell_index=None):
        """Waits for availability of a given tag on the page"""
        if cell_index is None and page is None:
            raise FrontendError('Provide a page or cell to wait from!')
        if cell_index is not None and page is not None:
            raise FrontendError('Provide only one of [page, cell] to wait from!')

        result = None
        if page is not None:
            if page == TREE_PAGE:
                specified_page = self._tree_page
            elif page == EDITOR_PAGE:
                specified_page = self._editor_page
            else:
                raise Exception('Error, provide a valid page to evaluate from!')

            result = specified_page.locator(tag)
        if cell_index is not None:
            result = self._cells[cell_index].wait_for_selector(tag)

        return FrontendElement(result)

    # TODO remove this
    def _locate(self, selector, page):
        """Find an frontend element by selector (Tag, CSS, XPath etc.)"""
        result = None
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        return specified_page.locator(selector)

    def clear_all_output(self):
        """Clear all cell outputs"""
        return self.evaluate(
            "Jupyter.notebook.clear_all_output();",
            page=EDITOR_PAGE
        )

    def clear_cell_output(self, index):
        """Clear single cell output"""
        JS = f'Jupyter.notebook.clear_output({index})'
        self.evaluate(JS, page=EDITOR_PAGE)

    def delete_all_cells(self):
        # Note: After deleting all cells, a single default cell will remain

        for _ in range(len(self._cells)):
            self.delete_cell(0)

    def populate(self, cell_texts):
        """Delete all cells, then add cells using the list of specified cell_texts"""
        self.delete_all_cells()

        for _ in range(len(cell_texts) - 1):  # Remove 1, there will already be 1 default cell
            self.add_cell()
        for index, txt in enumerate(cell_texts):
            self.edit_cell(None, index, txt)

    def click_toolbar_execute_btn(self):
        """Mimics a user pressing the execute button in the UI"""
        execute_button = self._editor_page.locator(
            "button["
                "data-jupyter-action="
                    "'jupyter-notebook:run-cell-and-select-next'"
            "]"
        )
        execute_button.click()

    def disable_autosave_and_onbeforeunload(self):
        """Disable request to save before closing window and autosave.

        This is most easily done by using js directly.
        """
        self.evaluate("window.onbeforeunload = null;", page=EDITOR_PAGE)
        self.evaluate("Jupyter.notebook.set_autosave_interval(0)", page=EDITOR_PAGE)

    def to_command_mode(self):
        """Changes us into command mode on currently focused cell"""
        self.body.press('Escape')
        self.evaluate(" () => { return Jupyter.notebook.handle_command_mode("
                                       "Jupyter.notebook.get_cell("
                                           "Jupyter.notebook.get_edit_index())) }", page=EDITOR_PAGE)

    def focus_cell(self, index=0):
        """Mimic a user focusing on the given cell"""
        cell = self._cells[index]
        cell.click()
        self.to_command_mode()
        self.current_cell = cell

    def select_cell_range(self, initial_index=0, final_index=0):
        self.focus_cell(initial_index)
        self.to_command_mode()
        for i in range(final_index - initial_index):
            self.press('j', EDITOR_PAGE, ['Shift'])

    def find_and_replace(self, index=0, find_txt='', replace_txt=''):
        """Uses Jupyter's find and replace"""
        self.focus_cell(index)
        self.to_command_mode()
        self.press('f', EDITOR_PAGE)
        self._editor_page.locator('#find-and-replace')
        self._editor_page.locator('#findreplace_allcells_btn').click()
        find_input = self.locate('#findreplace_find_inp', page=EDITOR_PAGE)
        # find and replace fields are HTML input elements, use .value to get/set text
        find_input.evaluate(f"(elem) => {{ elem.value = '{find_txt}'; return elem.value; }}")
        self.wait_for_condition(
            lambda: find_input.evaluate(
                '(elem) => { return elem.value; }') == find_txt,
            timeout=30,
            period=5
        )
        rep_input = self.locate('#findreplace_replace_inp', page=EDITOR_PAGE)
        rep_input.evaluate(f"(elem) => {{ elem.value = '{replace_txt}'; return elem.value; }}")
        self.wait_for_condition(
            lambda: rep_input.evaluate('(elem) => { return elem.value; }') == replace_txt,
            timeout=30,
            period=5
        )
        self._editor_page.locator('#findreplace_replaceall_btn').click()

    def convert_cell_type(self, index=0, cell_type="code"):
        # TODO add check to see if it is already present
        self.focus_cell(index)
        cell = self._cells[index]
        if cell_type == "markdown":
            self.current_cell.press("m")
        elif cell_type == "raw":
            self.current_cell.press("r")
        elif cell_type == "code":
            self.current_cell.press("y")
        else:
            raise CellTypeError(f"{cell_type} is not a valid cell type,use 'code', 'markdown', or 'raw'")

        self._wait_for_stale_cell(cell)
        self.focus_cell(index)
        return self.current_cell

    def _wait_for_stale_cell(self, cell):
        """ This is needed to switch a cell's mode and refocus it, or to render it.

        Warning: there is currently no way to do this when changing between
        markdown and raw cells.
        """
        cell.wait_for_element_state('hidden')

    def get_cells_contents(self):
        """Get a list of the text inside each cell"""
        JS = '() => { return Jupyter.notebook.get_cells().map(function(c) {return c.get_text();}) }'
        return self.evaluate(JS, page=EDITOR_PAGE)

    def get_cell_contents(self, index=0, selector='div .CodeMirror-code'):
        """Get the text inside a given cell"""
        return self._cells[index].query_selector(selector).inner_text()

    def get_cell_output(self, index=0, output=CELL_OUTPUT_SELECTOR):
        """Get the cell output for a given cell"""
        cell = self._cells[index].as_element().query_selector(output)  # Find cell child elements

        if cell is None:
            return None

        element = FrontendElement(cell, user_data={'index': index})

        return element

    def wait_for_condition(self, check_func, timeout=30, period=.1):
        """Wait for check_func to return a truthy value, return it or raise an exception upon timeout"""
        # TODO refactor/remove

        begin = datetime.datetime.now()
        while (datetime.datetime.now() - begin).seconds < timeout:
            try:
                condition = check_func()
                if condition:
                    return condition
                time.sleep(period)
            except Exception as err:
                # Log (print) exception and continue
                traceback.print_exc()
                print('\n[NotebookFrontend] Ignoring exception in wait_for_condition, read more above')
        else:
            raise TimeoutError()

    def wait_for_cell_output(self, index=0, timeout=30):
        """Waits for the cell to finish executing and return the cell output"""
        if not self._cells:
            raise Exception('Error, no cells exist!')

        milliseconds_to_seconds = 1000
        cell = self._cells[index].as_element()
        try:
            cell.wait_for_selector(CELL_OUTPUT_SELECTOR, timeout=timeout * milliseconds_to_seconds)
        except Exception:
            # None were found / timeout
            pass

        return self.get_cell_output(index=index)

    def set_cell_metadata(self, index, key, value):
        JS = f'Jupyter.notebook.get_cell({index}).metadata.{key} = {value}'
        return self.evaluate(JS, page=EDITOR_PAGE)

    def get_cell_type(self, index=0):
        JS = f'() => {{ return Jupyter.notebook.get_cell({index}).cell_type }}'
        return self.evaluate(JS, page=EDITOR_PAGE)

    def set_cell_input_prompt(self, index, prmpt_val):
        JS = f'Jupyter.notebook.get_cell({index}).set_input_prompt({prmpt_val})'
        self.evaluate(JS, page=EDITOR_PAGE)

    def edit_cell(self, cell=None, index=0, content="", render=False):
        """Set the contents of a cell to *content*, by cell object or by index
        """
        if cell is not None:
            index = self.index(cell)
        self.focus_cell(index)

        # Select & delete anything already in the cell
        self.press('Enter', EDITOR_PAGE)
        self.press('a', EDITOR_PAGE, [self.get_platform_modifier_key()])
        self.press('Delete', EDITOR_PAGE)

        self.type(content, page=EDITOR_PAGE)
        if render:
            self.execute_cell(index)

    def execute_cell(self, cell_or_index=None):
        if isinstance(cell_or_index, int):
            index = cell_or_index
        elif isinstance(cell_or_index, ElementHandle):
            # TODO: This probably doesn't work, fix/check
            index = self.index(cell_or_index)
        else:
            raise TypeError("execute_cell only accepts an ElementHandle or an int")
        self.focus_cell(index)
        self.current_cell.press("Control+Enter")

    def add_cell(self, index=-1, cell_type="code", content=""):
        # TODO fix/respect cell_type arg
        self.focus_cell(index)
        self.current_cell.press("b")
        new_index = index + 1 if index >= 0 else index
        if content:
            self.edit_cell(index=index, content=content)
        if cell_type != 'code':
            self.convert_cell_type(index=new_index, cell_type=cell_type)

    def add_and_execute_cell(self, index=-1, cell_type="code", content=""):
        self.add_cell(index=index, cell_type=cell_type, content=content)
        self.execute_cell(index)

    def delete_cell(self, index):
        self.focus_cell(index)
        self.to_command_mode()
        self.current_cell.type('dd')

    def add_markdown_cell(self, index=-1, content="", render=True):
        self.add_cell(index, cell_type="markdown")
        self.edit_cell(index=index, content=content, render=render)

    def append(self, *values, cell_type="code"):
        for value in values:
            if isinstance(value, str):
                self.add_cell(cell_type=cell_type,
                              content=value)
            else:
                raise TypeError(f"Don't know how to add cell from {value!r}")

    def is_jupyter_defined(self):
        """Checks that the Jupyter object is defined on the frontend"""
        return self.evaluate(
            "() => {"
            "  try {"
            "    return Jupyter != false;"
            "  } catch (e) {"
            "    return false;"
            "  }"
            "}",
            page=EDITOR_PAGE
        )

    def is_notebook_defined(self):
        """Checks that the Jupyter.notebook object is defined on the frontend"""
        return self.evaluate(
            "() => {"
            "  try {"
            "    return Jupyter.notebook != false;"
            "  } catch (e) {"
            "    return false;"
            "  }"
            "}",
            page=EDITOR_PAGE
        )

    def is_kernel_running(self):
        return self.evaluate(
            "() => { return Jupyter.notebook.kernel && Jupyter.notebook.kernel.is_connected() }",
            page=EDITOR_PAGE
        )

    def wait_for_kernel_ready(self):
        self._editor_page.wait_for_selector(".kernel_idle_icon")

    def _open_notebook_editor_page(self, existing_file_name=None):
        tree_page = self._tree_page

        if existing_file_name is not None:
            existing_notebook = tree_page.locator(f"text={existing_file_name}")
            existing_notebook.click()
            self._tree_page.reload()  # TODO: FIX this, page count does not update to 2
        else:
            # Simulate a user opening a new notebook/kernel
            new_dropdown_element = tree_page.locator('#new-dropdown-button')
            new_dropdown_element.click()
            kernel_name = 'kernel-python3'
            kernel_selector = f'#{kernel_name} a'
            new_notebook_element = tree_page.locator(kernel_selector)
            new_notebook_element.click()

        def wait_for_new_page():
            return [pg for pg in self._browser_data[BROWSER_CONTEXT].pages if 'tree' not in pg.url]

        new_pages = self.wait_for_condition(wait_for_new_page)
        editor_page = new_pages[0]
        return editor_page

    def get_page_url(self, page):
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        return specified_page.url
    
    def go_back(self, page):
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        return specified_page.go_back()

    def get_server_info(self):
        return self._browser_data[SERVER_INFO]['url']

    def navigate_to(self, page, partial_url):
        if page == TREE_PAGE:
            specified_page = self._tree_page
        elif page == EDITOR_PAGE:
            specified_page = self._editor_page
        else:
            raise Exception('Error, provide a valid page to evaluate from!')

        specified_page.goto(self._browser_data[SERVER_INFO]['url'] + partial_url)

    # TODO: Refactor/consider removing this (legacy cruft)
    @classmethod
    def new_notebook_frontend(cls, browser_data, kernel_name='kernel-python3', existing_file_name=None):
        instance = cls(browser_data, existing_file_name)

        return instance


def validate_dualmode_state(notebook, mode, index):
    """Validate the entire dual mode state of the notebook.
    Checks if the specified cell is selected, and the mode and keyboard mode are the same.
    Depending on the mode given:
        Command: Checks that no cells are in focus or in edit mode.
        Edit:    Checks that only the specified cell is in focus and in edit mode.
    """
    def is_only_cell_edit(index):
        JS = '() => { return Jupyter.notebook.get_cells().map(function(c) {return c.mode;}) }'
        cells_mode = notebook.evaluate(JS, EDITOR_PAGE)
        # None of the cells are in edit mode
        if index is None:
            for mode in cells_mode:
                if mode == 'edit':
                    return False
            return True
        # Only the index cell is on edit mode
        for i, mode in enumerate(cells_mode):
            if i == index:
                if mode != 'edit':
                    return False
            else:
                if mode == 'edit':
                    return False
        return True

    def is_focused_on(index):
        JS = "() => { return $('#notebook .CodeMirror-focused textarea').length; }"
        focused_cells = notebook.evaluate(JS, EDITOR_PAGE)
        if index is None:
            return focused_cells == 0

        if focused_cells != 1:  # only one cell is focused
            return False

        JS = "() => { return $('#notebook .CodeMirror-focused textarea')[0]; }"
        focused_cell = notebook.evaluate(JS, EDITOR_PAGE)
        JS = f"() => {{ return IPython.notebook.get_cell({index}).code_mirror.getInputField() }}"
        cell = notebook.evaluate(JS, EDITOR_PAGE)
        return focused_cell == cell

    # general test
    JS = "() => { return IPython.keyboard_manager.mode; }"
    keyboard_mode = notebook.evaluate(JS, EDITOR_PAGE)
    JS = "() => { return IPython.notebook.mode; }"
    notebook_mode = notebook.evaluate(JS, EDITOR_PAGE)

    # validate selected cell
    JS = "() => { return Jupyter.notebook.get_selected_cells_indices(); }"
    cell_index = notebook.evaluate(JS, EDITOR_PAGE)
    assert cell_index == [index]  # only the index cell is selected

    if mode != 'command' and mode != 'edit':
        raise Exception('An unknown mode was send: mode = "%s"'%mode)  # An unknown mode is send

    # validate mode
    assert mode == keyboard_mode  # keyboard mode is correct

    if mode == 'command':
        assert is_focused_on(None)  # no focused cells

        assert is_only_cell_edit(None)  # no cells in edit mode

    elif mode == 'edit':
        assert is_focused_on(index)  # The specified cell is focused

        assert is_only_cell_edit(index)  # The specified cell is the only one in edit mode

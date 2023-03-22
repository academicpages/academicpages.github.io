"""Test navigation to directory links"""


import os
from .utils import  TREE_PAGE
from jupyter_server.utils import url_path_join
pjoin = os.path.join


def url_in_tree(nb, url=None):
    if url is None:
        url = nb.get_page_url(page=TREE_PAGE)

    tree_url = url_path_join(nb.get_server_info(), 'tree')
    return True if tree_url in url else False


def get_list_items(nb):
    """
    Gets list items from a directory listing page
    """

    notebook_list = nb.locate('#notebook_list', page=TREE_PAGE)
    link_items = notebook_list.locate_all('.item_link')

    return [{
        'link': a.get_attribute('href'),
        'label': a.get_inner_text(),
        'element': a,
    } for a in link_items if a.get_inner_text() != '..']


def test_navigation(notebook_frontend):
    
    link_elements = get_list_items(notebook_frontend)

    def check_links(nb, list_of_link_elements):
        if len(list_of_link_elements) < 1:
            return False

        for item in list_of_link_elements:
            item["element"].click()

            assert url_in_tree(notebook_frontend) == True
            assert item["link"] in nb.get_page_url(page=TREE_PAGE)

            new_links = get_list_items(nb)
            if len(new_links) > 0:
                check_links(nb, new_links)

            nb.go_back(page=TREE_PAGE)

        return 

    check_links(notebook_frontend, link_elements)

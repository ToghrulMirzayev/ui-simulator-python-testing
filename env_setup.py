"""
Module that represents environment setup
"""

import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()


class PathSetup:
    """
    Class that contains Path as constants
    """
    ROOT_PATH: Final = os.path.dirname(os.path.realpath(__file__))


class URLSetup:
    """
    Class that contains URL as constants
    """
    INDEX_PAGE_URL: Final = "https://toghrulmirzayev.github.io/ui-simulator/"
    HOVER_AND_SELECT_PAGE_URL: Final = f"{INDEX_PAGE_URL}hover_and_select.html"
    INPUT_AND_CLICK_PAGE_URL: Final = f"{INDEX_PAGE_URL}input-and-click.html"
    CHECK_AND_VALIDATE_PAGE_URL: Final = f"{INDEX_PAGE_URL}check_and_validate.html"
    DRAG_AND_DROP_PAGE_URL: Final = f"{INDEX_PAGE_URL}drag-and-drop.html"
    CHECKBOX_AND_SCROLL_PAGE_URL: Final = f"{INDEX_PAGE_URL}checkbox-and-scroll.html"
    SORTING_PAGE_URL: Final = f"{INDEX_PAGE_URL}sorting.html"


class EnvVariables:
    """
    Class that contains secrets as constants
    """
    USERNAME: Final = os.environ.get("TEST_USERNAME")
    PASSWORD: Final = os.environ.get("TEST_PASSWORD")

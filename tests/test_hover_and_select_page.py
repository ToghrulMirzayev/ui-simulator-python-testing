from pytest import mark
from env_setup import URLSetup

pages = ([URLSetup.DRAG_AND_DROP_PAGE_URL, 1],
         [URLSetup.INPUT_AND_CLICK_PAGE_URL, 2],
         [URLSetup.CHECKBOX_AND_SCROLL_PAGE_URL, 3],
         [URLSetup.CHECK_AND_VALIDATE_PAGE_URL, 4],
         [URLSetup.SORTING_PAGE_URL, 5])


@mark.parametrize("page_url, page_index", pages,
                  ids=["drag and drop page", "input and click page", "checkbox and scroll page",
                       "check and validate page", "sorting page"])
@mark.smoke
def test_navigate_page(hover_and_select_page, page_url, page_index):
    hover_and_select_page.navigate(page=page_url,
                                   page_index=page_index)

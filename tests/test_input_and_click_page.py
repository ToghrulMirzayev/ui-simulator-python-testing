from pytest import mark


@mark.smoke
def test_add_item(input_and_click_page):
    input_and_click_page.add_new_item("item", "1")

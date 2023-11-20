def test_replace_cards(drag_and_drop_page):
    drag_and_drop_page.replace_cards()
    drag_and_drop_page.is_done_word_appeared()

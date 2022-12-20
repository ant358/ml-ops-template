from src.get_text_data import get_wiki, get_random_wiki_page


def test_get_wiki():
    assert len(get_wiki()) > 0


def test_get_random_wiki_page():
    assert len(get_random_wiki_page()) > 0

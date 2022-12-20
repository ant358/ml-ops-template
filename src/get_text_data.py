# %%
import wikipedia


def get_wiki(name="Monty Python", sentences=10) -> str:
    """A wikipedia fetcher function

    Args:
        name (str, optional): The name of the page to fetch.
            Defaults to "Python".
        sentences (int, optional): The number of sentences to fetch.
            Defaults to 10
            can be no greater than 10.

    Returns:
        str: The fetched wikipedia page
    """
    try:
        wiki = wikipedia.summary(name, sentences=sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        wiki = wikipedia.summary(e.options[0], sentences=sentences)
        print(e)
    except wikipedia.exceptions.PageError as e:
        wiki = wikipedia.summary(name, sentences=sentences)
        print(e)
    return wiki


def get_random_wiki_page(pages=1) -> list[str]:
    """Fetch a random wikipedia page

    Args:
        pages (int, optional): The number of pages titles. Defaults to 1.

        Returns:
            list[str]: The titles of the random pages
    """
    return wikipedia.random(pages=pages)


if __name__ == "__main__":
    print(get_wiki())

# %%

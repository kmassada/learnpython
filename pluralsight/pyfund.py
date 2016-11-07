"""Retrieve and print words form a URL

Usage:
    python3 <url|'http://sixty-north.com/c/t.txt'>

"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """ fetch a list of words from a link 
    Args:
        url: the url of the the UTF-8 text doc.
    Returns:
        A list of words and their count in file
    """
    with urlopen(url) as story:
        story_words = []
        results = dict()
        for line in story:
            lines = line.decode('utf-8').split()
            for word in lines:
                # word_count[word] = 1 if word not in word_count else word_count[word] + 1
                results[word] = results.setdefault(word, 0) + 1
                story_words.append(word)
    return results


def main(url):
    """Print each word from a text document from a URL

    Args: 
        url: The url of the UTF-8 text doc.
    """
    words = fetch_words(url)
    print_items(words)


def print_items(items):
    """Print items one per line

    Args:
        an iterable line of items
    """
    for item in items:
        print(item)


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://sixty-north.com/c/t.txt'
    main(url)

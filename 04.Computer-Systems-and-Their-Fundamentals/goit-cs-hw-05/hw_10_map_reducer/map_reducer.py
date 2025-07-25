"""Module for searching the most frequent words by URL"""

import string
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import requests
import matplotlib.pyplot as plt


SKIPWORDS = {
    "i",
    "a",
    "the",
    "this",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
    "and",
    "he",
    "it",
    "that",
    "his",
    "you",
    "they",
    "him",
    "which",
    "could",
    "she",
    "her",
    "one",
    "would",
    "an",
    "said",
    "what",
    "even",
    "them",
    "their",
    "its",
    "we",
    "your",
    "never",
    "two",
    "back",
}


def get_text(url: str) -> str:
    """Function of receiving text information by URL"""
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Failed to retrieve text from URL: {e}")
        return ""


def remove_punctuation(text: str) -> str:
    """Function of removing punctuation from a text"""
    return text.translate(str.maketrans("", "", string.punctuation))


def map_function(word: str) -> tuple:
    """Function that assigns the value 1 to a key word"""
    word = word.lower()
    if word in SKIPWORDS:
        return None, None
    return word, 1


def shuffle_function(mapped_values: list[tuple,]) -> defaultdict[str, list]:
    """Function for grouping words and their frequency"""
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        if key:
            shuffled[key].append(value)
    return shuffled.items()


def reduce_function(key_values: tuple[str, list[int,]]) -> tuple[str, int]:
    """Function of calculating the frequency of occurrence of a word in the text"""
    key, values = key_values
    return key, sum(values)


def map_reduce(text: str) -> dict:
    """Aggregation function for map reduction operations with text to find words with their frequencies"""
    text = remove_punctuation(text)
    words = text.split()

    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))

    shuffled_values = shuffle_function(mapped_values)

    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)


def visualize_top_words(word_freq: dict, top_n: int = 10) -> None:
    """The function of visualizing a chart with the most frequently occurring words"""
    top_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:top_n]
    words, frequencies = zip(*top_words)

    plt.figure(figsize=(10, 5))
    plt.bar(words, frequencies, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top Words by Frequency")
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    URL = "https://gutenberg.net.au/ebooks01/0100021.txt"
    source_text = get_text(URL)
    if source_text:
        result = map_reduce(source_text)
        visualize_top_words(result)

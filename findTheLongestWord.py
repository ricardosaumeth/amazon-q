from functools import reduce
from typing import Tuple


def find_the_longest_word(source: str) -> Tuple[int, str]:
    if not isinstance(source, str):
        raise ValueError("input must be a valid string")
    if not source:
        return [0, ""]

    words = source.split(" ")
    longest = max(words, key=len)
    return [len(longest), longest]
    # result = reduce(
    #     lambda longest, word: longest if len(longest) >= len(word) else word,
    #     words,
    # )
    # return [len(result), result]


print(find_the_longest_word("Ricardo Manuel Santana Saumeth"))  # [6, Ricardo]
print(find_the_longest_word("The quick brown fox"))  # Returns (5, "quick")
print(find_the_longest_word("Hello world"))  # Returns (5, "Hello")
print(find_the_longest_word(""))  # Returns (0, "")

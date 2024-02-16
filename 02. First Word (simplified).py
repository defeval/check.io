# You are given a string and you have to find its first word.
#
# The input string consists of only English letters and spaces.
# There aren’t any spaces at the beginning and the end of the string.
# example
#
# Input: A string (str).
#
# Output: A string (str).


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.split(' ')[0]


def best_first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")


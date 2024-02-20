# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# It can be the only one.
#
# example
#
# Input: Non-empty list of string (str).
#
# Output: A string (str).


# Best from statistics import mode as most_frequent


def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(set(data), key=lambda x: data.count(x))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")

# In a given text you need to sum the numbers while excluding any digits that form part of a word.
#
# The text consists of numbers, spaces and letters from the English alphabet.
#
# example
#
# Input: A string (str).
#
# Output: An integer (int).
import re


def sum_numbers(text: str) -> int:
    return sum(map(int, re.findall(r"\b\d+\b", text)))


def best_sum_numbers(text: str) -> int:
    return sum(int(word) for word in text.split() if word.isdigit())


print("Example:")
print(sum_numbers("hi 5"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

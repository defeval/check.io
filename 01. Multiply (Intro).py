# This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how
# to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".
#
# This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the
# multiplication of these 2 numbers.
#
# Input: Two arguments. Both are of type int.
#
# Output: Int.

# BEST

from operator import mul as mult_two


def mult_two(a, b):
    # your code here
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")



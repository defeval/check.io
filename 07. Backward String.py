# You should return a given string in reverse order.
#
# Input: A string (str).
#
# Output: A string (str).


def backward_string(val: str) -> str:
    # your code here
    return val[::-1]


# Best
best_backward_string = lambda val: val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")

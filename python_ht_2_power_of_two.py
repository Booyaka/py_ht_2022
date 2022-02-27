"""Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


def true_or_false(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False  # рукурсивное решение я подсмотрел, если честно. Поэтому сдаю то, что написал сам.
    # if num == 1:
    #     return True
    # if num % 2 == 0 or num == 0:
    #     return False


number = int(input('Pls, enters a number: '))
print(true_or_false(number))
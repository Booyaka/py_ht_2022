"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""


def true_or_false(array: list) -> bool:
    return len(array) != len(set(array))


print(true_or_false([1, 2, 3]))
print(true_or_false([1, 2, 1]))
print(true_or_false([3, 3, 3]))
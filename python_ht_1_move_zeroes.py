"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.

Note that you must do this in-place without making a copy of the array.
"""


def get_list(arr: list) -> list:
    for i in range(len(my_array)):
        if my_array[i] == 0:
            my_array.append(my_array.pop(i))

    return print(my_array)


my_array = [0, 1, 0, 3, 12, 0, 133]
get_list(my_array)
"""2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import sample

my_list = sample(range(0, 50), 20)

print(my_list)
print(min(my_list))
print(max(my_list))

my_max, my_min = my_list.index(max(my_list)), my_list.index(min(my_list))
my_list[my_max], my_list[my_min] = my_list[my_min], my_list[my_max]
print(my_list)
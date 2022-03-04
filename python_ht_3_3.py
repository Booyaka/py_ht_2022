"""3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import sample

my_list = sample(range(-20, 20), 20)
print(my_list)

print(f'Максимальный отрицательный элемент: {min(my_list)}, под индексом: {my_list.index(min(my_list))}')
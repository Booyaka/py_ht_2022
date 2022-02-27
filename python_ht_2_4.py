"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def count_n(n: int):
    idx = 0
    range_number = 1
    my_sum = 0
    while idx < n:
        my_sum += range_number
        range_number /= -2
        idx += 1

    print(f'Сумма {my_sum}')


number = int(input('Pls, enter amount of element: '))
count_n(number)
"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def nat_count(num: int):
    my_list = list(map(int, str(num)))
    even_count = 0
    odd_count = 0
    for i in my_list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
    return print(f'Четных: {even_count}, нечетных: {odd_count}')


nat_count(34560)
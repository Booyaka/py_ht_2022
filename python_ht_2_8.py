"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def count_of_number(num: int, dig: int):
    my_list = list(map(int, str(num)))
    # print(my_list)
    idx = 0
    for i in my_list:
        if i == dig:
            idx += 1

    print(f'{dig} occurs {idx} times in {num}')


number = int(input('Pls, enters a sequence a number: '))
digit = int(input('Pls, enter a digit: '))
count_of_number(number, digit)
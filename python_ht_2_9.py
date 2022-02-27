"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_of_num(num_1: int, num_2: int, num_3: int):
    sum_1 = sum(list(map(int, str(num_1))))
    sum_2 = sum(list(map(int, str(num_2))))
    sum_3 = sum(list(map(int, str(num_3))))

    if sum_1 > sum_2:
        if sum_1 > sum_3:
            print(num_1, sum_1)
        else:
            print(num_3, sum_3)
    else:
        if sum_2 > sum_3:
            print(num_2, sum_2)
        else:
            print(num_3, sum_3)


sum_of_num(111, 666, 13)
"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, то надо вывести
число 6843.
"""


def reverse_num(num: int):
    reverse = 0
    while num != 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    return reverse


number = 3486
print(reverse_num(number))
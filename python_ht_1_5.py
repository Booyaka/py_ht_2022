# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


def get_let(let: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = alphabet.index(let[0]) + 1
    b = alphabet.index(let[1]) + 1
    if a < b:
        c = b - a
    elif a > b:
        c = a - b
    else:
        c = a - b + 1

    return print(f'Position of letters: {a, b}, numbers between letters: {c - 1}')


letters = input('Pls, enter two letters in english: ').lower()
get_let(letters)
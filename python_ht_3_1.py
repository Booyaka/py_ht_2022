"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9.
"""

result = {}
for i in range(2, 10):
    result[i] = []
    for _ in range(2, 100):
        if _ % i == 0:
            result[i].append(_)
    print(f'Для числа {i} - {len(result[i])} кратных чисел.')
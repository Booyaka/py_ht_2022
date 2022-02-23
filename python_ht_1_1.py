import unittest


# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def get_sum(num: int) -> int:
    res = list(map(int, str(num)))
    return sum(res)


num = int(input('Pls, enter a number: '))
print(get_sum(num))


class TestGetMax(unittest.TestCase):
    def test_one(self):
        self.assertEqual(6, get_sum(123))
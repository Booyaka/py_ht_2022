# Определить, является ли год, который ввел пользователем, високосным или не високосным.

my_year = int(input('Pls, enter the year of your birth: '))
if ((my_year % 4 == 0 and my_year % 100 != 0) or (my_year % 400 == 0)):
  print("It's a leap year")
else:
  print("It's a normal year")
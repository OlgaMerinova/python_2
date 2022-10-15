# Реализуйте алгоритм перемешивания списка.

import random

N = int(input("Введите размер списка: "))
numbers = list(range(1, N+1))
print(numbers)

random.shuffle(numbers)
print(numbers)



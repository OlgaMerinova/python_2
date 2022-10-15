# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Введите размер списка: "))
numbers = list(range(-N, N+1))
print(numbers)

# data = open('file.txt', 'w')
file = []
with open("file.txt") as f:
    for line in f:
        file.append([int(x) for x in line.split()])
print(file)


# comp = 
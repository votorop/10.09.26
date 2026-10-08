#!usr/bin/python3

a = int(input("Введите число: "))
c = []
b = a
for i in range(2, 9):
    while (b%i == 0):
        b = b // i
        c.append(i)
c.append(b)
print("Простые множители числа ", a, ": ", c, ".")


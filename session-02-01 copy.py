# Факториал числа N!
n = int(input("Введите число: "))
sum = 1
while n >= 1:
    sum = sum * n
    n -=1
print(sum)

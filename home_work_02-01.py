import random
n = int(input("Введите число монет: "))
side = 0
eagle = 0
gerb = 0
for i in range (n):
    side = random.randint(0, 1)
    print (side, end = " ")
    if side > 0:
        eagle += 1
    else: 
        gerb += 1

if gerb > eagle:
    print(eagle)
else:
    print()
    print(gerb)


"""На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть."""

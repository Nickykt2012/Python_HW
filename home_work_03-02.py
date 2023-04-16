import random
n = int(input('Введите число: '))
list_1 = []
closest_num = -1
for i in range(10):
     list_1.append(random.randint(1,15))
     min_d = max(list_1) - n
     
for i in set(list_1):
     if abs(i - n) < min_d:
         min_d = abs(i - n)
         closest_num = i
print(f'максимально близкое число {closest_num}')
print(f'список {list_1}')
print(f'список без повторных чисел {set(list_1)}')



"""ТТребуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X"""
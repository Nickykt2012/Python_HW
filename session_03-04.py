import random
n = int(input("Введите количество элементов: "))
nums = []
count = 0
nums.append(random.randint(-10,10))
for i in range(1,n):
    nums.append(random.randint(-10,10))
    if nums[i]>nums[i-1]:
        count += 1

print(nums)
print(f"Количество чисел : {count}")

"""Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего 
элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)"""


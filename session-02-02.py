# Фибоначи
A = int(input("Ведите искомый номер числа фибоначчи "))

if A == 0:
    print("0")

elif A == 1:
    print("1\n или")

if (A < 0):
    print("-1")
else:
    fib1 = 0
    fib2 = 1
    fib3 = 1
    FibIndx = 2

    while (fib2 < A):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        FibIndx += 1

    result = FibIndx

if fib2 == A:
    print(result)

else:
    print("-1")
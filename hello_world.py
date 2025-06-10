import random

def factorial(n):
    if n==0:
        return 1
    else:
        res = 1
        for i in range (1, n+1):
            res *= i
        return res
    

for _ in range(3):
    num = random.randint(1,10)
    print(f"Factorial of {num}: {factorial(num)}")
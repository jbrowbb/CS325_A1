import random

def cache(func):
    cache_dic = {}
    def wrapper (*args):
        if args in cache_dic:
            return cache_dic[args]
        result = func(*args)
        cache_dic[args] = result
        return result
    return wrapper

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)



def main():
    for _ in range(10):
        random_number = random.randint(1,100)
        print(f"Random number generated: {random_number}")
        print(f"Fibonacci of {random_number}: {fib(random_number)}")
        print ("-" * 30)


if __name__ == "__main__":
    main()
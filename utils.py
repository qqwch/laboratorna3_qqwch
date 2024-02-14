def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

def is_prime(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(n * 0.5) + 1):
            if n % i == 0:
                return "Not prime"
        else:
            return "Is prime"

def GCD(a, b):
    while a * b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return b + a


def fib_rec(n):
    if n <= 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

def is_even(number):
    return number % 2 == 0

def is_odd(n):
	return n % 2 != 0

def func(n):
	return n

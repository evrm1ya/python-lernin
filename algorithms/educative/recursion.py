def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    print(factorial_iterative(5))
    print(factorial(0))
    print(factorial(5))
    print(factorial(200))

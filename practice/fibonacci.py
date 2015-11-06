def fibonacci_solution1(n):
    a, b = 1, 1
    if n < 3:
        return 1
    for i in range(n-2):
        c = a+b
        a = b
        b = c
    return b


def fibonacci_solution2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_solution2(n-1)+fibonacci_solution2(n-2)


def fibonacci_solution3(n):
    fib = [1, 1]
    for i in range(n-2):
        fib.append(fib[-1]+fib[-2])
    return fib[n-1]

print(fibonacci_solution3(5))

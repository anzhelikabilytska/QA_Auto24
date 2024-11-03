def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number

for num in even_numbers(10):
    print(f'Even digital: {num}')

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(20):
    print(f'Fibonacci digital: {num}')
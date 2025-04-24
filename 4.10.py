def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

N = int(input("Enter the number of Fibonacci terms to generate: "))

if N < 1:
    print("Please enter a positive integer.")
else:
    print(f"First {N} numbers of the Fibonacci series: {fibonacci(N)}")

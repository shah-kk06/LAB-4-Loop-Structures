import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def nPr(n, r):
    return math.factorial(n) // math.factorial(n - r)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if n < 0 or r < 0 or r > n:
    print("Invalid input! Ensure n >= r and both are non-negative.")
else:
    print(f"nCr ({n}C{r}): {nCr(n, r)}")
    print(f"nPr ({n}P{r}): {nPr(n, r)}")

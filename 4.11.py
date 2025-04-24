import math

def sine_taylor(x, terms=10):
    sin_x = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_x += term
    return sin_x

degrees = float(input("Enter the angle in degrees: "))

radians = degrees * (math.pi / 180)

sin_value = sine_taylor(radians)

print(f"sin({degrees}°) ≈ {sin_value}")

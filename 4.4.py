def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = str(n ** 2)
    return square.endswith(str(n))

num = int(input("Enter a number: "))

print(f"Is {num} Prime? {'Yes' if is_prime(num) else 'No'}")
print(f"Is {num} Perfect? {'Yes' if is_perfect(num) else 'No'}")
print(f"Is {num} Armstrong? {'Yes' if is_armstrong(num) else 'No'}")
print(f"Is {num} Palindrome? {'Yes' if is_palindrome(num) else 'No'}")
print(f"Is {num} Automorphic? {'Yes' if is_automorphic(num) else 'No'}")

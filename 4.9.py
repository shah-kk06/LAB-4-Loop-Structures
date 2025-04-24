N = int(input("Enter a number (N): "))

print(f"The first {N} natural numbers in reverse order:")
for i in range(N, 0, -1):
    print(i, end=" ")

user_string = input("Enter a string: ")

alphabet_count = 0
digit_count = 0

for char in user_string:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':  
        alphabet_count += 1
    elif '0' <= char <= '9':  
        digit_count += 1

print(f"Number of alphabets: {alphabet_count}")
print(f"Number of digits: {digit_count}")

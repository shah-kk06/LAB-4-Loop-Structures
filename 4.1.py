uppercase_letters = ""
for i in range(65, 91):  # ASCII values for A-Z
    uppercase_letters += chr(i) + " "

lowercase_letters = ""
for i in range(97, 123):  # ASCII values for a-z
    lowercase_letters += chr(i) + " "

print("Uppercase Alphabets:", uppercase_letters)
print("Lowercase Alphabets:", lowercase_letters)

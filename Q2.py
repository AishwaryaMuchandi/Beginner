# 2. Write a program that accepts a string as input from the user and
# calculates the number of digits and letters.
# Input: Hello123
# Output: Alphabets: 5 & Number : 3


user_input = input("Enter a string: ")


num_letters = 0
num_digits = 0


for char in user_input:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1


print(f"Alphabets: {num_letters} & Numbers: {num_digits}")

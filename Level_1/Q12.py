# Write a Python program to reverse a number using a while
# loop.
# Sample Input: num = 12345
# Sample Output: revnum = 54321

def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number //= 10
    return reversed_num

num = int(input("Enter a number: "))

revnum = reverse_number(num)

print(f"Reversed Number: {revnum}")

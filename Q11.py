# Write a Python program to calculate the sum of digits of a given
# number until the sum becomes a single-digit number.
# Sample Input: num = 987
# Sample Output: Sum_of_digits = 24,
# Again compute the sum of digits so that it can be reduced to
# on single digit.
# Final Output: 6

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

num = int(input("Enter a number: "))

while num >= 10:
    num = sum_of_digits(num)

print("Intermediate Sum of digits:", num)

final_sum = sum_of_digits(num)
print("Final Output:", final_sum)

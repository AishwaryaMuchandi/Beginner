# Write a Python program to calculate the LCM (Least Common
# Multiple) of two numbers.
# number1 = 12, number2 = 18
# LCM of 12 and 18 are: 36

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = lcm(number1, number2)

print(f"LCM of {number1} and {number2} is: {result}")

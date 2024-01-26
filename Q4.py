# Write a Python program to find the sum of all odd numbers
# between two given numbers.
# Start = 1, stop = 10
# Sum of odd numbers: 25


start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))

sum_of_odd_numbers = 0

for number in range(start, stop + 1):

    if number % 2 != 0:
        sum_of_odd_numbers += number

print(f"Sum of odd numbers between {start} and {stop}: {sum_of_odd_numbers}")



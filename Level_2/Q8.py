# Write a Python function that counts the number of vowels in a
# given string.
# Sample Input: string = "Hello, World!"
# Sample Output: Number of vowels: 3

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input_string = "Hello, World!"

num_vowels = count_vowels(input_string)
print("Number of vowels:", num_vowels)

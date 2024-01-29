# Write a Python program to find if a given string starts with a
# given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H"
# Sample Output: True

input_string = "Hello, World!"
given_char = "H"

starts_with_char = lambda s, c: s.startswith(c)

result = starts_with_char(input_string, given_char)
print("Sample Output:", result)

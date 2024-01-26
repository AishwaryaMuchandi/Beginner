
# 10. Write a Python program to reverse the order of words in a given
# sentence.
# Input_sentence = “Hello, World! Welcome to Python
# programming.”
# Output after reverse = “programming. Python to Welcome
# World! Hello,”


input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
reversed_sentence = ' '.join(reversed(words))
print("Output after reverse:", reversed_sentence)

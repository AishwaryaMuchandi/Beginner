# Read the doc.txt file using Python File handling concept and
# return only the even length string from the file. Consider the
# content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string which is of even length.
# Make sure you return the content in The same link as it is present.

with open("doc.txt", "r") as file:
    lines = file.readlines()

    even_length_strings = [word.strip() for line in lines for word in line.split() if len(word.strip()) % 2 == 0]

print("Even length strings from doc.txt:")
for string in even_length_strings:
    print(string)


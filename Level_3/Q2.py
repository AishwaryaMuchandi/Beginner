# Write a program to count the lines in a file “demo.txt”

with open("demo.txt", "r") as file:
    line_count = 0

    for line in file:
        line_count += 1

print("Total number of lines in demo.txt:", line_count)

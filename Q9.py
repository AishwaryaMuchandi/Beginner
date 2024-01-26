# 9. Write a Python program to count the frequency of each element
# in a list.
# Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
# Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

input_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]

frequency_count = {}

for element in input_list:
    frequency_count[element] = frequency_count.get(element, 0) + 1

print("Frequency count:", frequency_count)

# 1. Write a Python program to find the common elements between
# two lists.
# Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
# Sample output: [4, 5]


l1 = [int(x) for x in input("Enter elements of the first list separated by space: ").split()]
l2 = [int(x) for x in input("Enter elements of the second list separated by space: ").split()]

common_elements = list(set(l1) & set(l2))
print("Common elements:", common_elements)

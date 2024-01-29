# Create a function that takes a list and returns a new list with
# unique elements of the first list.
# Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
# Sample Output: list2 = [1, 2, 3, 4, 5]

def unique_elements(input_list):
    unique_set = set()
    
    for element in input_list:
        unique_set.add(element)
    
    unique_list = list(unique_set)
    
    unique_list.sort()
    
    return unique_list

list1 = [1, 2, 2, 3, 4, 4, 5, 5]

list2 = unique_elements(list1)
print("Sample Output:", list2)

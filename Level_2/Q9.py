# Write a Python program that executes an operation on a list and
# handles an IndexError exception if the index is out of range.

def perform_operation_on_list(my_list, index, operation):
    try:
        result = operation(my_list[index])
        return result
    except IndexError:
        print("Index is out of range.")

my_list = [1, 2, 3, 4, 5]

index = 10
operation = lambda x: x

result = perform_operation_on_list(my_list, index, operation)
if result is not None:
    print("Result:", result)

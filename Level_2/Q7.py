# Write a Python function that finds the median of a list of
# numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.0

def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    if n % 2 == 0:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median = sorted_list[n // 2]
    return median

number_list = [7, 2, 5, 1, 9, 3]

median = find_median(number_list)
print("Median:", median)

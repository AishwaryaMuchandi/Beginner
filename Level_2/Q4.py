# Given an array of size N. The task is to rotate array by D elements
# towards right
# Sample Input: arr = [1, 2, 3, 4, 5], D = 2
# Sample Output: arr after rotation = [4, 5, 1, 2, 3]

def rotate_array(arr, D):
    N = len(arr)
    rotated_arr = arr[N - D:] + arr[:N - D]
    
    return rotated_arr
arr = [1, 2, 3, 4, 5]
D = 2

rotated_arr = rotate_array(arr, D)
print("Sample Output: arr after rotation =", rotated_arr)

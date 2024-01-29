# Given an array of N integers and an integer K, find the number of
# pairs of elements in the array whose sum is equal to K.
# Sample Input: arr = [1, 2, 3, 4, 5], k = 6
# Sample Output: Pair count: 2

def pair_count(arr, k):
    freq_map = {}
    pair_count = 0
    
    for num in arr:
        complement = k - num
        if complement in freq_map:
            pair_count += freq_map[complement]
        
        freq_map[num] = freq_map.get(num, 0) + 1
    
    return pair_count

arr = [1, 2, 3, 4, 5]
k = 6

print("Pair count:", pair_count(arr, k))

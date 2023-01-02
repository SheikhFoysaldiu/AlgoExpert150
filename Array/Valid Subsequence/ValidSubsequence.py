# Subsequcence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

# Write a function that takes in two non-empty arrays of integers and determines whether the second array is a subsequence of the first one.

def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Test Cases:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
# Output: True

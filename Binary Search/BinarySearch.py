def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left+right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)


# Test
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(array, target))


# Output
# 3

# Time Complexity
# O(log(n)) time | O(log(n)) space
# O(log(n)) time because we are dividing the array in half each time
# O(log(n)) space because we are using recursion
# If we were not using recursion, we would have O(1) space


# -------------------Other Solutions-------------------#
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1

# time complexity
# O(log(n)) time | O(1) space

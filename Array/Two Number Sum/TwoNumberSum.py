def TwoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Test Case:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(TwoNumberSum(array, targetSum))


# Updated Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def TwoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# Test Case:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(TwoNumberSum(array, targetSum))


# Updated Solution
# Time Complexity: O(nlog(n))
# Space Complexity: O(1)
def TwoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


# test case
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(TwoNumberSum(array, targetSum))

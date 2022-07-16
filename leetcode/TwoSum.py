# Given an array of integers, return the indices of the two numbers that add up to a given target
# Approach
# --------
# 1. Are there any constraints? 
# All numbers are positive and have no duplicates. There may not always be a solution so return None is there is no solution. There can only be one pair that add up to the solution.
#
# 2. Write Test Cases
# It can be found at the bottom of the code where we call twoSum.

# Define a function that takes in two arguments: a list of numbers and a target value. Return the indices of the two numbers that add up to that value if any.

# brute force solution using Two-Pointer method
# TC: O(n^2) | SC: O(n)
def twoSum(nums, target):
    # go through the array and check to see if there are two numbers that add up to target. if there is a pair, return its indices, otherwise return None.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            complement = target - nums[i]
            if nums[j] == complement and i != j:
                return [i, j]

print(twoSum([1, 2, 4, 5, 9, 11], 7))
print(twoSum([1, 2, 4, 5, 9, 11], 8))
print(twoSum([], 7))
print(twoSum([1], 7))
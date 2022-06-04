# This pattern involves creating a window which can either be an array or number from position to another
# Depending on a certain condition, the window either increases or closes (and a new window is created)
# Very useful for keeping track of a subset of data in an array/string etc.

# TC: O(N) | SC: O(1)
def maxSubarraySum(array, num):
    # sets default values to 0
    maxSum , windowSum = 0 , 0
    window_start = 0

    # edge case where the array's length is smaller than the number of elements we're supposed to sum up
    if  len(array) < num:
        return None
    
    # loops through the range of the array to find maximum sum of n elements each time
    for window_end in range(len(array)):
        # current window sum is calculated by adding value to the window sum
        windowSum += array[window_end]

        # once we hit the end of the initital window range, start to calculate the new sum of the new window by subtracting from the left and adding from the right
        if window_end >= num-1:
            # check to see if maxSum or windowSum is greater then sets it to the maxSum
            maxSum = max(maxSum, windowSum)
            # subtracts left hand value from windowSum
            windowSum -= array[window_start]
            # moves starting window by one index to the right
            window_start += 1
    return maxSum
    


print(maxSubarraySum([2,6,9,2,1,8,5,6,3],3))

# You are given an array of positive integers where each integer represents the height of a vertical line on a chart. Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. Return the area of water it would hold.
# Approach
# --------
# 1. Are there any constraints? 
# Lines dont account into the area and container must be formed using the length of two walls in the array.
#
# 2. Write Test Cases
# See bottom of code for test cases.

# Define a function that takes in an array and returns the maxArea. Utilize the area equation.
# Area = length * width
# Area = min(a,b) * (bi - ai)

# optimized solution using Two-Shifting pointers
# TC: O(n) | SC: O(1)
def calculateMaxArea(array):
    # p1 starts 0 and p2 starts at the end of the array. set maxArea intiailly to zero.
    p1, p2, maxArea = 0, len(array) - 1, 0

    # while p1 is less than p2, calculate the current area and check to see if its larger than the maxArea. maxArea equals whichever is bigger
    while p1 < p2:
        current = min(array[p1], array[p2]) * (p2 - p1)
        maxArea = max(maxArea, current)

        # the # at p1 is less than or equal to the # at p2, move p1 to the right. else move p2 to the left
        if array[p1] <= array[p2]:
            p1 += 1
        else:
            p2 -= 1
    # returns maxArea
    return maxArea


# brute force solution using Two-Pointer method.
# TC: O(n^2) | SC: O(1)
# def calculateMaxArea(array):
#     maxArea = 0 # sets initial max size to 0
#     for i, a in enumerate(array):
#         for j, b in enumerate(array):
#             current = min(a, b) * (j - i) # calculates current maxArea
#             # if current area is bigger than maxArea, set it to the new maxArea
#             if(current > maxArea):
#                 maxArea = current

#             # you can also use
#             # maxArea = max(current, maxArea)
            
#     # returns maxArea
#     return maxArea

array1 = [7,1,2,3,9]
print(calculateMaxArea(array1))
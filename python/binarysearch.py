# Divide and Conquer
# This pattern involves dividing a data set into smaller chunks and then repeating a process with a subset of data
# This pattern can tremendously decrease time complexity

import math # imports math module to use floor() and ceil()

def binarysearch(array, target):
    min, max = 0 , len(array) - 1

    while min <= max:
        middle = math.floor((min + max) / 2)
        currElement = array[middle]

        if array[middle] < target:
            min = middle + 1
        elif array[middle] > target:
            max = middle - 1
        else:
            return middle
    return -1

print(binarysearch([1,2,3,5,6,8,9,12,15,16,29], 16)) # return 9 because 16 is at index 9
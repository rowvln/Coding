# Quick Sort
# Like merge sort, it exploits the fact that arrays of 0 or 1 element are always sorted
# Works by selecting one element (called the “pivot”) and finding the index where the pivot should end up in the sorted array
# Call the pivot helper on the array
# When the helper returns to you the updated pivot index, recursively call the pivot helper on the subarray to the left of that index and the subarray to the right of that index
# Your base case occurs when you consider a subarray with less than 2 elements

# Generates list of random numbers
import random
def generateRandom(): 
    mylist = []

    for i in range(0,1000):
        x = random.randint(1,1000)
        mylist.append(x)

    return mylist

def pivot(array, start, end):
    # choose the rightmost element as pivot
    pivot = array[end]

    # a pointer for greater element
    swapIndex = start - 1

    # go through all the elements and compare each element with the pivot
    for i in range(start, end):
        if pivot >= array[i]:
            swapIndex += 1

            # swaps elements at swapIndex with element at i
            (array[swapIndex], array[i]) = (array[i], array[swapIndex])

            # The swap above is similar to this traditional way of making a swap method but easier in Python
            # temp = array[i]
            # array[i] = array[swapIndex]
            # array[swapIndex] = temp

    # swaps the pivot element with the greater element specified by i
    (array[swapIndex + 1], array[end]) = (array[end], array[swapIndex + 1])
    return swapIndex + 1

# TC: O(nlogn) BEST, O(n^2) WORSE || SC: O(1)
def quickSort(array, left, right):
    if left < right:
        pivotIndex = pivot(array, left, right)

        # sorts left side
        quickSort(array, left, pivotIndex - 1)
        # sorts right side
        quickSort(array, pivotIndex + 1, right)
    return array

list1 = generateRandom()
print(quickSort(list1, 0, len(list1) - 1))
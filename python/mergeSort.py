# Merge Sort
# It’s a combination of two things - merging and sorting! A lot faster than Bubble, Selection, and Insertion
# Exploits the fact that arrays of 0 or 1 element are always sorted
# Works by decomposing an array into a smaller arrays of 0 or 1 elements, then building up a newly sorted array
# In order to implement merge sort, it’s useful to first implement a function responsible for merging two sorted arrays
# Given two arrays which are sorted, this helper function should create a new array which is also sorted, and consists of all of the elements in the two input arrays
# This function should run in O(m+n) time and O(n+m) space and should not modify the parameters passed to it
# Create an empty array, take a look at the smallest values in each input array

# While there are still values we haven’t looked at, do the following:

# If the value in the first array is smaller than the value in the second array, push the value in the first array into our results and move on to the next value in the first array
# If the value in the first array is larger than the value in the second array, push the value in the second array into our results and move on to the next value in the second array
# Once we exhaust one array, push in all the remaining values from the other array


# Generates list of random numbers
import random
def generateRandom(): 
    mylist = []

    for i in range(0,10):
        x = random.randint(1,1000)
        mylist.append(x)

    return mylist

# TC: O(nlogn) || SC: O(n)
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # recursively calls mergeSort on each half of the array
        mergeSort(left)
        mergeSort(right)

        # i and j iterates through the two halves, k is the iterator for the main list
        i, j, k = 0, 0, 0 # or i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            # moves k to next slot in the main list
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array

list1 = generateRandom()
print(mergeSort(list1))

# Notes for learning how to merge two lists together to understand how Merge Sort works
#
# Merges two sorted lists together - ROWVIN'S ATTEMPT
# def merge(array1, array2):
#     sortedArray = []
#     j = 0
#     for i in range(len(array1)):
#         if array1[i] < array2[j]:
#             sortedArray.append(array1[i])
#             i += 1
#         else:
#             sortedArray.append(array2[j])
#             j += 1
#     while i < len(array1):
#         sortedArray.append(array1[i])        
#     while j < len(array2):
#         sortedArray.append(array2[j])
#         j += 1    
#     return sortedArray

# Merges two sorted lists together - PROPER WAY
# def merge(array1, array2):
#     sortedArray = []
#     i = 0
#     j = 0
#     while i < len(array1) and j < len(array2):
#         if array1[i] < array2[j]:
#             sortedArray.append(array1[i])
#             i += 1
#         else:
#             sortedArray.append(array2[j])
#             j += 1
#         while i < len(array1):
#             sortedArray.append(array1[i])
#             i += 1        
#         while j < len(array2):
#             sortedArray.append(array2[j])
#             j += 1
#         return sortedArray
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
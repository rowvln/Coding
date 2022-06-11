# Selection Sort
# Similar to bubble sort, but instead of putting the large values into the sorted place, you’re putting the small values into the sorted place
# Store the first element as the smallest value you’ve seen so far
# Compare this item to the next item in the array until you find a smaller number
# If a smaller number  is found, designate that smaller number to be the new “minimum” and continue until the end of the array.
# If the “minimum” is not the value ( index) you initially began with, swap the values

# Generates list of random numbers
# import random
# def generateRandom(): 
#     mylist = []

#     for i in range(0,10000):
#         x = random.randint(1,1000)
#         mylist.append(x)

#     return mylist

# TC: O(n^2) || SC: O(1)
def selectionSort(array):
    arrLength = len(array)
    for i in range(arrLength):
        min = i
        for j in range(i+1, arrLength):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    return array

#list1 = generateRandom()
print(selectionSort(list1))

# Builds up the sort by gradually creating a larger half which is always sorted
# Start by picking the second element in the array
# Now compare the second element with the one before it and swap if necessary
# Continue to the next element and if it is in the incorrect order, iterate through the sorted portion ( i.e the left side) to place the element in the correct place
# Repeat until the array is sorted

# Generates list of random numbers
import random
def generateRandom(): 
    mylist = []

    for i in range(0,20):
        x = random.randint(1,1000)
        mylist.append(x)

    return mylist

# TC: O(n^2) || SC: O(1)
def insertionSort(array):
    for i in range(1, len(array)):
        currVal = array[i] 
        j = i - 1
        while j >= 0 and currVal < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = currVal
    return array

list1 = generateRandom()
print(insertionSort(list1))
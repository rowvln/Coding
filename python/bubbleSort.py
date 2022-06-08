# Bubble Sort
# A sorting algorithm where the largest values bubble up to the top
# Start looping with a variable called i from the end of the array towards the beginning
# Start an inner loop with a variable called j from the beginning until i - 1
# If arr[j] is greater than arr[j+1], swap those two values

# Generates list of random numbers
# import random
# def generateRandom(): 
#     mylist = []

#     for i in range(0,10000):
#         x = random.randint(1,1000)
#         mylist.append(x)

#     return mylist

# TC: O(n^2) | SC: O(1) - Naive Solution
# Not optimized solution
# def bubbleSort(array):
#     for i in range(len(array) - 1):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#     return array

# print(bubbleSort([37,45,29,8]))

# TC: O(n^2) | SC: O(1)
def bubbleSort(array):
    noswaps = None
    n  = len(array)

    for i in range(n - 1):
        noSwaps = True
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                noSwaps = False
        if noSwaps:
            break
    return array

#list1 = generateRandom()
print(bubbleSort(list1))
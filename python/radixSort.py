# Radix Sort - TC: || SC:
# Raxdix sort is a special sorting algorithm that ONLY works on lists of numbers
# It never makes comparisons between elements!
# It exploits the fact that information about the size of a number is encoded in the number of digits
# More digits means a bigger number!
# Sorts by putting numbers in different buckets starting from the rightmost number and moving to the leftmost side. 
# After each sort, put them together then move index to to the right

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# TC: O(n+k) || O(n+k)
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

print(radixSort([23,345,5367,12,2345,9852]))     

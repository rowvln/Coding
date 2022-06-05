# Linear search
# This function accepts an array and a value. Loop through the array and check if the current array element is equal to the value.
# If it is, return the index at which the element is found. If the value is never found, return -1

# TC: O(n) | SC: O(1)
def linearSearch(array, value):
    for i,num in enumerate(array):
        if num == value:
            return i
    return -1

print(linearSearch([9,8,7,6,5,4,3,2,1,0],10))
print(linearSearch([9,8,7,6,5,4,3,2,1,0],4))
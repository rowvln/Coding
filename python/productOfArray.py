def productOfArray(array):
    if(len(array) == 0):
        return 1
    return array[0] * productOfArray(array.slice(1))

print(productOfArray([1,2,3,10]))
# Using Multiple Pointers Method
# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle, based on a certain condition
# Very effcient for solving problems with minimal space complexity as well
def countUniqueValues(array):
    array_set = set(array)
    unique_total = len(array_set)
    print(unique_total)
    return unique_total

countUniqueValues([1,2,2,5,7,7,99])
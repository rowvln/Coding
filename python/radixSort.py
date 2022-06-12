# Radix Sort - TC: || SC:
# Raxdix sort is a special sorting algorithm that ONLY works on lists of numbers
# It never makes comparisons between elements!
# It exploits the fact that information about the size of a number is encoded in the number of digits
# More digits means a bigger number!
# Sorts by putting numbers in different buckets starting from the rightmost number and moving to the leftmost side. 
# After each sort, put them together then move index to to the right
import math

def getDigit(num, i):
    return math.floor(abs(num) / pow(10, i) % 10)

def digitCount(num):
    if num == 0: 
        return 1
    return math.floor(math.log10(abs(num))) + 1

def mostDigits(nums):
    maxDigits = 0
    for i in range(len(nums)):
        maxDigits = max(maxDigits, digitCount(nums[i]))
    return maxDigits

def radixSort(nums):
    maxDigitCount = mostDigits(nums)
    for k in range(maxDigitCount):
        digitBuckets = []
        for i in range(len(nums) - 1):
            digitBuckets[getDigit(nums[i], k)].push("hello")
    print(range(len(nums) - 1))
print(radixSort([23,345,5367,12,2345,9852]))     

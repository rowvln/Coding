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

print(getDigit(10,2)) # returns 0
print(digitCount(7234)) # returns 4

def radixSort(nums):
    maxDigitCount = mostDigits(nums)
    while k < maxDigitCount:
        digitBuckets = 

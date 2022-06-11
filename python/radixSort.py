<<<<<<< HEAD
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
=======
# Generates list of random numbers
# import random
# def generateRandom(): 
#     mylist = []

#     for i in range(0,10000):
#         x = random.randint(1,1000)
#         mylist.append(x)

#     return mylist

# TC: O(nlogn) || SC: O(1)
def radixSort(array):
    return array
>>>>>>> 06cb013a5e121e3665a25d7fde3f89822ad4cc77

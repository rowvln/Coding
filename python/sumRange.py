# sumRange function using Recursion
# A function tht calls itself and invokes the same function with a different input until you reach your base case
def sumRange(num):
    if num == 1:
        return 1
    return num + sumRange(num-1)

print(sumRange(3))
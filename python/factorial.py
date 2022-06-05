# sumRange function using Recursion
# A function tht calls itself and invokes the same function with a different input until you reach your base case
# def factorial(num):
#     total = 1
#     while num > 0:
#         total *= num
#         num -= 1
#     return total

def factorial(num):
    if(num == 1):
        return 1
    return num * factorial(num - 1)

print(factorial(5))

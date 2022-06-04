# Using Frequency Counter method
# This pattern uses objects or sets to collect values/frequencies of values
# This can often avoid the need for nested loops or O(n^2) operations with arrays/strings

def validAnagram(first, second):
    if(len(first) != len(second)):
        return False;
    
    lookup = {}

    for l in first:
        letter = l
        if lookup[letter] not in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1
    
    for l in second:
        if not lookup[letter]:
            return False
        else:
            lookup[letter] -= 1
    return True

validAnagram('anagram', 'nagaram')
# 
def iCantEven(lst):
    for number in lst:
        if number % 2 == 0:
            return False
    return True

def iCantEven2(lst):
    foundEven = False
    for number in lst:
        if number % 2 == 0:
            foundEven = True
    return not foundEven

# If you're really really cool
def iCantEven3(lst):
    return all(item % 2 == 1 for item in lst)

# Testing Code
lst = []
lst2 = [0]
lst3 = [1]
lst4 = [0,2]
lst5 = [0,1,2,3]
lst6 = [1,9,7,5,3]

assert iCantEven(lst) and iCantEven2(lst) and iCantEven3(lst)
assert not iCantEven(lst2) and not iCantEven2(lst2) and not iCantEven3(lst2)
assert iCantEven(lst3) and iCantEven2(lst3) and iCantEven3(lst3)
assert not iCantEven(lst4) and not iCantEven2(lst4) and not iCantEven3(lst4)
assert not iCantEven(lst5) and not iCantEven2(lst5) and not iCantEven3(lst5)
assert iCantEven(lst6) and iCantEven2(lst6) and iCantEven3(lst6)
print("Tests Passed")
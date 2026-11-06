def sumList(*args):
    return sum(args)


l1 = list(range(1, 6, 3))  # start, stop, step
print(l1)

l = list(range(*l1))  # [1,4] -> [1, 2, 3]
print(l)

print(sumList(1, 2, 3, 4, 5))


# Documentation
def nothing():
    """Nothing"""
    pass


print(nothing.__doc__)

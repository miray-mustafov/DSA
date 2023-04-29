def findMinOperation(s1, s2, i1, i2):
    if i1 == len(s1):
        return len(s2) - i2
    if i2 == len(s2):
        return len(s1) - i1
    if s1[i1] == s2[i2]:
        return findMinOperation(s1, s2, i1 + 1, i2 + 1)

    deleteOp = 1 + findMinOperation(s1, s2, i1, i2 + 1)
    insertOp = 1 + findMinOperation(s1, s2, i1 + 1, i2)
    replaceOp = 1 + findMinOperation(s1, s2, i1 + 1, i2 + 1)
    return min(deleteOp, insertOp, replaceOp)


print(findMinOperation("table", "tbrlt", 0, 0))
print(findMinOperation("catch", "carch", 0, 0))

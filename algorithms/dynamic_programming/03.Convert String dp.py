def findMinOperation(s1, s2, i1, i2, memo):
    if i1 == len(s1):
        return len(s2) - i2
    if i2 == len(s2):
        return len(s1) - i1
    if s1[i1] == s2[i2]:
        return findMinOperation(s1, s2, i1 + 1, i2 + 1, memo)
    if (i1, i2) not in memo:
        deleteOp = 1 + findMinOperation(s1, s2, i1, i2 + 1, memo)
        insertOp = 1 + findMinOperation(s1, s2, i1 + 1, i2, memo)
        replaceOp = 1 + findMinOperation(s1, s2, i1 + 1, i2 + 1, memo)
        memo[(i1, i2)] = min(deleteOp, insertOp, replaceOp)
    return memo[(i1, i2)]


def bottom_up_tabulation(s1, s2, i1, i2):
    pass


memo = {}
print(findMinOperation("table", "tbrlt", 0, 0, memo.copy()))
print(findMinOperation("catch", "carch", 0, 0, memo.copy()))

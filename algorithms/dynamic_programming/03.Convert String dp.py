def findMinOperation(s1, s2, index1, index2, memo):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1, memo)
    if (index1, index2) not in memo:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2 + 1, memo)
        insertOp = 1 + findMinOperation(s1, s2, index1 + 1, index2, memo)
        replaceOp = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1, memo)
        memo[(index1, index2)] = min(deleteOp, insertOp, replaceOp)
    return memo[(index1, index2)]


memo = {}
print(findMinOperation("table", "tbrlt", 0, 0, memo.copy()))
print(findMinOperation("catch", "carch", 0, 0, memo.copy()))

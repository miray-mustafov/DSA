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


def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1) + 1):
        dictKey = str(i1) + '0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2) + 1):
        dictKey = '0' + str(i2)
        tempDict[dictKey] = i2

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dictKey = str(i1) + str(i2)
                dictKey1 = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1) + str(i2)
                dictKeyD = str(i1 - 1) + str(i2)
                dictKeyI = str(i1) + str(i2 - 1)
                dictKeyR = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI], tempDict[dictKeyR]))
    dictKey = str(len(s1)) + str(len(s2))
    return tempDict[dictKey]


print(findMinOperationBU("table", "tbrlt", {}))

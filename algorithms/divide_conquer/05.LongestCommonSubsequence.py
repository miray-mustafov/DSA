def findLCS(s1, s2, i1, i2):
    if i1 >= len(s1) or i2 >= len(s2):
        return 0
    if s1[i1] == s2[i2]:
        return 1 + findLCS(s1, s2, i1 + 1, i2 + 1)
    op1 = findLCS(s1, s2, i1, i2 + 1)
    op2 = findLCS(s1, s2, i1 + 1, i2)
    return max(op1, op2)


print(findLCS("elephant", "eretpsat", 0, 0))  # 5

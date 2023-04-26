def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex + 1, endIndex - 1)

    op1 = findLPS(s, startIndex, endIndex - 1)
    op2 = findLPS(s, startIndex + 1, endIndex)
    return max(op1, op2)


def findLPS_str(s, startIndex, endIndex):
    if startIndex > endIndex:
        return ''
    elif startIndex == endIndex:
        return s[startIndex]
    elif s[startIndex] == s[endIndex]:
        return s[startIndex] + findLPS_str(s, startIndex + 1, endIndex - 1) + s[endIndex]

    op1 = findLPS_str(s, startIndex, endIndex - 1)
    op2 = findLPS_str(s, startIndex + 1, endIndex)
    return op1 if len(op1) >= len(op2) else op2


print(findLPS("ELRMENMET", 0, 8))  # 5
print(findLPS_str("ELRMENMET", 0, 8))  # EMEME

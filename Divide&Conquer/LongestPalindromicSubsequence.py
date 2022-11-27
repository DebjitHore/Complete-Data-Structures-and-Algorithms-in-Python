
def LPS(s, startIndex, endIndex):
    if startIndex>endIndex:
        return 0
    elif startIndex==endIndex:
        return 1
    elif s[startIndex]==s[endIndex]:
        return 2+LPS(s, startIndex+1, endIndex-1)
    else:
        op1= LPS(s, startIndex+1, endIndex )
        op2=LPS(s, startIndex, endIndex-1)
        return max(op1, op2)



print(LPS('ELRMENMET', 0, 8))
    


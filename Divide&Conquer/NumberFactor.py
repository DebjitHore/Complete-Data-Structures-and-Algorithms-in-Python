#Given N, number of ways to express N as a sum of 1,3,4
#To find the subproblems just find the f(N-i)+i combinations where i=1,3,4


def numberFactor(N):
    if N in (0,1,2):
        return 1
    elif N==3:
        return 2
    else:
        subP1= numberFactor(N-1)
        subP2= numberFactor(N-3)
        subP3= numberFactor(N-4)
        return (subP1+subP2+subP3)


print(numberFactor(5))
    





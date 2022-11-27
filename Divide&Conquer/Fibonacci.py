def fibonacciSeries(N):
    if N<1:
        return "Not Possible"
    elif N==1:
        return 0
    elif N==2:
        return 1
    else:
        return (fibonacciSeries(N-1)+fibonacciSeries(N-2))




print(fibonacciSeries(10))
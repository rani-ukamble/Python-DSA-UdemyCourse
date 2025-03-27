def fatcorial(n):
    if n==1:
        return 1
    return n*fatcorial(n-1)

print(fatcorial(4))
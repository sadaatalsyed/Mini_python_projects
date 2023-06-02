def factt(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factt(n-1)

print(factt(5))
def fibb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

print(fibb(int(input("Enter a number to find a fibbonaci: "))))
'''
f4=f3+f2=(f2+f1)+(f1+f0)=((f1+f0)+f1)+(f1+f0)=((1+0)+1)+(1+0)=3
'''
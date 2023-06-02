
def fibb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        list_a=[0,1]
        while(n>2):
            a, b = b, b+1
            list_a.append(a)
            n-=1
        # print(f"a:{a}")
        # print(f"b:{b}")
        return list_a
# print(fibb(int(input("Enter a number to find a fibbonaci series: "))))
n=int(input("Enter a number to find a fibbonaci series: "))
print(fibb(n))
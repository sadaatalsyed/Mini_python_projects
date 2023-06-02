num1=0
num2=1
total_num=100


def equi(num1,num2,total_num):
    count=0
    dis=(num2-num1)/total_num
    for i in range(1,total_num+1):
        count+=1
        num1+=dis
        print(f"{num1} \t",end="")
    print(dis)
# num1=int(input("Enter Lower num1: "))
# num2=int(input("Enter Lower num2: "))
# total_num=int(input("How much equidistance numbers you want: "))
equi(num1,num2,total_num)

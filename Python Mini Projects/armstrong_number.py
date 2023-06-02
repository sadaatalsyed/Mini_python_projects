def isArmstrong(n):
    nstr=str(n) #convert number into string
    nlist=list(nstr) #converts string to a list containing one digit as one item of list
    order=len(nlist) #total number of digits in the list i.e digits in the number
    sum=0
    for i in range(len(nlist)):
        num=(int(nlist[i])**order) #calculate each digit raised to the power of total number of digits
        # print(f"{int(nlist[i])}^{order}: {int(nlist[i])**order}")
        sum+=num
        
    return sum==n

def calculateBelowList(num):
    list_of_armstrong=[]
    for n in range (num):
        if isArmstrong(n):
            list_of_armstrong.append(n)
    print(f"List of Armstong numbers below {num} is :{list_of_armstrong}")
def calculateBetweenList(lo_num,up_num):
    list_of_armstrong=[]
    for n in range (lo_num,up_num):
        if isArmstrong(n):
            list_of_armstrong.append(n)
    print(f"List of Armstong numbers between {lo_num} and {up_num} is :{list_of_armstrong}")

try_again= "y"

while try_again.lower()=='y':
    try:
        choice=(input('''What do you want to do?\n1:\tFind if a number is an Armstrong or not?(Press 1)
                \n2:\tFind total numbers of Armstrong number below a number e.g below 1000 (Press 2)
                \n3:\tFind total numbers of Armstrong number between two numbers e.g bw 1000 and 3000 (Press 3)\n Input here :  '''))
        choice = int(choice)
        # if choice not in (1,2,3):
        #     print("Invalid Choice!,Choose out of given options")
        if choice==1:
            print("So you choose to check an Armstrong number")
            num=input("Enter a number to check if it is Armstrong or not: ")
            num=int(num)
            if isArmstrong(num):
                print("Number is an Armstrong number")
            else:
                print("Sorry, your number is not an Armstrong ")
        elif choice==2:
            print("So you choose to find list of Armstrong numbers below certain number")
            num=input("Enter a number to  Armstrong numbers lower than that: ")
            num=int(num)
            print(f"Calculating list of Armstrong numbers below {num}.......")
            calculateBelowList(num)
        elif choice==3:
            print("So you choose to find list of Armstrong numbers between two numbers.")
            lowerNumber=int(input("Enter lower number: "))
            upperNumber=int(input("Enter upper number: "))
            print(f"Calculating list of Armstrong numbers between {lowerNumber} and {upperNumber}.......")
            calculateBetweenList(lowerNumber,upperNumber)
            
    except ValueError:
        print("Input must be a digit.")
    
    try_again=input("Press y to try again or any other key to exit: ")
    
    




def findMissingNumber(listOfNumbers):
    maxOfList=listOfNumbers[-1]
    minOfList=listOfNumbers[0]
    missingNumbers=[]
    for i in range(minOfList,maxOfList):
        if i not in listOfNumbers:
            missingNumbers.append(i)
    # print(missingNumbers)
    return missingNumbers
n=0
list_n=[]
n=int(input("Enter numbers one at a time (or any negative number exit the programme ): "))
while n>=0:
    list_n.append(n)
    n=int(input("Enter numbers one at a time (or any negative number exit the programme ): "))
    list_n.sort()

print("your list of Numbers: ", list_n)


missingNums=findMissingNumber(list_n)
print(f"You missed following number between {list_n[0]} and {list_n[-1]} :  {missingNums}")
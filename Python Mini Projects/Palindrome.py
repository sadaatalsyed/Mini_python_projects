
def reverse1(num):
    reverse=0
    while num>0:  
        digit=num%10    #fetching last digit of the number with mod e.g 234 % 10 will give 4.
        reverse=reverse*10 + digit 
        num=num//10    # calculating remaining number e.g 234 // 10 gives 23
        # print("remaining number: ",num, "last fetched digit: ",digit)
        return reverse


num=int(input("Enter number to check if it is palindrome or not "))
temp=num
rev=reverse1(num)
print("Reverse of the number:", rev)
if temp ==rev :
    print(f"{temp}  is a Palindome ")
else:
    print(f"{temp} is not a Palindrome")


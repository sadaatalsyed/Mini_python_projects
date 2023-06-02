
def isPrime(n):
    for i in range(2,n//2+1):
        if n % i==0:
            # print(i)
            print(f"{n} is Not prime because it divisible by {i}")
            break
    else:
        print(f"{n} is a prime number")
isPrime(int(input("Enter a valid digit number: ")))
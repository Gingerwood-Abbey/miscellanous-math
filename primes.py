# Check whether a number is prime or not 

n = int(input("Enter a number: "))

for i in range(2,n):
    if n%i ==0:
       print(n," is not a prime ")
       break
    else:
        print(n," is a prime")

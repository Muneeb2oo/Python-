n=int(input("Enter Number "))
if(n)==1:
        print("this is prime number")
for i in range(2,n):
    if(n%i)==0:
        print("this is not prime number")
        break
    else:
        print("this is prime number")
        break

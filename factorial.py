n=int(input("Enter number to find its factorial"))

if n>0:
    fact=1
    for i in range(1,n+1):
        fact*=i

    print("factorial using for loop is: " ,fact)

    fact=1
    while(n>0):
        fact*=n
        n-=1

    print("factorial using while loop is: " ,fact)

elif n==0 or n==1:
    print("the factorial is:",n)

else:
    print("Factorial doesn't exist for negative number")

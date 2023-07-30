n=int(input("Enter no of element for dictionary: "))

d={}
if n>0:
    for i in range(1,n+1):
        d[i]=i*i

    print(d)

elif n<=0:
    print("Enter a valid input")



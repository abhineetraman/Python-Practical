t1=()
a=int(input("Enter element of tuple:"))
t1=t1+(a,)
n=int(input("Enter no of element for tuple:"))
for i in range(n-1):
    a=int(input("Enter element of tuple:"))
    t1=t1+(a,)
print(t1)

t2=()
a=int(input("Enter element of tuple:"))
t2=t2+(a,)
n=int(input("Enter no of element for tuple:"))
for i in range(n-1):
    a=int(input("Enter element of tuple:"))
    t2=t2+(a,)
print(t2)

t1,t2=t2,t1
print(t1,t2)
    

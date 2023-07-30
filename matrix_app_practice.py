n=int(input("Enter Size of 1st square matrix: "))
l1=[]
for i in range(n):
    z=[]
    for j in range(n):
        a=int(input("Enter element of 1st matrix: "))
        z.append(a)
    l1.append(z)

n=int(input("Enter Size of 2nd square matrix: "))
l2=[]
for i in range(n):
    z=[]
    for j in range(n):
        a=int(input("Enter element of 1st matrix: "))
        z.append(a)
    l2.append(z)

print("The 1st Matrix is:" )
for i in range(n):
        for j in range(n):
            print(l1[i][j],end=' ')
        print()
print("The 2nd Matrix is:" ,)
for i in range(n):
        for j in range(n):
            print(l2[i][j],end=' ')
        print()
z=int(input("Enter the number for operation :\n1.Addition \n2.Subtraction \n3.Transpose of A \n4.Transpose of B \n"))
if z==1:
    c=[[0*n]*n]*n
    print("The matrix after sum is:")
    for i in range(n):
        for j in range(n):
            c[i][j]=l1[i][j]+l2[i][j]
            print(c[i][j],end=' ')
        print()

if z==2:
    c=[[0*n]*n]*n
    print("The matrix after subtract is:")
    for i in range(n):
        for j in range(n):
            c[i][j]=l1[i][j]-l2[i][j]
            print(c[i][j],end=' ')
        print()

if z==3:
    for i in range(n):
        for j in range(i):
            l1[i][j],l1[j][i]=l1[j][i],l1[i][j]

    print("The matrix after transpose is:")
    for i in range(n):
        for j in range(n):
            print(l1[i][j],end=' ')
        print()

if z==4:
    for i in range(n):
        for j in range(i):
            l2[i][j],l2[j][i]=l2[j][i],l2[i][j]

    print("The matrix after transpose is:")
    for i in range(n):
        for j in range(n):
            print(l2[i][j],end=' ')
        print()

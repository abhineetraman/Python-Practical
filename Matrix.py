A=[]
size=int(input("Enter size for square Matrix"))
for i in range(size):
    row=[]
    for j in range(size):
        row.append(int(input("Enter the element")))
    A.append(row)

for i in range(size):
    for j in range(size):
        print(A[i][j],end=" ")
    print()



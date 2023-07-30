n=int(input("Enter no of block for pyramid:"))
print('star square of size',n,)
for i in range(1,n*2,2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))
for i in range(n*2-3,0,-2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))

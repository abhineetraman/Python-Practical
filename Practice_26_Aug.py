n=int(input("Enter no of block for pyramid:"))

print('Triangle from right')
for i in range(n+1):
    print((' ' * (n-i)) + ( '*' * i))

print(' ')
print('Triangle pyramid')
for i in range(1,n*2,2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))

print(' ')
print('Triangle pyramid upright')
for i in range(n*2-1,0,-2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))

print(' ')
print('star square')
for i in range(1,n*2,2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))
for i in range(n*2-3,0,-2):
    print((' ' * (((n*2)-i)//2)) + ( '*' * i) + (' ' * (((n*2)-i)//2)))



l=[1,2,3,4,5,6,7]
l1=[]
for i in range(len(l)):
    l1.append(l[i])
print("The list is:",l)
a=l.reverse()
print("Reverse list using in-built functions:",l)

print("Reverse list without using in-built functions:",l1[::-1])

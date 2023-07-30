import random
l=[]
for i in range(20):
    l.append(random.randint(1,100))

print(l)
print("The sum of list:",sum(l))

pro=1
for i in range(20):
    pro*=l[i]

print("the product of list:",pro)


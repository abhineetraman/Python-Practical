import random
l=[]
for i in range(100):
    l.append(random.randint(1,100))

print(l)
s=set(l)
d={}
for i in s:
    d[i]=0

for i in l:
    d[i]=d[i]+1

print(d)

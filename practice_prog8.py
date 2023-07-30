import random

l=[]
l1=[]
for i in range(20):
    l1.append(random.randint(1,100))

def check_list(l):
    if len(l)==0:
        return "the list is empty"
    else:
        return "the list is not empty"

print(check_list(l))
print(check_list(l1))

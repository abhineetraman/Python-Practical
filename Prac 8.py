import math
def fibo(n):
    l=[0,1]
    sum_term=0
    for i in range(n-2):
        sum_term=l[i]+l[i+1]
        l.append(sum_term)

    return l

def fact(n):
    l=fibo(n)
    fac=1
    for i in range(1,l[-1]+1):
        fac*=i
    return [l[-1],fac]

n=int(input("Position no to find it's fibonacci series no: "))
print(fact(n))

    

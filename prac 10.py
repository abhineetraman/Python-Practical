t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)

def tuple_func1(t1):
    l=list(t1)
    l1=[]
    for i in range(len(l)-1):
        if l[i]%2==0:
            l1.append(l[i])
    t1_even=tuple(l1)
    return t1_even

tuple_func2=lambda t1 : t1+t2

tuple_func3=lambda t1 : max(t1)

tuple_func4=lambda t1 : min(t1)

print("Even number in t1 is",tuple_func1(t1),"\nAfter concatination :",tuple_func2(t1),"\nMaximum number is :",tuple_func3(t1),"\nMinimum number is :",tuple_func4(t1))


    

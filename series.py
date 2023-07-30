n=int(input("Enter number to find its sum in the series"))
x=int(input('Enter the value of x: '))

def fact(n):
    fact=1
    while(n>0):
        fact*=n
        n-=1
    return fact

def series(n):
    sum_series=0
    for i in range(0,n):
        if i%2==0:
            sum_series+=x**(2*i)/fact(2*i)
        else:
            sum_series-=x**(2*i)/fact(2*i)
    return sum_series

print(series(n))


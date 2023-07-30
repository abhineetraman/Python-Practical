a=int(input('Enter the value'))
b=int(input('Enter the value'))
add=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div_int=lambda x,y:x//y
div_float=lambda x,y:x/y
remainder=lambda x,y:x%y
print('Select any option to perform : \n 1. add \n 2.Subtract \n 3.Multiply \n 4.Divide (int) \n 5.Divide(Float) \n 6. Remainder ')
z=int(input())
if z==1:
    print(add(a,b))
if z==2:
    print(sub(a,b))
if z==3:
    print(mul(a,b))
if z==4:
    print(div_int(a,b))
if z==5:
    print(div_float(a,b))
if z==6:
    print(remaider(a,b))

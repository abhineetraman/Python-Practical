add=lambda x,y: x+y
sub=lambda x,y: x-y
div=lambda x,y: x/y
remainder=lambda x,y: x%y
mul=lambda x,y: x*y
div_int=lambda x,y: x//y
power=lambda x,y: x**y

a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
c=input("Press '+' for add \n '-' for subtract \n '*' for multiply \n '**' for exponentiation \n '/' for float division \n '//' for int division \n '%' for remainder \n ")

if c=="+":
    print(add(a,b))
if c=="-":
    print(sub(a,b))
if c=="*":
    print(mul(a,b))
if c=="**":
    print(power(a,b))
if b>0:
    if c=="/":
        print(div(a,b))
    if c=="//":
        print(div_int(a,b))
    if c=="%":
        print(remainder(a,b))

else:
    print("Wrong expression")

    

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a>b and a>c:
    print(a, "is greatest")
if c>b and c>a:
    print(c, "is greatest")
if b>a and b>c:
    print(b, "is greatest")
if a<b and a<c:
    print(a, "is smallest")
if b<a and b<c:
    print(b, "is smallest")
if c<b and a>c:
    print(c, "is smallest")

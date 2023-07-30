perimeter = lambda x,y,z : x+y+z

def area(x,y,z):
    s=perimeter(x,y,z)//2
    return ((s*(s-x)*(s-y)*(s-z))**0.5)

def check_triangle(x,y,z):
    if x+y>z and x+z>y and y+z>x and x>0 and y>0 and z>0:
        return True
    else:
        return False

x=int(input("Enter 1st side: "))
y=int(input("Enter 2nd side: "))
z=int(input("Enter 3rd side: "))

if (check_triangle(x,y,z)):
    print("Area of triangle is ",area(x,y,z))
    print("Perimeter of triangle is: " , perimeter(x,y,z))
else:
    print("Invalid Triangle")

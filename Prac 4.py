side1=int(input('Enter 1st side'))
side2=int(input('Enter 2nd side'))
side3=int(input('Enter 3rd side'))

def area_triangle(x,y,z):
    if check_triangle(side1,side2,side3):
        semi_peri=(x+y+z)//2
        return (x+y+z,((semi_peri*(semi_peri-x)*(semi_peri-y)*(semi_peri-z))**0.5))
    else:
        return "Triangle is not correct"

def check_triangle(x,y,z):
    if x+y>z and x+z>y and y+z>x:
        return True
    else:
        return False

print("perimeter and area of triangle is:" ,area_triangle(side1,side2,side3))

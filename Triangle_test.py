a=int(input("Enter 1st side of triangle: "))
b=int(input("Enter 2nd side of triangle: "))
c=int(input("Enter 3rd side of triangle: "))
semi_peri=(a+b+c)//2
ar=((semi_peri*(semi_peri-a)*(semi_peri-b)*(semi_peri-c))**0.5)
if a==b==c:
    print("Triangle is equilateral")
    print("The Perimeter is: " + str(a+b+c))
elif a==b or b==c or c==a:
    semi_peri=(a+b+c)//2
    ar=((semi_peri*(semi_peri-a)*(semi_peri-b)*(semi_peri-c))**0.5)
    print("Triangle is isosceles","The area of triangle is :" + str(ar),sep='\n')
else:
    semi_peri=(a+b+c)//2
    ar=((semi_peri*(semi_peri-a)*(semi_peri-b)*(semi_peri-c))**0.5)
    print("Triangle is scalane","The area of triangle is :" + str(ar),sep='\n')
    

d={}
a=int(input("No. of salesman in showroom:"))
for j in range(1,a+1):
    
    sales_week=int(input("Enter week sales the salesman:"))
    sales_month=0
    sales_month+=sales_week
    for i in range(4):
        sales_week=int(input("Enter week sales of the salesman:"))
        sales_month+=sales_week
    print("sales of next salesman")
    d[j]=sales_month

def workshop(d):
    for i in range(1,a+1):
        com=0
        rem=" "
        if d[i]>50000:
            com=0.05*d[i]
        else:
            com=0
        
        if d[i]>=80000:
            rem="Excellent"
        elif d[i]>=60000:
            rem="Good"
        elif d[i]>=40000:
            rem="Average"
        elif d[i]<40000:
            rem="Work Hard"
        d[i]=(d[i],com,rem)

    return d.items() 

print(workshop(d))
    

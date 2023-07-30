def leap(yy1,yy2):
    l=[]
    for i in range(yy1,yy2):
        if i%4==0:
            if i%100!=0:
                l.append(i)
        if i%400==0:
            l.append(i)

    return l

   
def month(mm,yy):
    month ={1:'January', 2:'February', 3:'March',4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'} 
    day =(yy-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7

    nly =[31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    ly =[31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31] 

    s = 0
    if yy % 4 == 0: 

        for i in range(mm-1): 

            s+= ly[i] 

    else: 
        for i in range(mm-1): 
            s+= nly[i] 

    day += s % 7
    day = day % 7
    space ='' 
    space = space.rjust(2, ' ') 
    print(month[mm], yy) 
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa') 

    if mm == 9 or mm == 4 or mm == 6 or mm == 11:  
        for i in range(31 + day): 
            if i<= day: 
                print(space, end =' ') 

            else: 
                print("{:02d}".format(i-day), end =' ') 
                if (i + 1)% 7 == 0: 
                    print() 

    elif mm == 2: 
        if yy % 4 == 0: 
            p = 30
        else: 
            p = 29

        for i in range(p + day): 
            if i<= day: 
                print(space, end =' ') 
            else: 
                print("{:02d}".format(i-day), end =' ') 
                if (i + 1)% 7 == 0: 
                    print()  

    else: 
        for i in range(32 + day):       
            if i<= day: 
                print(space, end =' ') 
            else: 
                print("{:02d}".format(i-day), end =' ') 
                if (i + 1)% 7 == 0: 
                    print()

def day(dd,mm,yy):
    month ={1:'January', 2:'February', 3:'March',4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'} 
    day =(yy-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7

    nly =[31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    ly =[31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31] 

    s = 0
    if yy % 4 == 0: 

        for i in range(mm-1): 

            s+= ly[i] 

    else: 
        for i in range(mm-1): 
            s+= nly[i] 
    s+=dd
    day =(day + (s%7))%7
    week=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    return week[day]

while(True):
    a=int(input('Write the number for function input: \n1. Calender of the month \n2.Day of date given \n3.List of leap year \n4.Exit'))
    if a==1:
        yy=int(input('Enter the year'))
        mm=int(input("Enter the month no."))
        print(month(mm,yy))

    elif a==2:
        yy=int(input('Enter the year'))
        mm=int(input("Enter the month no."))
        dd=int(input('Enter a date'))
        print(day(dd,mm,yy))

    elif a==3:
        print(leap(2000,3000))
    elif a==4:
        exit(0)
    else:
        print('Wrong Input. Please try again')




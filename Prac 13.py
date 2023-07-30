d={}
while(True):
    name=input('Enter the name of student : ')
    if name=='':
        break
    else:
        marks={}
        Python_marks=int(input('Enter Python Marks :'))
        marks['Python']=Python_marks
        DS_marks=int(input('Enter DS Marks :'))
        marks['DS']=DS_marks
        OS_marks=int(input('Enter OS Marks :'))
        marks['OS']=OS_marks
        CN_marks=int(input('Enter CN Marks :'))
        marks['CN']=CN_marks
        d[name]=marks


print(d)

def highest_percent(d):
    maxi=0
    output=''
    for i in d:
        sum_per=0
        a=d[i]
        for j in a:
            sum_per+=a[j]
            per=(sum_per*100)/400
            if maxi<per:
                maxi=per
                output=i

    return output

print('Highest marks is secured by : ',highest_percent(d))


l=[]
a=input('Enter element of list seperated by commas')
for i in a.strip().split(','):
    l.append(i)

l1=[]
a=input('Enter element of list seperated by commas')
for i in a.strip().split(','):
    l1.append(i)

def check_numeric(l):
    for i in l:
        if i.isdigit():
            pass
        else:
            return False

    return True

def check_odd(l):
    if check_numeric(l):
        for i in range(len(l)):
            l[i]=int(l[i])

        count=0
        for i in l:
            if i%2!=0:
                count+=1

        return count

def max_string(l):
    if check_numeric(l) == False:
        return max(l)

def reverse_list(l):
    for i in range(len(l)//2):
        l[i],l[-i-1]=l[-i-1],l[i]

    return l

def search(l,k,begin=0,end=len(l)):
    l.sort()
    if begin==end:
        if l[begin]==k:
            return "Element found"
        else:
            return "Element not found"

    if end-begin==1:
        if l[begin]==k or l[end]==k:
            return "Element found"
        else:
            return "Element not found"

    if end-begin<0:
        return "Element not found"
    
    if end-begin>1:
        mid=(end+begin)//2
        if l[mid]==k:
            return "Element found"
        elif l[mid]>k:
            end=mid-1
        elif l[mid]<k:
            begin=mid+1
        return search(l,begin,end,k)

def remove(l,n):
    return l.remove(n)

def sort_desc(l):
    l.sort
    l.reverse
    return l

def common_member(l1,l2):
    s1,s2=set(l1),set(l2)
    return (list(s1 & s2))

print('The list is numeric or not :' ,check_numeric(l))
print(check_odd(l), max_string(l1))
print(reverse_list(l))
n=int(input('Enter a number to search: '))
print(search(l,n,0,len(l)))
n=int(input('Enter element to be deleted'))
print(remove(l,n))
print(sort_desc(l))
print(common_member(l,l1))

def linear_search(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return "Element found"

    return "Element not found"

def binary_search(l,begin,end,k):
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
        return binary_search(l,begin,end,k)

def insertion_sort(l,size):
    key=l[0]
    for i in range(size):
        for j in range(size):
            if key<l[j]:
                l[i],l[j]=l[j],l[i]

        if i<size-1:
            key=l[i+1]

    return l

def selection_sort(l,size):
    for i in range(size):
        for j in range(size):
            if j<size-1:
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]

    return l

def bubble_sort(l,size):
    for i in range(size):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

    return l

size=int(input("Enter size of array"))
l=[]
for i in range(size):
    a=int(input("enter the element"))
    l.append(a)

print("enter a way to find element \n1 for Linear \n2 for Binary")
ch=int(input())

k=int(input("Enter element to be searched"))
begin,end=0,size

if ch==1:
    print(linear_search(l,k))
elif ch==2:
    print('Binary search required sorted list')
    print('Choose an option to sort : \n1. Selection sort\n2. Bubble sort \n3. Insertion sort\n')
    c=int(input())
    if c==1:
        selection_sort(l,size)
    elif c==2:
        bubble_sort(l,size)
    elif c==3:
        insertion_sort(l,size)
    else:
        print('Wrong choice')

    print(binary_search(l,begin,end,k))

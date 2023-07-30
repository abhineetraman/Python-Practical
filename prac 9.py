n=input("Enter any integer greater than 10: ")
def digit_set(n):
    if n.isdigit() and n>"10":
        l=[]    
        for i in n:
            l.append(int(i))

        return set(l)

    else:
        return "Enter valid number"

print(digit_set(n))
        

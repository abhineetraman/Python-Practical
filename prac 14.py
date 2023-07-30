def frequency(s):
    s=s.lower()
    d={}
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        d[i]=0

    for i in s:
        if i in d:
            d[i]+=1
        else:
            pass

    return d

str1=input('Enter a sentence : ')
print(frequency(str1))

        

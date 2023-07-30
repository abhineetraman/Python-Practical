alpha='abcdefghijklmnopqrstuvwxyz'
s=input('String in lowercase')
t=''
k=int(input('Enter the number to be shifted'))
for i in range(len(s)):
    t=t+alpha[(((alpha.index(s[i]))+k)%26)]

print(t)

str_length=lambda str1:len(str1)

def maximum(str1,str2,str3):
    l=[str1,str2,str3]
    return max(l)

def replace_vowel(str1):
    output=''
    for i in str1:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            output+='#'
        else:
            output+=i

    return output

def word_count(str1):
    count=1
    for i in str1:
        if i==' ':
            count+=1

    return count

def palindrome(str1):
    if str1==str1[::-1]:
        return 'Palindrome'
    else:
        return 'Not a Palindrome'


s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")
s3=input("Enter 3rd string: ")

print('Select a choice: \n1.length of string \n2. Maximum of 3 string \n3. Replace vowel with # \n4.Count No. of words \n5.Check Palindrome \n6. Exit')
while(True):
    ch=int(input())
    
    if ch==1:
        print(str_length(s1))
    elif ch==2:
        print(maximum(s1,s2,s3))
    elif ch==3:
        print(replace_vowel(s1))
    elif ch==4:
        print(word_count(s1))
    elif ch==5:
        print(palindrome(s3))
    elif ch==6:
        exit(0)
    else:
        print("Enter right input")

          

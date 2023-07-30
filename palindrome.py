str1=input("Enter a word:")
str1=str1.lower()

output=" "
def palindrome(s):
    for i in range(len(s)):
        if s[i]==s[-i-1]:
            output= "Palindrome"
        else:
            output= "Not a Palindrome"
            break
    return output

print(palindrome(str1))

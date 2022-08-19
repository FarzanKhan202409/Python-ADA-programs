# Q. Write a function which return all the unique palindromes from a given string.

# A function to check whether a given object is palindrome or not:

def ispalindrome (x):
  s=str(x)
  for i in range(len (s)):
    if s[i]!= s[len(s)-1-j]:
       return False
   return True
# A function to collect all the palindrome set present in the passed sets

def PalindromeInstring(s)
result =[]  # An empty list to collect the result
for i in range (len(s)):
  temp=" " #Empty string
for j in range(i,len(s)):
   temp=temp + s[j] # appends the previous character to the next character for every iteration of j
           if ispalindrome(temp):
             if len(temp)>1: # A condition to check wheteher a string has len>1.
                             # since ispalindrome() returns True for single character.
                 result.append(temp)
    return result
if _name_=='_main_':
  s= abcdefghijk
print(PalindromeInstring(s))  

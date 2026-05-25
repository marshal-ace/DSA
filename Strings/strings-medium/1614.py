'''Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.'''

'''
Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.'''


#This is the optimal
s = "(1+(2*3)+((8)/4))+1"
def brute(s):
    max1=count=0
    for i in s:
        if i=="(":
            count+=1
        elif i==")":
            max1=max(count,max1)
            count-=1
    return max1
print(brute(s))
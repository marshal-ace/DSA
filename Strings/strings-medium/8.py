'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''

# s = "00000-42a1234"
# def brute(s):
#     sign=1
#     INT_MAX = 2**31 - 1
#     INT_MIN = -2**31
#     ans=""
#     s=s.lstrip("0")
#     print(s)
#     if s[0]=="-":
#         sign=-1
#         s=s[1:]
#     for i in range(0,len(s)):
#         if s[i]=="0" or s[i]=="1"or s[i]=="2" or s[i]=="3" or s[i]=="4" or  s[i]=="5" or s[i]=="6" or s[i]=="7" or s[i]=="8" or s[i]=="9":
#             ans+=s[i]
#         else:
#             if ans == "":
#                 return 0
#             ans=int(ans)
#             if sign==-1:
#                 ans=ans*-1
#             return ans
#     ans=int(ans)
#     if sign==-1:
#         ans=ans*-1
#     if ans>INT_MAX:
#         return INT_MAX
#     elif ans< INT_MIN:
#         return INT_MIN
#     else:
#         return ans
# print(brute(s))

s = "00000-42a1234"
def optimal(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    s=s.strip()

    if not s:
        return 0
    sign=1
    i=0

    if s[i]=="+" or s[i]=="-":
        if s[i]=="-":
            sign=-1
        i+=1
    ans=""
    while i<len(s) and s[i].isdigit():
        ans+=s[i]
        i+=1
    if not ans:
        return 0
    ans= int(ans)*sign
    if ans > INT_MAX:
        return INT_MAX
    if ans < INT_MIN:
        return INT_MIN
    return ans
print(optimal(s))
'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string. '''
'''
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.'''


n="35427"
# while n!=0:
#     r=n%10
#     if r%2==1:
#         print(str(n))
#         break
#     else:
#         n=n//10
# if n==0:
#     print("")
#Optimal
n="4206"
def brute(n):
    c=len(n)
    for ch in reversed(n):
        last_ch=int(ch)
        if last_ch%2==0:
            c-=1
            continue
        else:
            return n[:c]
print(brute(n))
            
            
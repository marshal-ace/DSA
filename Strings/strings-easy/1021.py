'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

'''
#I'm comparing the adjanceny paranthesis to do
# s="()()"
# ans=[s[0]]
# dust=[]   
# for i in range(1,len(s)):
#     if s[i]==ans[-1]:
#         dust.append(s[i])
#     else:
#         ans.append(s[i])
# print(ans)
# print(dust)


s="(()())(())"
def optimized(s):
    #Intialized a counter
    count=0
    ans=""
    for i in s:
        if i=="(":
            if count>0:
                ans+=i
            count+=1
        else:
            count-=1
            if count>0:
                ans+=i
    return ans
print(optimized(s))
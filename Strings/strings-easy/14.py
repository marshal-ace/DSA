'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"'''
'''A prefix is a collection of characters at the beginning of a string. For instance, “mi” is a prefix of “mint” and the longest common prefix between “mint”, “mini”, and “mineral” is “min”.'''

strs = ["a"]

def brute(strs):
    ans=""
    i=j=k=0
    if len(strs)==0:
        return ""
    while i<len(strs[0]) and j<len(strs[1]) and k<len(strs[2]):
        if strs[0][i]==strs[1][j] and strs[1][j]==strs[2][k]:
            ans+=strs[0][i]
            i+=1
            j+=1
            k+=1
        else:
            return ans
# print(brute(strs))

def optimized(strs):
    ans=""
    strs.sort()
    i=j=0
    if len(strs)==0 or len(strs[0])==0:
        return ""
    while i<len(strs[0]) and j<len(strs[-1]):
        if strs[0][i]==strs[-1][j]:
            ans+=strs[0][i]
            i+=1
            j+=1
        else:
            return ans
    return ans
print(optimized(strs))
# print(len(strs[0]))
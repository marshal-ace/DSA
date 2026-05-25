'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
'''anagram=An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.'''

s="anagram"
t="nagaram"

def brute(s,t):
    s=sorted(s)
    t=sorted(t)
    s="".join(s)
    t="".join(t)
    if s==t:
        return True
    else:
        return False
# print(brute(s,t))

'''NOt Optimal Time Complexity is O(n2)'''
def optimal(s,t):
    if len(s)!=len(t):
        return False
    s=list(s)
    map1={}
    for i in t:
        if i not in map1:
            map1[i]=s.count(i)
    t=list(t)
    for i in t:
        if i in map1:
            if t.count(i)!= map1.get(i):
                return False
        else:
            return False
    return True

def optimal(s,t):
    if len(s)!=len(t):
        return False
    hp={}
    for i in s:
        hp[i]=hp.get(i,0)+1
    for i in t:
        if i not in hp:
            return False
        hp[i]-=1
        if hp[i]<0:
            return False
    return True
    
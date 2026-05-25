'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

s="paper"
t="titll"
def brute(s,t):
    map1={}
    map2={}
    for i in range(len(s)):
        #As we need to check for Isomorhpic we need to check both the conditions thats why 2 maps are intialized
        #One map for checkin s->t
        #Second map for checking t->s
        
        if s[i] in map1:
            if map1.get(s[i])==t[i]:
                continue
            else:
                return False
        elif t[i] in map2:
            if map2.get(t[i])==s[i]:
                continue
            else:
                return False
        else:
            map1[s[i]]=t[i]
            map2[t[i]]=s[i]
    return True
print(brute(s,t))

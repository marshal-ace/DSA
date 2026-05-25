'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.'''





#Brute Time Complexity  O(n2) Space Complexity O(n)
s="Aabb"
def add(max,i):
    ans=""
    
    for ele in range((max)):
        ans+=i
    return ans
def brute(s):
    ans=""
    hp={}
    for i in s:
        hp[i]=hp.get(i,0)+1
    while hp:
        max=i=0
        for key,value in hp.items():
            if value > max:
                max=value
                i=key
        ans+=add(max,i)
        hp.pop(i)
    return ans
# print(brute(s))

#TC-O(n log n) SC (O(n))
def better(s):
    hp={}
    ans=""
    for i in s:
        hp[i]=hp.get(i,0)+1
    sorted_items=sorted(hp.items(),key=lambda x:x[1],reverse=True)
    for i in range(len(sorted_items)):
        for j in range(sorted_items[i][1]):
            ans+=sorted_items[i][0]
    return ans
print(better(s))

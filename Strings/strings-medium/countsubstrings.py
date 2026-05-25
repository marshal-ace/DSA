# You are given:
# A string s
# A positive integer k
# You must count how many substrings of s contain exactly k distinct characters.
# Return that count.

#brute
s="pqpqs"
i=0
k=2
final_count=0
while i<len(s):
    test=""
    j=i
    count=0
    while j<len(s):
        if s[j] not in test:
            test+=s[j]
            count+=1
        elif s[j] in test:
            test+=s[j]
        if count==k:
            final_count+=1
        elif count>k:
            break
        j+=1
    i+=1
print(final_count)

def atmost(s,k):
    left=right=0
    count=0
    freq={}
    while right<len(s):
        freq[s[right]]=freq.get(s[right],0)+1

        while len(freq)>k:
            freq[s[left]]-=1

            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
        count+=(right-left+1)
        right+=1
    return count
def substring(s,k):
    return atmost(s,k) - atmost(s,k-1)
print(substring(s,k))
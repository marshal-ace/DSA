s="aabcbaa"
#TC= O(n3) SC=O(n)
def brute(s):
    i=0
    dif=0
    beauti=0
    while i<len(s):
        test=""
        j=i
        freq={}
        while j<len(s):
            freq[s[j]]=freq.get(s[j],0)+1
            dif=(max(freq.values()))-(min(freq.values()))
            beauti+=dif
            j+=1
        i+=1
    return beauti
print(brute(s))

            

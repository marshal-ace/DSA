nums=[1,0,-1,0,-2,2]
target=0
def brute(nums):
    i=0
    res=[]
    while i<len(nums):
        j=i+1
        while j<len(nums):
            k=j+1
            while k<len(nums):
                m=k+1
                while m<len(nums):
                    total=0
                    total=nums[i]+nums[j]+nums[k]+nums[m]
                    if total==target:
                        temp=[nums[i],nums[j],nums[k],nums[m]]
                        temp.sort()
                        if temp not in res:
                            res.append(temp)
                    m+=1
                k+=1
            j+=1
        i+=1
    return res
# print(brute(nums))
#TIme Complexity O(n^3)*log(n=number of elements in the given array) -- Space Complexity O(1)
#Pick i
#  Pick j
#   seen = empty
#    Pick m
#     ❓ Do I already have a number that completes target?
#        YES → valid 4 numbers
#     ➕ Store nums[m] for future checks
# we don't the need the same element so we first check and then add into the hashmap
#we already add into the hashmap then waste of keeping becz already added the element we will check
def better(nums):
    res=[]
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            m=j+1
            hashmap={}
            while m<len(nums):
                temp=[]
                need=target-(nums[i]+nums[j]+nums[m])
                if need in hashmap:
                    temp=[nums[i],nums[j],nums[m],target-(nums[i]+nums[j]+nums[m])]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                hashmap[nums[m]]=m
                m+=1
            j+=1
        i+=1
    return res
# print(better(nums))

#In Optimal we are using 4 Pointers
# Same as the the 3 sum approach here we are fixing 2 variables i and j at the start and traversing k and l
#The loop runs till k>l and the array is sorted to avoid the duplication part
#Necessary conditions are written for each variable to avoid the duplicates
# Time Complexity-O(n3) -- Space O(1)
def optimal(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j!=i+1 and nums[j]==nums[j-1]: # "j!=i+1 this means if i+1=1 and j=1 we can consider like in the start but if j>i and still j value  "
                #J value is the same then we'll contiue like new loop
                continue
            k=j+1
            l=len(nums)-1
            while k<l:
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total==target:
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    res.append(temp)
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                elif total<target:
                    k+=1
                else:
                    l-=1
    return res
print(optimal(nums))

    
nums=[-1,0,1,2,-1,-4]
res=[]
#TL-O(n3)
def brute(nums):
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            k=j+1
            while k<len(nums):
                sum=0
                sum=nums[i]+nums[j]+nums[k]    
                if sum==0:
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)    
                k+=1
            j+=1
        i+=1
    return res
# print(brute(nums))
#TL-O(n2)
def better(nums):
    res=[]
    i=0
    while i<len(nums):
        # j=i+1
        hp={}
        # while j<len(nums):
        #     if nums[j] not in hp:
        #         hp[nums[j]]=j
        #         j+=1
        #Hash Map inside becz of the range
        #this allows no duplication of same elemenet
        k=i+1
        while k<len(nums):
            hp[nums[k]]=k
            temp=[]
            if 0-(nums[k]+nums[i]) in hp:
                temp=[nums[i],nums[k],(0-(nums[k]+nums[i]))]
                temp.sort()
                if temp not in res:
                    res.append(temp)
            k+=1
        i+=1
    return res
print(better(nums))
def optimal(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)):
        j=i+1
        k=len(nums)-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                res.append(temp)
                j+=1
                k-=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1
    return res
# print(optimal(nums))
            


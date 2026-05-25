nums=[1]
def brute(nums):
    res=[]
    hashmap={}
    for key,value in enumerate(nums):
        if value not in hashmap:
            hashmap[value]=1
        else:
            hashmap[value]+=1
    for key,value in hashmap.items():
        if value>len(nums)//3:
            res.append(key)
    return res
# print(brute(nums))
#Moore Algo main idea is that to remove the candidates which are useless for the contention . not to count the frequencies
#Mistakes: Didn't verify the moore checkin in the end
nums1=[1, 2, 1, 2, 1, 2, 1, 2, 3]
def optimized(nums):
    candidate_1=None
    candidate_2=None
    c1=0
    c2=0
    for i in range(0,len(nums1)):
        if nums[i]==candidate_1:
            c1+=1
        elif nums[i]==candidate_2:
            c2+=1
        elif c1==0:
            c1=1
            candidate_1=nums[i]
        elif c2==0:
            c2=1
            candidate_2=nums[i]
        else:
            c1-=1
            c2-=1
    res=[]
    if nums.count(candidate_1)>len(nums)//3:
        res.append(candidate_1)
    if nums.count(candidate_2)>len(nums)//3 and candidate_1!=candidate_2:
        res.append(candidate_2)
    return res
res=optimized(nums1)
print(res)
:q


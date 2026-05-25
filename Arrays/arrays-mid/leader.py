nums=[1,2,5,3,1,2]
i=0
res=[]
# Mine
while i<len(nums):
    count=len(nums)-i-1
    c=0
    j=i+1
    while j < len(nums):
        if nums[i]>nums[j]:
            c+=1
        j+=1
    if c==count:
        res.append(nums[i])
    i+=1
print(res)

#Slighlty better
while i<len(nums):
    leader=True
    j=i+1
    while nums[j]<nums[i]:
        leader=False
        break
    res.append(nums[i])
    i+=1
print(res)


#Optimized Here the idea is that we are iterating from the left so that range of (last to (i--) ) we find the max element nd we compare it with
# the ith position if the elemt is greater add it into the result and swap it with the max position
i=len(nums)-2
max=nums[len(nums)-1]
res.insert(0,nums[len(nums)-1])
print(res)
while i>0:
    if nums[i]>max:
        res.insert(0,nums[i])
        max=nums[i]
    i-=1
print(res)

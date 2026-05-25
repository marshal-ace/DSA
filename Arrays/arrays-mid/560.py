# nums=[0,0,0]
# k=0
# hashmap={}
# hashmap[0]=-1
# sum=c=0
# for i in range(len(nums)):
#     sum=sum+nums[i]
#     hashmap[sum]=i
# print(hashmap)
# for key,val in hashmap.items():
#     if key-k in hashmap:
#         c+=1
# 
nums=[1,2,3,-3,1,1,1,4,2,-3]
k=3
hashmap={0:1}
presum=0
count=0
for i in range(len(nums)):
    presum+=nums[i]
    if presum not in hashmap:
        hashmap[presum]=1
    if presum-k in hashmap:
        count+=hashmap[presum-k]
    # hashmap[presum]+=1  #here we store the pre sum when u get doubt check the subarray[1,2,3,-3,1,1,1] after reaching 
    # here we get presum as 3 count is becz when we check back 3:2 (3 sum appears 2 times before means 2 arrays )
print(hashmap)
print(count)
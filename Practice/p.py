# nums=[10,5,2,7,1,9]
# k=15
# l=r=sum=0
# max_1=0
# while r<len(nums):
#     sum=sum+nums[r]
#     while sum>k:
#         sum=sum-nums[l]
#         l+=1
#     if sum==k:
#         max_1=max(max_1,r-l+1)
#     r+=1
# print(max_1)

        

# nums=[7,6,4,3,1]
# max_p=0
# i=1
# min_i=nums[0]
# while i<len(nums):
#     max_p=max(max_p,nums[i]-min_i)
#     min_i=min(min_i,nums[i])
#     i+=1
# print(max_p)


# print("Hi")

# nums=[2,1,5,4,3,0,0]
# def rev(nums,l,r):
#     nums[l:r+1]=nums[l:r+1][::-1]
#     return nums
# i=len(nums)-2
# ind=-1
# while i>=0:
#     if nums[i]<nums[i+1]:
#         ind=i
#         break
#     i-=1
# if ind==-1:
#     print(nums[::-1])
# j=len(nums)-1
# while j>0:
#     if nums[j]>nums[ind]:
#         nums[ind],nums[j]=nums[j],nums[ind]
#         break
#     j-=1
# nums=rev(nums,ind+1,len(nums)-1)
# print(nums)


# nums=[1,2,5,3,1,2]
# max_1=nums[len(nums)-1]
# i=len(nums)-2
# while i>=0:
#     max_1=max(max_1,nums[i])
#     i-=1
# print(max_1)
# res=[]
# res.insert(0,nums[len(nums)-1])
# print(res)

nums=[1,1,1,11,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6 ]
# count=1
# i=0
# max_count=0
# last_smol=float("-inf")
# nums.sort()
# print(nums)
# while i<len(nums):
#     if nums[i]-1==last_smol:
#         last_smol=nums[i]
#         count+=1
#     elif nums[i]!=last_smol:
#         last_smol=nums[i]
#         count=1
#     max_count=max(count,max_count)
# #     i+=1
# # print(max_count)
# longest=0
# count=0
# st=set()
# for i in nums:
#     st.add(i)
# for it in st:
#     if it-1 not in st:
#         count=1
#         x=it
#         while x+1 in st:
#             x=x+1
#             count+=1
#         longest=max(count,longest)
# print(longest)

nums=[1, 2,3]
k=3
count=0
sum=0
hashmap={0:1}
i=0
while i<len(nums):
    sum+=nums[i]
    if sum not in hashmap:
        hashmap[sum]=0
    if sum-k in hashmap:
        count+=hashmap[sum-k]
    hashmap[sum]+=1
    i+=1
print(count)
# 2148. Count Elements With Strictly Smaller and Greater Elements 
# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

nums=[11,7,2,15]
def check(nums):
    count=0
    maxn=minn=nums[0]
    for i in nums[1:]:
        maxn=max(maxn,i)
        minn=min(minn,i)
    for i in nums:
        if minn<i and maxn>i:
            count+=1
    return count
print(check(nums))
#1800
# Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

nums=[12,17,15,13,10,11,12]

def maximun(nums):
    last_seen=sum=max_sum=0
    i=0
    while i<len(nums):
        if nums[i]>last_seen:
            sum=sum+nums[i]
            last_seen=nums[i]
        elif nums[i]<=last_seen:
            max_sum=max(max_sum,sum)
            sum=0
            sum=sum+nums[i]
            last_seen=nums[i]
        max_sum=max(max_sum,sum)
        i+=1
    return max_sum
print(maximun(nums))
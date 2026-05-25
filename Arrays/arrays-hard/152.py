'''152. Maximum Product Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.'''
'''Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.'''

#TC-O(n2)--SC--O(1)
nums=[-2,0,-1]
def brute(nums):
    i=0
    res=float("-inf")
    while i<len(nums):
        j=i+1
        res=max(res,nums[i])
        product=nums[i]
        while j<len(nums):
            product=product*nums[j]
            res=max(res,product)
            j+=1
        i+=1
    return res
print(brute(nums))

#Optimal Prefix and Suffix multiplication
#When zero's cme change it into 1 an do multiplication again
def optimal(nums):
    presum=suffixsum=1
    ans=float("-inf")
    n=len(nums)
    for i in range(len(nums)):
        if presum==0:
            presum=1
        if suffixsum==0:
            suffixsum=1
        presum=presum*nums[i]
        suffixsum=suffixsum*nums[n-i-1]
        ans=max(ans,presum,suffixsum)
    return ans
print(optimal(nums))
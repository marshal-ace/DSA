#Largest Subarray with Sum 0
nums=[1,0,-4,3,1,0]
def brute(nums):
    sum=0
    max_len=0
    hashmap={}
    for i in range(len(nums)):
        sum=sum+nums[i]
        if sum==0:
            max_len=max(max_len,i+1)
        if sum-0 in hashmap:
            length=i-hashmap[sum-0]
            max_len=max(max_len,length)
        if sum not in hashmap:
            hashmap[sum]=i
    return max_len
print(brute(nums))
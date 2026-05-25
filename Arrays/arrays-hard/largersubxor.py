
nums=[4, 2, 2, 6, 4]
def brute(nums):
    i=0
    k=6
    count=0
    while i<len(nums):
        j=i+1
        xor=nums[i]
        if nums[i]==k:
            count+=1
        while j<len(nums):
            xor=xor^nums[j]
            if xor==k:
                count+=1
            j+=1
        i+=1
    return count
# print(brute(nums))
# def optimal(nums):
#     hashmap={-1:0}
#     k=6
#     count=0
#     xor=nums[0]
#     for i in range(1,len(nums)):
#         xor=xor^nums[i]
#         if nums[i]^xor in hashmap:
#             count+=1
#         if xor not in hashmap:
#             hashmap[xor]=i
#     return count
def optimal(nums):
    xr=0
    k=6
    hashmap={0:1}
    count=0
    for i in range(len(nums)):
        xr=xr^nums[i]
        x=xr^k
        count+=hashmap.get(x,0)
        hashmap[xr]=hashmap.get(xr,0)+1
    return count
print(optimal(nums))



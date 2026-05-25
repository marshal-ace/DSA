import array as a 
nums=a.array('i',[-2,1,-3,4,-1,2,1,-5,4])

def sum():
    sum=0
    i=0
    max_sum=0
    while i<len(nums):
        sum+=nums[i]
        if sum<0:
            sum=0
        i+=1
        max_sum=max(max_sum,sum)
    return max_sum

## Kadane Algo for Negative Sum

def neg_sum(nums):
    max_sum=sum=nums[0]
    i=1
    start=end=0
    while i<len(nums):
        sum+=nums[i]
        if sum<nums[i]:
            sum=nums[i]
            start=i
        if sum>max_sum:
            max_sum=sum
            end=i
        
        i+=1
    return max_sum,start,end
print(neg_sum(nums))

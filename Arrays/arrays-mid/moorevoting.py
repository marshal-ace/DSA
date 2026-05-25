#This is Moore Voting Algo to find the majority element > n/2 with 0(n) Time and 0(1) Space

import array as a
nums=a.array('i',[7, 0, 1, 7, 2, 7, 3, 7, 4, 7, 7])

def moore(nums):
    count=0
    for i in range(0,len(nums)):
        if count==0:
            ele=nums[i]
            count=1
        elif count==nums[i]:
            count+=1
        else:
            count-=1
    count1=0
    for i in range(0,len(nums)):
        if ele==nums[i]:
            count+=1
    if count>len(nums)/2:
        return ele
print(moore(nums))
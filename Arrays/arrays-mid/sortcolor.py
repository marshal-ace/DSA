import array as a
nums=a.array('i',[2,0,2,1,1,0])
n=len(nums)
def sortcolor(nums):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
                
print(sortcolor(nums))

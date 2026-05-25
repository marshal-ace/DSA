import array as a
nums=a.array('i',[0,1,1,0,1,2,1,2,0,0,0])


def max(nums):
    low=mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(max(nums))

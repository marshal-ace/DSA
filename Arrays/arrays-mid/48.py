nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def brute(nums):
    nums1=[]
    nums2=[]
    for i in range(0,len(nums)):
        nums1=[]
        for j in range(len(nums)-1,-1,-1):
            nums1.append(nums[j][i])
        nums2.append(nums1)
    return nums2
#Optimal i was a dickhead :)
def optimal(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    for i in range(0,len(nums)):
        nums[i].reverse()
    return nums
print(optimal(nums))
        
'''Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.'''
# Input: nums = [2, 3, 7, 1, 3, 5]
# Output: 5
# Explanation:
# The responsible indexes are:
# nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
# nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
# nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
# nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
# nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5
nums=[2, 3, 7, 1, 3, 5]
# Time Complexity-O(n2)--Space Complexity O(1)
def brute(nums):
    i=0
    count=0
    while i<len(nums):
        j=0
        while j<len(nums):
            if nums[i]>nums[j] and i<j:
                count+=1
            j+=1
        i+=1
    return count
# print(brute(nums))


#Optimal using Merge Sort
#Intution is built on merge sort

def merge(nums,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    count=0
    while left<=mid and right<=high:
        if nums[left]<= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            #Left and Right Virtual array are sorted so if left(index 1) element is greater than right (index 1)
            #all the elements in the left array frm index1 to other end of lef array are greater so we are adding that count
            count+=(mid-left+1)
            right+=1
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1
    for i in range(low,high+1):
        nums[i]=temp[i-low]
    return count
def mergesort(nums,low,high):
    #Base Condition
    #If the array has one element no further sorting return and merge
    if low>=high:
        return 0
    mid=(low+high)//2
    count=0
    count+=mergesort(nums,low,mid)
    count+=mergesort(nums,mid+1,high)
    count+=merge(nums,low,mid,high)
    return count
def run(nums):
    low=0
    high=len(nums)-1
    return  mergesort(nums,low,high)
print(run(nums))
    
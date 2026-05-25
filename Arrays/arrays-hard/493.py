'''Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
'''
'''
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1'''

# Time Complexity-O(n2)--Space Complexity -O(1)
nums=[2,4,3,5,1]
def brute(nums):
    res=[]
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[i]>2*(nums[j]):
                res.append([i,j])
            j+=1
        i+=1
    return res
# print(brute(nums))

def merge(nums,low,mid,high):
    temp=[]
    l=left=low
    r=right=mid+1
    count=0
    while l<=mid and r<=high:
        if nums[l]>2*nums[r]:
            count+=(mid-l+1)
            r+=1
        else:
            l+=1
    while left<=mid and right<=high:
        if nums[left]<= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            # if nums[left]>2*(nums[right]):
            #     count+=1 #Mistake : I was counting one -to - one yet we need to count on bulk as both sides are sorted
            #     count+=(mid-left+1)
            #Left and Right Virtual array are sorted so if left(index 1) element is greater than right (index 1)
            #all the elements in the left array frm index1 to other end of lef array are greater so we are adding that count
            # count+=(mid-left+1)
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
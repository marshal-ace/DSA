#Merge Sorted Array
'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''


nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
#TC-O((m+n)log(m+n))​ ---- SC O(m+n)
def brute(nums1,nums2):
    nums1.extend(nums2)
    nums1.sort()
    return nums1
# print(brute(nums1,nums2))

#TC- O(m+n)-- SC-O(m+n)

def better(nums1,nums2):
    m=3
    n=3
    res=[]
    i=j=0
    while i<m and j<n:
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        elif nums1[i]==nums2[j]:
            res.append(nums1[i])
            res.append(nums2[j])
            i+=1
            j+=1
        else:
            res.append(nums2[j])
            j+=1
    while i<m:
        res.append(nums1[i])
        i+=1
    while j<n:
        res.append(nums2[j])
        j+=1
    return res
# print(better(nums1,nums2))
def optimal(nums1,nums2):
    m=3
    n=3
    i=m-1
    j=n-1
    k=(m+n)-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    while j>=0:
        nums1[k]=nums2[j]
        k-=1
        j-=1
    return nums1
print(optimal(nums1,nums2))


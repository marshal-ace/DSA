        #Next Perumtation
import array as a 
nums=a.array('i',[2,1,5,4,3,0,0])
# def perm(nums):
#     i=len(nums)-1
#     j=len(nums)-2
#     while j > 0:
#         min_1=9
#         for k in range(j,i+1):
#             if nums[k]>nums[j]:
#                 curr=nums[k]
#                 if curr<min_1:
#                     min_1=nums[k]
#                     id=k
#         if min_1>nums[j]:
#             a=[]
#             nums[j],nums[id]=nums[id],nums[j]
#             l=len(nums)-1
#             while l>j:
#                 a.append(nums.pop(l))
#                 l-=1
#             a.sort()
#             nums.extend(a)
#             return nums
#         else:
#             j-=1
# print(perm(nums))
def reverse(nums,l,r):
    nums[l:r+1]=nums[l:r+1][::-1]
    return nums
def optimized(nums):
    i=len(nums)-2
    ind=-1
    while i>=0:
        if nums[i]<nums[i+1]:
            ind=i
            break
        i-=1
    if ind==-1:
        nums.reverse()
        return nums
    j=len(nums)-1
    while j>0:
        if nums[j]>nums[ind]:
            nums[ind],nums[j]=nums[j],nums[ind]
            break
        j-=1
    nums=reverse(nums,ind+1,len(nums)-1)
    return nums
print(optimized(nums))
















#We are given two arrays nums1 and nums2 we need sort that all the smallest will be on nums1 and all the largest will be on nums2

nums1=[1,3,5,7]
nums2=[0,2,6,8,9]
m=len(nums1)
n=len(nums2)

#Optimal
#This is Optimal Solution1
def optimal1(nums1,nums2):
    i=m-1
    j=0
    while i>=0 and j<n:
        if nums1[i]>nums2[j]:
            nums1[i],nums2[j]=nums2[j],nums1[i]
            i-=1
            j+=1
        else:
            break
    nums1.sort()
    nums2.sort()
    return nums1,nums2
# print(optimal1(nums1,nums2))

#There is another optimal solution 2 which is implemented by using Gap Method Which is taken by Shell Sort

def swapgreater(nums1,nums2,left,right):
    if nums1[left]>nums2[right]:
        nums1[left],nums2[right]=nums2[right],nums1[left]
def optimal2(nums1,nums2):
    gap=(m+n+1)//2
    #The Gap is calculated again when right crosses the boundaries
    #Whn right>total length,Gap is reduced and "Gap" loop is run till Gap is 1
    
    while gap>0:
        left=0
        right=left+gap
        #Mistake-1 Just took N
        #But we are taking whole length and treating it as one array
        while right<(m+n):
            #3 Conditions
            #Condition-1
            #if left is in arr1 and right is in arr2
            if left<m and right>=m:
                swapgreater(nums1,nums2,left,right-n)
            #Condition-2
            #if left is in arr2 and right is in arr2
            elif left>=m:
                swapgreater(nums1,nums2,left-n,right-n)
            #Condition-3
            #if left is in arr1 and right is in arr1
            else:
                swapgreater(nums1,nums2,left,right)
            left+=1
            right+=1
        #Mistake 2 Main loop breaking condition wasn't added
        if gap==1:
            break
        else:
            #Mistake 3: gap should be reduced i reduced m+n causing infinite loop
            gap=(gap+1)//2
    return(nums1,nums2)
print(optimal2(nums1,nums2))
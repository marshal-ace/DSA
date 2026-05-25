nums=[1, 9, 3, 10, 4, 20, 2]
def brute(nums):
    i=0
    c_max=0
    while i<len(nums):
        j=0
        c=1
        n=nums[i]
        if n+1 in nums:
            while j<len(nums):
                n+=1
                if n in nums:
                    c+=1
                else:
                    break
                j+=1
        i+=1
        c_max=max(c,c_max)
    return c_max
#-----------------------------------------------------------------------
nums=[1,1,1,11,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6 ]
def better(nums):
    nums.sort()
    longest=1
    count=1
    i=0
    last_smaller=float('-inf')
    while i<len(nums):
        if nums[i]-1 == last_smaller:
            last_smaller=nums[i]
            count+=1
        elif nums[i]!=last_smaller:
            last_smaller=nums[i]
            count=1
        longest=max(count,longest)
        i+=1
    return longest


        
        
#------------------------------
nums=[1,1,1,11,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6 ]
def optimal(nums):
    st=set()
    longest=1
    for i in nums:
        st.add(i)
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it
            while x+1 in st:
                x=x+1
                cnt+=1
            longest=max(longest,cnt)
    return longest
print(better(nums))
        
        


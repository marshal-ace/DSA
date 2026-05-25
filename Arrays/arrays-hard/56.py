'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

nums=[[1,3],[2,6],[8,10],[15,18]]
#Time Complexity-0(2N)+N log N --- Space Compllexity O(N)
def brute(nums):
    nums.sort()
    ans=[]
    for i in range(len(nums)):
        start=nums[i][0]
        end=nums[i][1]
        if len(ans)!=0 and end<=ans[-1][1]:
            continue
        for j in range(i+1,len(nums)):
            if nums[j][0]<end:
                end=max(end,nums[j][1])
            else:
                break
        ans.append([start,end])
    return ans
print(brute(nums))
def optimal(nums):
    ans=[]  
    for i in range(len(nums)):
        if len(ans)==0 or nums[i][0]>ans[-1][1]:
            ans.append([nums[i][0],nums[i][1]])
        else:
            ans[-1][1]=max(nums[i][1],ans[-1][1])
    return ans
print(optimal(nums))
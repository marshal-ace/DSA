'''Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.'''
'''Input: nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation:
1 appears two times in the array and 2 is missing from nums'''

nums=[3,5,4,1,1]
#Time Complexity 0(n2)--Space Complexity 0(1)
def brute(nums):
    res=[]
    for i in range(1,len(nums)+1):
        count=0
        for j in range(len(nums)):
            if i==nums[j]:
                count+=1
        if count==0 or count==2:
            res.append(i)
    return res
# print(brute(nums))
def brute_method(nums):
    res=[]  
    for i in range(1,len(nums)+1):
        cout=nums.count(i)
        if cout==0 or cout==2:
            res.append(i)
    return res
# print(brute_method(nums))
#Better He are Strivers used Hasharray so what we did was first first we initialzed the hashmap with keys  and the value "0"
#next what we did was iterate over the array using get function after that we can use if condition and get the keys whose value is 0 and 2
#Like this we can this is the better
#TL-O(2n) SL-O(n)
def better(nums):
    hashmap={}
    for i in range(1,len(nums)+1):
        hashmap[i]=0
    for i in range(1,len(nums)):
        hashmap[nums[i]]=hashmap.get(nums[i],0)+1
    return hashmap
print(better(nums))
#Optimal 1 using Mathematicssss
#x=repeating element
#y=missing element
#we find two equation using sum of n natural numbers and sum of squares of n natural numbers and solve this
def optimal1(nums):
    n=len(nums)
    # sum_nums=sum(nums)
    sn=n*(n+1)/2  #Sum of N natural numbrs
    s2n=(n*(n+1) * (2*n+1)) / 6 #Square of sum of n natural numbers
    s=0 #sum of numbers in array
    s2=0 #square of sum of numbers in array
    for i in nums:
        s=s+i
        s2=s2 + (i*i)
    val1=s-sn  #Equation valuesss     
    val2=s2-s2n
    val2=val2/val1
    x=int((val2+val1)/2)
    y=int(x-val1)
    return [x,y]
print(optimal1(nums))

def optimal2(nums):
    pass
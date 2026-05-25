import array as a 


nums=a.array('i',[5,4,-1,7,8])
max_sum=float('-inf')
i=0
while i<len(nums):
    j=i
    while j<len(nums):
        sum=0
        for k in range(i,j+1):
            sum+=nums[k]
            k+=1
        if sum>max_sum:
            max_sum=sum
        j+=1
    
    i+=1
    

print(max_sum)
  
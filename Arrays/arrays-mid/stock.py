import array as a 
nums=a.array('i',[7,1,5,3,6,4])


def brute(nums):
    i=0
    max_sum=0
    while i<len(nums)-1:
        j=i+1
        while j<len(nums):
            sum=nums[j]-nums[i]
            print(f"{nums[j]}-{nums[i]}={sum}")
            max_sum=max(sum,max_sum)
            j+=1
        i+=1
    return max_sum
# nums=a.array('i',[7,1,5,3,6,4])
#Optimized Hunch Profits= Selling Price - Buying Price : Its also the difference of changes between when we hold the stock
#Kadane is something we need to hold if only we get profits (Like if they are use to use) if they aren't usefull  throw them
def optimized(nums):
    i=1
    max_profit=0
    sum=0
    while i<len(nums):
        profit=nums[i]-nums[i-1]
        sum+=profit
        if sum<0:
            sum=0
        max_profit=max(sum,max_profit)
        i+=1
    return max_profit
print(optimized(nums))

def striveroptimized(nums):
    i=1
    max_profit=0
    min_1=nums[0]
    while i<len(nums):
        profit=nums[i]-min_1
        max_profit=max(profit,max_profit)
        min_1=min(min_1,nums[i])
        i+=1
    return max_profit
print(striveroptimized(nums))
            
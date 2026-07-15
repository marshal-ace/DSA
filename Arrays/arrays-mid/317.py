# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums=[1,2,3,1]
def check(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(check(nums))
import array as a
nums=[3,2,3]
hashmap={}

def majority(nums):
    for key,vale in enumerate(nums):
        if vale not in hashmap:
            hashmap[vale]=1
        else:
            hashmap[vale]+=1
    for key,vale in hashmap.items():
        if vale>len(nums)/2:
            return key
        
print(majority(nums))
import array as a
nums=a.array('i',[2,7,11,13])
k=9

hashmap={}
for key,value in enumerate(nums):
    hashmap[value]=key
for key,value in enumerate(nums):
    if (k-value) in hashmap and key !=hashmap[k-value]:
        print(key,hashmap[k-value])
        break
        


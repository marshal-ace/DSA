import array as a 
nums=a.array('i',[3,1,-2,-5,2,-4])
# pos=[]
# neg=[]
# for i in range(0,len(nums)):
#     if nums[i]<0:
#         neg.append(nums[i])
#     else:
#         pos.append(nums[i])
# res=[]
# for i in range(0,len(nums)//2):
#     res.append(pos[i])
#     res.append(neg[i])
# print(res)
# print(pos)
# print(neg)  
# res=[]


#Optimal
res=[0]*len(nums)
pos=0
neg=1
for i in nums:
    if i<0:
        res[neg]=i
        neg+=2
    else:
        res[pos]=i
        pos+=2
print(res)

    

        
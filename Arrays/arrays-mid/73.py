nums=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zero={}
k=0
def llama(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j]==0:
                k+=1
                zero[k]=[i,j]

    for key,value in zero.items():
        if value[0]-1<len(nums) and value[1]<len(nums[value[0]]): #i--
            i=value[0]
            while i>=0:
                nums[i][value[1]]=0
                i-=1
        if value[0]+1<len(nums) and value[1]<len(nums[value[0]]): #i++
            i=value[0]
            while i<len(nums):
                nums[i][value[1]]=0
                i+=1
        if value[0]<len(nums) and value[1]<len(nums[value[0]-1]): #j--
            i=value[1]
            while i>=0:
                nums[value[0]][i]=0
                i-=1
        if value[0]<len(nums) and value[1]<len(nums[value[0]+1]): #j++
            i=value[1]
            while i<len(nums[value[1]]):
                nums[value[0]][i]=0
    return nums
#--- Brute Striver Time Complexity which is Close to 0(n^3)
def markdowni(i):
    for j in range(0,len(nums[i])): 
        if nums[i][j]!=0:
            nums[i][j]=-1
def markdownj(j):
    for i in range(0,len(nums)):
        if nums[i][j]!=0:
            nums[i][j]=-1
def brute(nums):
    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            if nums[i][j]==0:
                markdowni(i)
                markdownj(j)
    
    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            if nums[i][j]==-1:
                nums[i][j]=0
    return nums
#print(brute(nums))
#Better Solution
def better(nums):
    col=[0]*len(nums[0])
    row=[0]*len(nums)
    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            if nums[i][j]==0:
                col[j]=1
                row[i]=1
    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            if row[i]==1 or col[j]==1:
                nums[i][j]=0
    return nums
#print(better(nums))
#Optimal-------------------------------------------
def optimal(nums):
    #counter is nothing but marker
    #It marks if the element is 0
    #row counter= nums[.....][0]
    #colum counter=nums[0][.....]
    col0=1
    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            if nums[i][j]==0:
                nums[i][0]=0 # row counter
                if j==0:
                    col0=0
                else:
                    nums[0][j]=0 #column counter 
    for i in range(1,len(nums)):
        for j in range(1,len(nums[i])):
            if nums[i][0]==0 or nums[0][j]==0:
                nums[i][j]=0
    if nums[0][0] == 0:
        #Row Marker
        for j in range(0,len(nums[i])):
            nums[0][j]=0
        #Column Marker
    if col0==0:
        for i in range(0,len(nums)):
            nums[i][0]=0
    return nums
print(optimal(nums))
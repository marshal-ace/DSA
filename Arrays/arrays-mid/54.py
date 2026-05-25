nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=len(nums)
m=len(nums[0])
top=left=0
right=m-1
bottom=n-1
res=[]
#make sure to give the edges cases a look left<right and top<bottom my idealogy was crct but i didnt know how to implement now i understood
#we are changing i to top,bottom,left,right and changing accordingly

while left<=right and top<=bottom:
    i=left
    while i<=right:
        res.append(nums[top][i])
        i+=1
    top+=1
    i=top
    while i<=bottom:
        res.append(nums[i][right])
        i+=1
    right-=1
    if top<=bottom:
        i=right
        while i>=left:
            res.append(nums[bottom][i])
            i-=1
        bottom-=1
    if left<=right:
        i=bottom
        while i>=top:
            res.append(nums[i][left])
            i-=1
        left+=1
print(res)
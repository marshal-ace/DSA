#Pascals Triangle
'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''
#Time and Space Complexity
#O(n^2) & O(n^2)
def brute(n): #n= number of rows the pascal triangle to be printed
    res=[]
    for r in range(n):
        temp=[]
        for c in range(r+1):
            if c==0 or r==c:
                temp.append(1)
            else:
                temp.append(res[r-1][c-1]+res[r-1][c])
        res.append(temp)
    return res

# optimized 
# Everything is baased on nCr forumla 7

#If they give row and col (index values) and print that digit we use nCr forumla
#n-1Cr-1
def digit(r,c):
    ans=1
    for i in range(c):
        ans=ans*(r-i)
        ans=ans//(i+1)
    return ans
print(digit(5,1))
# if the question to print a row just by giving the row number
def row(n):
    res=[]
    res.append(1)
    ans=1
    for col in range(1,n):
        ans=ans*(n-col)
        ans=ans//col
        res.append(ans)
    return res
print(row(6))
# if the question asks us to print pascals triangle giving by the row numbers
def pascal(n):
    ans=[]
    for i in range(1,n+1):
        ans.append(row(i))
    return ans
print(pascal(5))



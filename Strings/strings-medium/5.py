#Longest Palindromic Strings

#Palindromic Strings:A substring is a contiguous non-empty sequence of characters within a string

# Time Complexity O(n3) nd Space Complexity O(n)
s="cbbd"
def brute(s):
    i=0
    max_text=""
    while i<len(s):
        test=""
        j=i
        while j<len(s):
            test+=s[j]
            rev_test=test[::-1]
            if rev_test==test:
                if len(test)>len(max_text):
                    max_text=test
            j+=1
        i+=1
    return max_text
# print(brute(s))


# left=len(s)//2
# right=left+1
# final=""
# while left>0 and right<len(s):
#     if s[left]==s[right]:
#         test=s[left:right+1]
#         rev_test=test[::-1]
#         if test==rev_test and len(test)>final:
#             final=test
#     left-=1
#     right+=1
# print(final)

 #Intution instead of checking all substrings we select one char as middle and expand and check
 #We take one character as middle and check all possibilities


def optimal(s):
    final=""

    def expand(left,right):
        while left >=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    for i in range(len(s)):
        #odd and even are related to middle for even length there is no single middle so we check all

        odd=expand(i,i)
        even=expand(i,i+1)

        if len(odd)>len(final):
            final=odd
        if len(even)>len(final):
            final=even
    return final
print(optimal(s))

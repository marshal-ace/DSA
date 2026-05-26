# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


#TC-O(n) SC-O(n)
#This approach involves using the string in-builtin methods
s="the sky is blue"
def optimal1(s):
    s=s.split()
    s=s[::-1]
    s=" ".join(s)
    return s
print(optimal1(s))

#TC-0(N) SC-0(N)
#This approach where we scan from right to left
# First Ignore all the right side spaces and mark the end of the word
# Then we need to find the Start 
# after that extract the word and if the result string isn't empty add a space and add that word
def optimal2(s):
    i=len(s)-1
    result=""
    while i>=0:
        while i>=0 and s[i] ==" ":
            i-=1
        if i<0:
            break
        end=i
        while i>=0 and s[i]!=" ":
            i-=1
        word=s[i+1:end+1]
        if result!="":
            result+=" "
        result+=word
    return result
print(optimal2(s))
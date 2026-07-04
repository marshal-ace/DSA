
# 58. Length of Last Word

# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.
s="luffy is still joyboy"
def last(s):    
    s=s.strip()
    length=len(s)-1
    check=length
    while length>=0 and s[length]!=" ":
        length-=1
    final=check-length
    return final
length=last(s)
print(length)
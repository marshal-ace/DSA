'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.'''


s = "abcde"
goal = "cdeab"
# def brute(s,goal):
#     i = 0
#     count = 0

#     while i < len(s):
#         if s[i] == goal[0]:
#             count = i
#             break
#         else:
#             i += 1

#     s = list(s)

#     for j in range(count):
#         x = s.pop(0)
#         s.append(x)

#     s = "".join(s)

#     if s == goal:
#         print(True)
#     else:
#         print(False)

def optimal(s,goal):
    s=s+s
    if goal in s:
        return True
    return False
print(optimal(s,goal))
#!/usr/bin/python

def extention(s,i,j):
    while i >=0 and j< len(s) and s[i] == s[j]:
        i -= 1
        j += 1

    return i+1, j-1

def plalindrome(s):
    result_str = []
    for i in range(len(s)):
        start,end = extention(s,i,i)
        result_str.append(s[start:end+1])
        start,end = extention(s,i,i+1)
        result_str.append(s[start:end+1])
         
    return max(result_str,key=len) if result_str else ''



print plalindrome('babab')
print plalindrome('b')
print plalindrome('bb')
print plalindrome('')
print plalindrome('abbc')
print plalindrome('abba')
print plalindrome('ababa')
print plalindrome('abcdc')
print plalindrome('abcdcbdbf')


#!/usr/bin/python

def strStr(haystack,needle):
    i = j = 0
    match_length = 0
    if needle == '':
        return 0

    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            match_length += 1
        else:
            i = i - match_length + 1
            j = 0
            match_length = 0


    if j == len(needle):
        return i-j

    return -1


haystack = 'ababac'
needle = 'abac'
print haystack,needle,strStr(haystack,needle)

haystack = 'hello'
needle = 'll'
print haystack,needle,strStr(haystack,needle)

haystack = ''
needle = 'll'
print haystack,needle,strStr(haystack,needle)

haystack = 'abc'
needle = 'b'
print haystack,needle,strStr(haystack,needle)

haystack = 'abcb'
needle = 'bc'
print haystack,needle,strStr(haystack,needle)

haystack = 'abcba'
needle = 'bcb'
print haystack,needle,strStr(haystack,needle)

haystack = 'aaa'
needle = 'aaa'
print haystack,needle,strStr(haystack,needle)

haystack = 'baa'
needle = 'aaa'
print haystack,needle,strStr(haystack,needle)

haystack = 'baa'
needle = 'aa'
print haystack,needle,strStr(haystack,needle)

haystack = 'abcbaabcabc'
needle = 'cab'
print haystack,needle,strStr(haystack,needle)


haystack = 'abcbaabcabc'
needle = ''
print haystack,needle,strStr(haystack,needle)


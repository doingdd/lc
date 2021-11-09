#!/usr/bin/python
from collections import Counter

def findSubStr(s,words):
    rt_list = []
    if not words:
        return [0]

    if not s:
        return []

    ## diff the dict{word:time} of words and split of s
    dict_words = Counter(words)
    word_num = len(words)
    word_length = len(words[0])
    ## slide window
    i = 0
    j = i + word_num * word_length
    if len(s) < j:
        return []

    while j <= len(s):
        dict_s = {}
        for k in range(word_num):
            split_str = s[i+k*word_length:i+(k+1)*word_length]
            dict_s[split_str] = dict_s.get(split_str,0) + 1

        #print dict_words,dict_s
        if dict_words == dict_s:
            rt_list.append(i)

        i += 1
        j += 1
    
    return rt_list




s = "foobar"
words = ["foo","bar"]
rt = findSubStr(s,words)
print s,words,rt

s = "wordgoodgoodgoodbestword"
words = ["word","good","best",'word']
print s,words,findSubStr(s,words)

s = "foobar"
words = ["foo","bar",'foo']
print s,words,findSubStr(s,words)

s = "foobar"
words = ["","",'']
print s,words,findSubStr(s,words)

s = "youaremysunshine"
words = ["my","su"]
print s,words,findSubStr(s,words)


s = "ababcb"
words = ["ba","cb"]
print s,words,findSubStr(s,words)

s = "foobaryouwordyouwordbaryoufoobar"
words = ["bar","you","wor"]
print s,words,findSubStr(s,words)


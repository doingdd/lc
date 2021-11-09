#!/usr/bin/python

def func(s,t):
    result_list = []
    i = 0
    t_count = {}
    need_count = len(t)
    for k in t:
        t_count[k] = t_count.get(k,0) + 1

    for j,c in enumerate(s):
        if c in t_count:
            t_count[c] -= 1
            if t_count[c] >= 0:
                need_count -= 1

        if need_count == 0:
            while True:
                if s[i] in t_count and t_count[s[i]] == 0:
                    t_count[s[i]] += 1
                    need_count += 1
                    result_list.append(s[i:j+1])
                    i += 1
                    break
                else:
                    if s[i] in t_count:
                        t_count[s[i]] += 1

                    i += 1


    if result_list:
        return min(result_list,key=len)
    
    return ''


assert func('abc','abc') == 'abc'
assert func('abc','a') == 'a'
assert func('abc','ab') == 'ab'
assert func('abcfdsadf','acf') == 'abcf'
assert func('abcfdsadf','afd') == "adf"
assert func('abcfdsadf','aR') == ''
assert func('abcfdsadf','cff') == 'cfdsadf'
assert func('abcfdsadf','sad') == 'dsa'
assert func('ADOBECODEBANC','ABC') == 'BANC'

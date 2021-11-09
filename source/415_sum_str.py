#!/usr/bin/python
def sum_str(num1,num2):
    i,j = len(num1)-1,len(num2)-1
    ad = 0
    result = ""
    while i >=0 or j >=0 or ad:
        s1 = int(num1[i]) if i >= 0 else 0
        s2 = int(num2[j]) if j >= 0 else 0
        r = (s1 + s2 + ad) % 10
        ad = (s1 + s2 + ad) / 10
        result = str(r) + result
        i -= 1
        j -= 1

    return result


a,b = "104","24"
print a,b,sum_str(a,b)
a,b = "10","10"
print a,b,sum_str(a,b)
a,b = "134","71"
print a,b,sum_str(a,b)
a,b = "134","79"
print a,b,sum_str(a,b)
a,b = "999","1"
print a,b,sum_str(a,b)

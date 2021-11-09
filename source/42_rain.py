#!/usr/bin/python
def get_re(height):
    rt = 0
    l_max = 0
    r_max = 0
    l_max_list = [0]
    r_max_list = [0]*len(height)
    i = 1
    while i < len(height):
        l_max = max(l_max,height[i-1])
        l_max_list.append(l_max) 
        i += 1

    i = len(height) - 2
    while i >= 0:
        r_max = max(r_max,height[i+1])
        r_max_list[i] = r_max
        i -= 1

    i = 0
    while i < len(height):
        rain = min(l_max_list[i],r_max_list[i]) - height[i]
        if rain > 0:
            rt += rain

        i += 1

            
    #print l_max_list
    #print r_max_list
    return rt
            
def get_re1(height):
    if not height:
        return 0

    rt = 0
    left = 0
    right = len(height) - 1
    l_max = height[0]
    r_max = height[-1]
    while left <= right:
        l_max = max(l_max,height[left])
        r_max = max(r_max,height[right])

        if l_max < r_max:
            if l_max > height[left]:
                rt += (l_max-height[left])

            left += 1

        else:
            if r_max > height[right]:
                rt += (r_max - height[right])

            right -= 1

                
    return rt


def get_re2(height):
    rt = 0
    if len(height) < 3:
        return rt

    left = 0
    right = len(height) - 1
    l_max = height[0]
    r_max = height[-1]
    while left < right:
        l_max = max(l_max,height[left])
        r_max = max(r_max,height[right])
        if l_max < r_max:
            if height[left] < l_max:
                rt += (l_max-height[left])
            
            left += 1
        else:
            if height[right] < r_max:
                rt += (r_max-height[right])

            right -= 1

    return rt
                




































height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = get_re(height)
print height,a

height = [4,2,0,3,2,5]
a = get_re(height)
print height,a

height = []
a = get_re(height)
print height,a

height = [0,0,0]
a = get_re(height)
print height,a

height = [0,1,0]
a = get_re(height)
print height,a

height = [1,0,1]
a = get_re(height)
print height,a
print '----'*10
height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = get_re1(height)
print height,a
print '----'*10
height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = get_re2(height)
print height,a

height = [4,2,0,3,2,5]
a = get_re1(height)
print height,a

height = []
a = get_re1(height)
print height,a

height = [0,0,0]
a = get_re1(height)
print height,a

height = [0,1,0]
a = get_re1(height)
print height,a

height = [1,0,1]
a = get_re1(height)
print height,a

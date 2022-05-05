#!/usr/bin/python

case = [('11','123'),
       ('456','77'),
       ('0','0'),
       ('0','123'),
       ('999','99'),
        ('456','77')
       ]

def sub_str(s1,s2):
    i,j = len(s1)-1,len(s2)-1
    c_bit = 0
    s3 = ''
    while i >= 0 or j >= 0:
        n1 = int(s1[i]) if i>=0 else 0
        n2 = int(s2[j]) if j>=0 else 0
        n_bit = (n1+n2+c_bit) % 10
        c_bit = (n1+n2+c_bit) / 10
        s3 = str(n_bit) + s3
        i -= 1
        j -= 1

    s3 = str(c_bit) + s3 if c_bit else s3


    return s3

for i in case:
    print 'case is {0},result is {1}'.format(i,sub_str(*i))


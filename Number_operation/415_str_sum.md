## 415.字符串相加

### 用例设计

有效等价类：num1 = '11',num2 = '123',输出‘134’

'456'+'77' = '533'

无效等价类：'' + '1', ''+''

特殊值：'0'+'0' = '0'， '0'+ '123' = '123', '999' + '99' = '1098'

```python
case = [('11','123'),
       ('456','77'),
       ('0','0'),
       ('0','123'),
       ('999','99')
        ('456','77')
       ]
```



### 思路与实现

这种相加的题的基本思路都很类似：两个指针，分别从后向前遍历两个字符串，用一个变量表示进位，另一个变量表示相加后的个位数，如果有某一个字符串遍历结束后，则补0，直到两个字符串都遍历结束为止

```python
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
```

输出:

```python
case is ('11', '123'),result is 134
case is ('456', '77'),result is 533
case is ('0', '0'),result is 0
case is ('0', '123'),result is 123
case is ('999', '99'),result is 1098
case is ('456', '77'),result is 533
```



### 总结

这个题有两个点需要注意，

一个是n_bit和c_bit的计算，b_bit要再c_bit之前，为什么呢？因为计算n_bit实际依赖上一轮循环中的c_bit，所以顺序如果反了是不对的

第二个注意的点是循环结束后，对c_bit的判断，如果余留了c_bit没有处理，算出来的数字会缺少最高的进位，比如case 999+99，最高位的“1”，就是通过循环后对c_bit的处理而来的，否则计算出错误的结果：098


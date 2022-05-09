## 补充4. 快速排序

### 用例设计

有效等价类：[1,2,3,4,5],[3,2,1],[1,1,3,2,2,1],[5,3]

无效等价类：[],

特殊值: [1],[1,1],[2,2,2],[9,8,7,6,5,4,1,2,3]

```python
```



### 思路及实现

快排的基本思路是归并，是将一个序列分解成左右两个序列，左边序列的元素值小于基准点，右边序列大于，并递归的处理左右两个子序列，知道子序列长度为1为止。

1. 选择一个基准点，pivot，这里无脑选择序列的第一个值为pivot(实际情况中，随机选择pivot的时间复杂度更好，涉及复杂的验证，这里为了实现简单就选择第一个元素)
2. 遍历当前的数组，把小于基准点的元素全移到基准点左边，大于的元素移到右边
3. 递归的对左右两个子序列进行第1和第2步骤，生成新的子序列，直到生成的子序列长度为1为止

选择基准点的思路简单，但是实现时，为了节省空间，使用换地交换的方式进行，就需要一个partition的函数，这个函数的作用是实现1和2步骤，并且返回交换后的基准点的索引，比如：`[4,3,1,2]`这个序列，基准点为`4`，那么执行完partition之后，这个序列应该变成`3,1,2,4`，并且返回基准点的index`3`

实现了paritiion之后，外层就需要调用它，并且按照返回的index，递归的处理index左侧的序列和右侧的序列，所以，partition的输入还应该包含序列的起始和结束的index值

```python
#!/usr/bin/python
def quick_sort(l):
    length = len(l)
    if length < 2:
        return l
    quick_s(l,0,length-1)

    return l

def quick_s(l,start,end):
    if start >= end:
        return
    p = partition(l,start,end)
    quick_s(l,start,p-1)
    quick_s(l,p+1,end)

def partition(l,start,end):
    pivot = l[end]
    i = start
    for j in range(start,end):
        if l[j] < pivot:
            l[i],l[j] = l[j],l[i]
            i += 1

    l[end],l[i] = l[i],l[end]
    return i

case = [[1,2,3,4,5],[3,2,1],[1,1,3,2,2,1],[5,3],
        [],
        [1],[1,1],[2,2,2],[9,8,7,6,5,4,1,2,3]]

for i in case:
  print "case is ",i
  print "result is ",quick_sort(i)


```

### 补充选取第一个元素作为pivot的写法，可以省去最后一次交换

```python
case = [
        [5,4,3,2,1],
        [1,2,3,4],
        [1],
        [],
        [1,2,2,2,3,1],
        [1,3,2,4],
        [3,1,2,4]
        ]
def quick_sort(nums):
    if len(nums) < 2:
        return nums

    quick_s(nums,0,len(nums)-1)

    return nums

def partition(nums,left,right):
    i = left
    pivot = nums[left]
    for j in range(left,right+1):
        if nums[j] < pivot:
            nums[j],nums[i] = nums[i],nums[j]
            i += 1

    return i

def quick_s(nums,left,right):
    if left < right:
        p = partition(nums,left,right)
        quick_s(nums,left,p-1)
        quick_s(nums,p+1,right)

for i in case:
    print i,quick_sort(i)
```



### 总结

快排的整体思路比较清晰，这里需要注意的是实现的方式，而且要注意实现时，循环的边界值

1. 递归时，把选出的p从左列表和右列表中剔除
2. 递归时的起止范围，end的选择是始终在最后一个index，而不是len的值
3. pivot的选取，这里选取最后一个元素有一个好处，就是在i和j交替往前走之后，最后的i实际上是一定大于或者等于pivot，所以可以直接nums[i],nums[pivot] = nums[pivot],nums[i],做交换




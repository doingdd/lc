## 704.二分查找
### 用例设计
有效等价类： nums = [-1,0,3,5,9,12], target = 9，输出4

无效等价类： nums = [-1,0,3,5,9,12], target = 2，输出-1

特殊值：nums = [0], target=0,输出0，nums = [1], target=0,输出-1

### 思路及解答

二分查找有两种解法，递归和遍历

#### 1.递归

的思路也是归并，选取列表中的中间值，如果target小于，则递归处理左子序列，如果大于，则递归处理右子序列，等于则返回index

递归的函数需要三个参数：start，end，target，终止递归的条件是start>end

```python
#!/usr/bin/python
def bin_search(nums,target):
    def search(start,end):
        if start > end:
            return -1

        mid = start + (end-start)/2
        if target > nums[mid]:
            start = mid+1
        elif target < nums[mid]:
            end = mid -1
        else:
            return mid

        return search(start,end)

    result = search(0,len(nums)-1)
    return result

case = [([-1,0,3,5,9,12],9),
        ([-1,0,3,5,9,12],2),
        ([0],0),
        ([1],0),
        ([1,3,9],1),
        ([],1)

        ]

for i in case:
    print "case is: ",i
    print "result is: ",bin_search(*i)

```

#### 遍历

遍历的话，就是定义好start和end，然后循环的终止条件是start>end,在循环体中，判断target和nums[mid]的关系，找到相等直接返回，或者一直不相等，跳出循环后返回-1

```python
def bin_search(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)/2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1
```



### 总结

二分查找的中心思路，是不断的修改边界start,end,核心的代码在于三个判断：`targert>nums[mid]/<nums[mid]/==nums[mid]`, 判断后，继续遍历时，注意start和end应该跨过mid，否则会陷入死循环。

另外，计算mid时，使用`left+(right-left)/2`,相比于`tart+end)/2`，可以避免大数溢出


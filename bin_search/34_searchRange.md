# 34. 在排序数组中查找元素的第一个和最后一个位置

## case

```python
case = [
  ([5,7,7,8,8,10],8),
  ([5,7,7,8,8,10],6),
  ([],0),
  ([1,1,1,1],1),
  ([1,1,1,1],0),
  ([1,2,3,4,5,6,6],6),
  ([1,1,2,3,4,5,6,6],1)
]
```



## 思路

题目中的数组是升序，首先想到这是一个二分查找的问题，二分查找可以在logn复杂度内找到target的index，然后要返回该的第一个位置和最后一个位置，相当于从index的位置中心扩散，使用两个指针来维护即可；

本题和剑指53是统一题目，区别在于返回值的不同

```python
def search_range(nums,target): 
  	i,j = -1,-1
    if not nums:
        return [i,j]

    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)/2
        if target == nums[mid]:
            i,j = find_range(0,len(nums)-1,nums,mid)
            break
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1


    return [i,j]

def find_range(left,right,nums,mid):
    i,j = mid,mid
    while i >=left and nums[i] == nums[mid]:
        i -= 1

    while j <= right and nums[j] == nums[mid]:
        j += 1

    return i+1,j-1
```



## 总结

这道题的难点在于，二分找到index的扩散方法，扩散的时候需要考虑一些边界值的细节：

1. 扩散时，当nums[i]  != target时要终止左扩散，当i已经越界要终止扩散，右扩散同理
2. 扩散函数的返回值，由于结束时i或者j相当于多走了一步，所以要返回前一步的i和j




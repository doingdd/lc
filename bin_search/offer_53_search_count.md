# 剑指53. 在排序数组中查找元素出现的次数

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

本题和34题是一个解法，区别是返回值不同

```python
   def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        if not nums:
            return count

        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if target == nums[mid]:
                i,j = find_range(0,len(nums)-1,nums,mid)
                count = j-i+1
                break
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1


        return count

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




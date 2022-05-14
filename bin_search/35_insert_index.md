# 插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

## case

```python
case = [
	([1,3,5,6],2),
  ([1,3,5,6],5),
  ([1,3,5,6],7)
]
```



## 思路

这道题虽然是简单题，但是思路还是有一点难想的，首先确认的是二分查找，但是区别于普通的二分，本题要求是不仅要在target存在的时候找到target的index，在不存在的时候还要找到该插入的位置

1. 这两个隐含的要求，其实可以转化成一个：就是找到数组中第一个`大于等于`target的元素位置，这里一定要重点理解，可以带到本题的三个case中看下，`等于`的情况不用说，主要是`大于`,其实就是插入的位置就是第一个大于target的位置。

2. 而且需要注意的是case 3，存在在数组末尾插入的情况，这时target一定大于数组末尾元素，可以特殊判断，也可以将初始的right设为len，这样随着二分查找的进行，left和right一定会重合在len这个位置
3. 第三点需要注意的是结束循环的条件，不再是left <= right， 而是left < right，为什么呢？因为本题不会返回一个-1，而是一定会返回一个index，如果left和right没相遇之前没有找到答案，那么在相遇的时候，答案一定是left和right本身
4. 区间缩小思路，本题中，由于是要找到第一个大于等于target的元素，所以在判断nums[mid] 和target的关系时，如果nums[mid]< target，那么可以确认nums[left]到nums[mid]之间的元素，也就是mid之前的元素一定都小于target，都不满足，所以可以将left + 1； 如果反之，则可以判断nums[mid] **可能**是要找到的index，但是也不一定是第一个，所以需要right= mid，等待下一轮继续判断

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1
        if nums[-1] < target:
            return len(nums)

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            
        return left 
```

免去处理插入位置在数组末尾的写法，就是将初始值right设定为len：

```python
def insert_index(nums,target):
    l = len(nums)
    left,right = 0,l
    while left < right:
        mid = left + (right-left)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left

for i in case:
    print i,insert_index(*i)
```





## 总结

本题不太像是简单题，感觉很容易翻车，因为它跟常规的二分模板有好几点不一样的地方：

1. 循环终止条件，不再包含==
2. 对插入位置在数组之后的特殊情况的处理
3. left，right指针的缩小条件，不再是left = mid + 1,right = mid -1,而是根据本题条件，要找的是第一个>=target的元素位置，改成了right = mid
4. 最后的返回值，left或者right都行，因为如1所示，循环终止时left和right一定重合

坑很多，多记忆吧
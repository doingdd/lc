# 33.旋转数组

## 用例设计

```python
case = [
  ([4,5,6,7,0,1,2],0),
  ([4,5,6,7,0,1,2],3),
  ([1],0),
  ([],0),
  ([1,2,3,0],1)
       ]
```



## 思路解答

这道题如果没有旋转的条件，那么就是一个普通的二分查找，而加上旋转之后，其核心在于如何处理旋转的特点，其实和普通二分的区别，就在于取了mid之后，如果判断出target在mid左侧还是右侧，其实就判断的逻辑有了一些变化

* 普通的二分查找，需判断target 和nums[mid]的关系
* 本题的二分查找，先判断mid的左子序列和右子序列哪个有序，根据有序的部分，可以得出边界的变化方式，判断左右子序列哪个有序，可以通过判断nums[mid]和左边界的关系，如果nums[mid]>=左边界，那么mid一定是取在了第一个上升序列里，也就是mid左侧的序列，一定是上升的，右侧序列一定是包括了旋转的部分；反之，nums[mid]<左边界，则mid一定是取在了第二个上升序列，也就是旋转的部分上,那么右侧有序；注意这个**左边界**，可以是绝对的左边界nums[0]，也可以是相对的左边界nums[left],这里效果是一样的
* 如果左侧有序，那么如果nums[mid] > target > nums[left]则在左侧寻找，否则右侧；如果右侧有序，且nums[mid]< target < nums[right]则在右侧寻找，否则左侧，同时注意处理边界值

根据上述的思路，可以得到代码：

```python
    if not nums:
        return -1

    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)/2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[0]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[0]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
for i in case:
    print "case is {0},result is {1}".format(i,bin_search(*i))
```

```python
case is ([4, 5, 6, 7, 0, 1, 2], 0),result is 4
case is ([4, 5, 6, 7, 0, 1, 2], 3),result is -1
case is ([1], 0),result is -1
case is ([], 0),result is -1
case is ([1, 2, 3, 0], 1),result is 0
case is ([4, 5, 6, 7, 8, 1, 2, 3], 8),result is 4
```



## 总结

这道题是二分查找的变版，需要有三个点注意：

1. 如合判断左右子序列有序
2. 判断后，如何使用有序的子序列缩小边界，这里连续的两个<是精髓：nums[left] <= target < nums[mid], 它的反条件，也就是else的条件是target < nums[left] or target > nums[mid], 注意记忆这个写法，否则代码会很乱
3. 注意判断时，需要考虑边界值的处理，是左开右闭还是相反，首先第一层循环，就要用<=；还有判断左右子序列有序的时候，要考虑mid值和左边界相等的情况(相等则左子序列为空，也认为左子序列有序)，所以这个等号放在了跟>一起




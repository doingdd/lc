## 冒泡排序

## case

```python
case = [
        [5,4,3,2,1],
        [1,2,3,4],
        [1],
        [],
        [1,2,2,2,3,1]
        ]
```

## 思路

模仿泡泡往水面上浮的感觉，从第一个元素开始往上(后)移动，判断当前元素和下一个元素相比，如果大于则交换，如果小于则继续往后走，双层遍历

```python
def bubble_sort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i,l):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

    return nums

for i in case:
    print i,bubble_sort(i)

```

## 总结

其实不只一种写法，本文的写法就是"从前往后处理每一个元素，将其放到正确的位置"；还有种写法是类似从后往前，每次把"最大"的元素确定在最右侧
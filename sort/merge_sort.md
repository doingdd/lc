# 归并排序

## case

```python
case = [[2,3,3,1],[4,3,2,1,0],[1,2,3],[1],[]]
for i in case:
    print i , merge_sort(i)

```

## 思路

归并排序的核心思路就两个单词：分治和递归

1. 分治. 将数组分成左右两部分，然后将左右两个子数组进行排序，排完之后再执行merge，merge成一个数组
2. 递归. 数组分两h部分之后，每个部分仍然继续分隔，直到只剩一个元素为止，这一过程可以用递归来实现

分治是一种思想，递归是一种编程方式

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    num = len(arr)/2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    arr = merge(left,right)

    return arr

def merge(left,right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result
```



## 总结

归并排序的时间复杂度是O(nlogn),空间复杂度是O(n), 是稳定排序，唯一缺点是需要额外的空间，不是原地排序


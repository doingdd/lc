# 215 数组中第k个最大元素

## case

```
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```

## 思路

1.简单而暴力的思路，就是先排序，再取值，这样的时间复杂度取决于排序算法，也就是快排的O(n*logn)

2.本题的考查基本是堆排序，构建一个k个元素的最小堆，那么堆顶元素即为第k个最大元素，解释一下，小顶堆的特点是：最上面的元素最小，在遍历整个数组时，如果元素大于堆顶，那么进堆，如果小于则不进堆，这样，最小堆里维护的肯定是k个“比较大”的元素，堆顶就恰好是这些“大元素”里最小的那个，也就是“第k个最大元素”

如下是直接调用python的heapq库的解法，已经把构造堆封装好了

```python
   	def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        if not nums:
            return None
        heap = nums[:k]
        heapq.heapify(heap)
        #print( heap)
        for i in nums[k:]:
            if i >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,i)

        return heap[0]
```

如果有余力，可以自己手写一个构造堆的方法

构造堆，主要涉及三个方法：上升，下降和构造，如果再堆末尾添加一个元素，需要用到上升，如果在堆顶删除一个元素并添加一个新元素(或者直接替换)则需要下降，构造就是初始化堆时需要, 本题中其实只用到build和down方法就够了，先build一个k个元素的堆，然后对其余元素遍历，当元素大于堆顶元素时，将堆顶元素替换成该元素，并调用down方法整理堆

```python
def up(arr):
    c_idx = len(arr) - 1
    p_idx = (c_idx - 1)/2
    temp = arr[c_idx]
    while c_idx > 0 and temp < arr[p_idx]:
        arr[c_idx] = arr[p_idx]
        c_idx = p_idx
        p_idx = (p_idx - 1)/2

    arr[c_idx] = temp

def down(arr,p_idx):
    c_idx = 2*p_idx + 1
    temp = arr[p_idx]
    l = len(arr)
    while c_idx < l:
        if c_idx + 1 < l and arr[c_idx+1] < arr[c_idx]:
            c_idx += 1

        if temp <= arr[c_idx]:
            break

        arr[p_idx] = arr[c_idx]
        p_idx = c_idx
        c_idx = 2*c_idx + 1

    arr[p_idx] = temp

def build(arr):
    i = (len(arr) - 1 - 1)/2
    while i >= 0:
        down(arr,i)
        i -= 1

    return arr

```



## 总结

本题的考查就是堆的使用，能理解最小堆的含义(二叉堆的一种)，还有它的特点：

1.堆顶元素最小

2.父节点一定小于其子节点

构建的思路：

1.对一个数组来说，如果把它定义成一个二叉树，那么从i=0开始，2*i+1就是左子节点，2\*i+2就是右子节点，构建堆的方法，就是把每个节点元素执行一次down操作，让每个父节点都小于其子节点，这里采用从后向前的方式:len(arr)-1就是最后一个节点k，从它的父节点开始down，就是(k-1)/2，也就是(len(arr) - 1 - 1)/2

2.down的过程，就是判断待处理的元素是否小于两个子节点中最小的那一个，如果是，那么就停止down，整理完成；如果否，那么就继续下沉，下沉的方式就是将子节点上浮一位，同时将子节点的位置，替换成待处理元素(上述的方法省略了这一步，只在最后结束down的时候替换一次，这里需要思考理解)
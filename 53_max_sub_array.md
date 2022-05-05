# 53.最大子数组和



## case

```python
case = [
  [-2,1,-3,4,-1,2,1,-5,4],
  [],
  [-1],
  [0],
  [4,5,-1,7,8]
]
```



## 思路

这道题虽然是个简单题，思路还是比较奇特的，而且不太好记忆，核心的思路需要理解：

当遍历到当前元素时，如果前面的子数组和为正，那么取前面和+当前值，与前面和的最大值，作为临时的子数组最大

如果前面的子数组和为负，那么取当前值作为临时最大值

整理上述两个条件，临时最大为max((tmp_sum+i),i), 这里需要重点记忆

然后再维护一个全局的最大值，并实时更新即可

```python
def get_max(nums):
    if not nums:
        return 0

    _sum = _max = nums[0]
    for i in range(1,len(nums)):
        _sum = max(nums[i],nums[i] + _sum)
        _max = max(_max,_sum)

    return _max


nums = [-2,1,-3,4,-1,2,1,-5,4]
print nums,get_max(nums)
nums = [1,1,1]
print nums,get_max(nums)
nums = [1]
print nums,get_max(nums)
nums = []
print nums,get_max(nums)
nums = [2,-1,3]
print nums,get_max(nums)
```



## 总结

这道题也是个记忆体，记住了临时最大值的取法就行了


# 560. 和为k的子数组

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 *该数组中和为 `k` 的子数组的个数* 。

## case

```python
case = [
        ([1,1,1],1),
        ([1,1,1],2),
        ([1,2,3],3),
        ([1,2,3],4),
        ([5,1,4,-1,1,2,3],5),
        ([],1),
        ([1],1),
        ([2],1)
        ]
for i in case:
    print i,sub_array_num(*i)
```



## 思路

连续子数组的问题，可以考虑是不是前缀和

本题的核心思路：两个位置的前缀和相减，如果等于k，那么可以得到这两个位置组成的子数组和为k，即presum[j] - presum[i] == k

那么sum(nums[i:j+1])这时肯定等于k

对上述等式做一个变幻，即presum[j] - k，这时得到的一个值，如果能和某一个presum[i]相等，那么则认为找到了一个符合条件的数组，维护一个全局的变量count，这时将count累加即可

```python
def sub_array_num(nums,k):
    pre_sum = {0:1}
    cur_sum = 0
    count = 0
    for i in nums:
        cur_sum += i
        if (cur_sum-k) in pre_sum:
            count += pre_sum[cur_sum-k]

        pre_sum[cur_sum] = pre_sum.get(cur_sum,0) + 1

    return count
```



## 总结

本题如果想到了前缀和，还可能答不出来，原因是没有想清楚前缀和究竟要存什么

1. 前缀和pre_sum，key为前缀和，value为这个前缀和前面出现过的次数
2. 每次遍历一个元素，计算当前的前缀和，并且将这个前缀和出现过的次数加1
3. 同时，判断如果当前(前缀和-k)是不是已经出现过了(出现过则一定会被记录在pre_sum字典里)，如果出现过，那么相当于找了一个答案，此时将count 更新，注意这里不是简单的+1，而是说要加上出现过的真实次数，这个次数就是pre_sum的value
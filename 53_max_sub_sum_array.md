## 53.最大子序和

### 用例设计
* 有效等价类： [-2,1,-3,4,-1,2,1,-5,4]：连续子数组 [4,-1,2,1] 的和最大，为 6   
* 有效等价类：[1,2,3,-1]
* 无效等价类：[]
* 特殊值： [1],[0],[-1],[-1000],

### 思路及解答
这道题虽然属于简单难度，但是很容易陷入思维误区，如果想求出最大的和，第一印象想到的一般就是遍历。  

遍历的过程中，如果都是正数很好办，直接加上当前值就可以了，但是如果遇到负数呢？

不加负数的话：后面是否会遇到更大的正数，加上当前的负数，再加上之前的正数之后，构成最大和？

或者说加上负数，那后面万一全是负数，岂不是应该仅保留正数的子序列才对？

上面的思路是多次做这道题时第一个会蹦出来的疑问，如果顺着这个疑问继续往下想，很容易陷入误区无法解答，根据这道题的官方解答，提炼出一个思路，帮助记忆：  

上面的思路误区在于，过于关注`以后`,而这道题的正解，是要只关注`当下`,也就是说，当前以及之前遍历过的子序和，是否有价值，需要保留？  

注意这个思路很重要，即通过对比当前的值和(之前的子序和+当前值)的大小，得出新的子序和是当前值(抛弃之前的子序和)还是之前的子序和+当前值(既保留前面的子序和，又保留和当前值)，也就是说，当遍历的时候，永远要保证有一个局部最大值，这个最大值可能是前面的子序和一路累加过来的，也可能是抛弃了前面的和，仅保留了一个当前值。  

```python
def get_max(nums):
    if not nums:
        return 0

    _sum = _max = nums[0]
    for i in nums[1:]:
        _sum = max(i,i+_sum)
        _max = max(_sum,_max)

    return _max
```

### 总结
这道题的代码非常简单，但是思路有个弯，如果绕不出来，就很难解答，还是比较坑的，需要多多回顾。  

这道题的核心在于：max(当前值,前面的子序和+当前值),隐含的思想就是，如果前面的子序和+当前值< 当前值，那就把当前值作为局部最优，相当于放弃掉前面的子序和；如果>当前值，那么就带上当前值；注意，前面的子序和不一定是正数，也可能是负数，如果是负数，果断扔掉  

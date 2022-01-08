# 39.组合总和



## 用例

```python
case = [
  [[2,3,6,7],7],
  [[2,3,5],8],
  [[2],1],
  [[1],1],
  [[1],2]
]
```



## 思路

这是一道回溯问题，由于每个元素的使用次数不限，需要想清楚如何穷举所有可能，按照人的思路，应该是从前到后的遍历，然后在遍历的过程中，再继续"往深"遍历，比如第一个case，先拿到一个元素2，用一个临时变量temp_sum存当前和,如果当前和< target,则继续往深走，再拿一次2，再拿两次2，知道拿了四次2，发现temp_sum> target，这一次则终止，重新回到3次2的时候，再拿3：3*2+3>7，终止；再回到两次2的时候，拿3，得到了=target，记录这个组合后继续遍历

在实现中，使用循环+递归的方法，递归的终止条件就是tmp_sum=target(正常终止)，tmp_sum>target(异常终止), 递归的参数需要有：当前已经遍历到的组合(用来记录)， 以及target-当前值(这样可以通过判断target是否=0来确定是否正常终止，<0则异常终止)

```python
def combine_sum(candidates,target):
    result = []
    passed = []
    def find(target,passed,candidate):
        if target == 0:
            result.append(passed)
        if target < 0:
            return
        for i,v in enumerate(candidate):
            find(target-v,passed+[v],candidate[i:])

    find(target,passed,candidates)

    return result

for i in case:
    print "case is {0}, result is {1}".format(i,combine_sum(*i))

```



## 总结

这道题比较难理解的地方在于，为什么再递归里要套循环，以及递归函数这几个参数的定义是为什么

这设计回溯问题的基本思路，及每走一步时，当前这个步骤，它的历史路径是什么，它的target是什么，它的可选路径又是什么

想清楚这三个问题，就想清楚了回溯问题的思路

* 它的历史路径，就是它已经走过的元素，即passed，
* passed的和与target相等时终止，或者passed的和超出了target终止；即本题中每次递归，都将target-v，其实就是在反向的计算passed的和是否已经满足条件
* 当前可已选择的路径，即candidate[i:],这里为什么不是candidate本身，要从i这个index开始呢？因为回溯问题其实是两层遍历，一层是"水平遍历"，一层是"深度遍历"，在深度遍历的时候，当前的可选路径，其实是不变的，因为i没变；在某一个点"深度遍历"完成后，才开始水平移动，这时已经不用考虑它前面的元素了，因为前面的元素的所有组合已经在前一个水平遍历+深度遍历时完成了，当然，这一逻辑的基础，是本题不考虑顺序的前提下，如果考虑答案的顺序，比如[2,3,3]和[3,3,2]是两个不同的答案的话，那就不是从i开始了，应该每次都从0开始
* 本题解的时间复杂度应该是O(n^2)


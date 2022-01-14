case = [
    [0,1,2,3,4,6],
    [0,2,3,4],
    [0,1,2,3,5]
        ]
def find_n(nums):
    if not nums:
        return ''

    return (0+nums[-1])*(nums[-1]+1)//2 - sum(nums)

def bin_find_n(nums):
    if not nums:
        return ''

    l = len(nums)
    left,right = 0,l-1
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid

    return left

for i in case:
    print(i)
    print(bin_find_n(i))

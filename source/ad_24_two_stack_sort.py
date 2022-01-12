case = [
        [4,3,2,1],
        [],
        [1,2,3],
        [1,1,1],
        [1],
        [4,2,1,3,4,5],
        [1,2,3,4,3,2,1]
    ]

def stack_sort(stack):
    tmp_stack = []
    while stack:
        v = stack.pop()
        while tmp_stack and tmp_stack[-1] > v:
            tmp_v = tmp_stack.pop()
            stack.append(tmp_v)

        tmp_stack.append(v)

    return tmp_stack

for i in case:
    print(i)
    print(stack_sort(i))

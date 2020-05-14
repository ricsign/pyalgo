def solve(train_num,queue):
    # queue is left in right out
    branch = []  # right out right in stack
    last_enter = 0
    while True:
        if last_enter == train_num:
            ret_list.append('Y')
            return
        elif branch and branch[-1] == last_enter + 1:
            last_enter += 1
            branch.pop()
        elif queue:
            if queue[-1] == last_enter + 1:
                last_enter += 1
                queue.pop()
            else:
                branch.append(queue.pop())
        elif (not queue) and branch:
            if branch[-1] != last_enter + 1:
                ret_list.append('N')
                return


ret_list = []
test_num = int(input())
for _ in range(test_num):
    t = int(input())
    q = [int(input()) for _ in range(t)]
    solve(t,q)
for i in ret_list:
    print(i)


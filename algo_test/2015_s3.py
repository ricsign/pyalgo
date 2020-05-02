gates_num = int(input().strip())
plane_num = int(input().strip())
plane_queue = []
gates_set = set(i+1 for i in range(gates_num))
flag = True
count = 0

for _ in range(plane_num):
    plane_queue.append(int(input().strip()))

while flag and plane_queue:
    cur_plane = plane_queue.pop(0)
    pos = cur_plane
    while True:
        if pos in gates_set:
            count += 1
            gates_set.discard(pos)
            break
        elif pos > 0:
            pos -= 1
            continue
        else:
            flag = False
            break

print(count)







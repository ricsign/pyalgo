input_set = [input().split() for _ in range(3)]
output_set = []
cur_flag=[False,False,False] #False if not x

for handle in input_set:
    cur_x_count = 0
    for i in range(len(handle)):
        if handle[i] == 'X':
            cur_x_count += 1
            cur_flag[i] = True

    if cur_x_count == 0:
        output_set.append(handle)

    elif cur_x_count == 1:
        x_pos = cur_flag.index(True)
        if x_pos == 0:
            differ = int(handle[2])-int(handle[1])
            output_set.append([str(int(handle[1])-differ),handle[1],handle[2]])
        elif x_pos == 1:
            differ = (int(handle[2])-int(handle[0]))//2
            output_set.append([handle[0], str(int(handle[0]) + differ), handle[2]])
        else:
            differ = int(handle[1]) - int(handle[0])
            output_set.append([handle[0],handle[1],str(int(handle[1])+ differ)])


    elif cur_x_count == 2:
        not_x_pos = cur_flag.index(False)
        output_set.append([handle[not_x_pos] for _ in range(3)])


    else:
        output_set.append(['1','1','1'])

    cur_flag = [False, False, False]


print(output_set)





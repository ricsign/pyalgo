# Name: Richard Shuai
# Grade: 10
# Teacher: Mr.Schellenberg
# ACSL 3
# WMCI


table = [[0 for _ in range(4)] for _ in range(4)]
del_dictionary = {'~A':(0,1),'A':(2,3),'~B':(0,1),'B':(2,3),'~C':(1,2),'C':(0,3),'~D':(1,2),'D':(0,3)}
hexa_lookup = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
ret_vals = []

def read_buffer_load(buffer):
    fill_rows = {0, 1, 2, 3}
    fill_cols = {0, 1, 2, 3}
    not_flag = False
    for curr in buffer:
        if curr == 'A' or curr == 'C':  # delete each columns using demorgan
            if not_flag:
                curr = '~' + curr
                not_flag = False
            fill_cols.discard(del_dictionary[curr][0])
            fill_cols.discard(del_dictionary[curr][1])
        elif curr == 'B' or curr == 'D':  # delete each columns using demorgan
            if not_flag:
                curr = '~' + curr
                not_flag = False
            fill_rows.discard(del_dictionary[curr][0])
            fill_rows.discard(del_dictionary[curr][1])
        if curr == '~':
            not_flag = True

    # start to add the grid
    for i in fill_rows:
        for j in fill_cols:
            table[i][j] = 1

def converter():
    ret = ''
    curr_sum = 0
    for x in range(4):
        for y in range(4):
            curr_sum += (2**(3-y))*table[x][y]
        if curr_sum > 9:
            ret += hexa_lookup[curr_sum]
        else:
            ret += str(curr_sum)
        curr_sum = 0
    return ret


def veitch(veitch_str):
    global table
    buffer = ''
    if veitch_str == '':
        return '0000'
    for char in veitch_str:
        if char == '+':
            read_buffer_load(buffer)
            # clear buffer, another iteration
            buffer = ''
            continue
        buffer += char

    # handle the last adding or no addition sign
    read_buffer_load(buffer)
    # convert table to hexadecimal
    ret = converter()
    # recycle all resources
    table = [[0 for _ in range(4)] for _ in range(4)]
    return ret

for _ in range(5):
    ret_vals.append(veitch(input().strip()))
for i in ret_vals:
    print(i)






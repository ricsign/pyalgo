dictionary = {}
index_of_dict = {}
visited = []
for i in range(1,4):
    a1,a2 = input().split()
    dictionary[a1] = a2
    index_of_dict[a1] = i
line4 = input().split()
total_steps,initial_state,final_state = int(line4[0]),line4[1],line4[2]


def rule_of_three(current_state,step_left):
    if current_state == final_state and step_left == 0:
        return visited
    elif step_left > 0:
        for pre in range(len(current_state)+1):
            for post in range(pre+1,len(current_state)+1):
                if current_state[pre:post] in dictionary:
                    rule_used = index_of_dict[current_state[pre:post]]
                    new_current_state = current_state[:pre] + dictionary[current_state[pre:post]] + current_state[post:]
                    step_left -= 1
                    visited.append([rule_used,pre+1,new_current_state])
                    ret = rule_of_three(new_current_state,step_left)
                    if ret: return ret
                    visited.pop()
                    step_left += 1


rule_of_three(initial_state,total_steps)
for i in visited:
    for j in i:
        print(j,end=' ')
    print()

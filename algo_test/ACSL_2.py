same_list = []
alphebet_tab = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphebet_table = alphebet_tab[::-1]


def sameness(s1,s2):
    length = len(s1) if len(s2) > len(s1) else len(s2)
    global same_list
    for i in range(length):
        if s1[i] == s2[i]:
            same_list.append(i)
    count = 0
    for i in same_list:
        s1 = s1[:i-count] + s1[i+1-count:]
        s2 = s2[:i-count] + s2[i+1-count:]
        count += 1

    new_length_s1 = len(s1)
    new_length_s2 = len(s2)
    cursor = 0

    while True:
        if cursor >= new_length_s1 or cursor >= new_length_s2:
            break
        check = 0
        while True:
            if check >= new_length_s1 or check >= new_length_s2:
                break
            if s1[check] == s2[check]:
                s1 = s1[:check] + s1[check+1:]
                s2 = s2[:check] + s2[check + 1:]
                check = 0
                new_length_s1 -= 1
                new_length_s2 -= 1
            check += 1
        if cursor+1 < len(s2):
            if s2[cursor+1] == s1[cursor]:
                s2 = s2[:cursor] + s2[cursor+2:]
                s1 = s1[:cursor] + s1[cursor+1:]
                new_length_s2 -= 2
                new_length_s1 -= 1
                cursor = 0
                continue
        if cursor+1 < len(s1):
            if s1[cursor+1] == s2[cursor]:
                s1 = s1[:cursor] + s1[cursor+2:]
                s2 = s2[:cursor] + s2[cursor + 1:]
                new_length_s1 -= 2
                new_length_s2 -= 1
                cursor = 0
                continue
        cursor += 1

    update_shorter_length = len(s1) if len(s2) > len(s1) else len(s2)
    sum = len(s2) - len(s1) if update_shorter_length == len(s1) else len(s1) - len(s2)


    for i in range(update_shorter_length):
        a = (alphebet_table.index(s2[i]) - alphebet_table.index(s1[i]))
        sum += a
    print(sum)
    same_list = []

a = []
for _ in range(5):
    a.append(input().split())

for inputs in a:
    sameness(inputs[0],inputs[1])


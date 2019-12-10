def shell_sort(l):
    d = len(l)// 2
    while d >= 1:
        for i in range(0,len(l)-d):
            if l[i+d] < l[i]:
                l[i],l[i+d] = l[i+d],l[i]
        d = d // 2
    return l

print(shell_sort([4,3,1,0,-1,3,2]))
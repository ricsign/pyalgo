def rule_of_three(src,dest,dict,path,time,flag):
    if src == dest:
        path.append('*')
        return path
    for prefix in range(len(src)):
        for affix in range(prefix+1,len(src)+1):
            if src[prefix:affix] in dict.keys():
                print(path)
                src = src[:prefix]+dict[src[prefix:affix]]+src[affix:]
                path.append(src)
                rule_of_three(src,dest,dict,path,time-1,flag)
                if path[-1] == '*':
                    return path
                if time <= 0:
                path.pop()
                time += 1
                src = path[-1]
                break



record = ['AA']
dict = {'AA':'AB','AB':'BB','B':'AA'}
print(rule_of_three('AA','AAAAA',dict,record,4,0))

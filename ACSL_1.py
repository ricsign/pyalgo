def handle(n,p):
    ret = ''
    special_dig = int(n[0-p])
    for i in range(len(n)):
        current = int(n[i])
        if i == len(n)-p:
            ret += str(special_dig % 10)
        elif i < len(n)-p:
            ret += str((current + special_dig) % 10)
        else:
            ret += str(abs((current - special_dig)) % 10)
    return ret

#Input method 1
# a = []
# for _ in range(5):
#     a.append(input().split())
#
# for inputs in range(5):
#     print(str(inputs+1) + '. ' + handle(a[inputs][0], int(a[inputs][1])))


#Input method 2
# b = input().split()
# print(handle(b[0],int(b[1])))




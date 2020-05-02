order = input()
h,v = 0,0
for i in order:
    if i == "V":
        v += 1
    elif i == "H":
        h += 1
if v % 2 == 0 and h % 2 == 0:
    print("1 2")
    print("3 4")
if v % 2 == 1 and h % 2 == 0:
    print("2 1")
    print("4 3")
if v % 2 == 0 and h % 2 == 1:
    print("3 4")
    print("1 2")
if v % 2 == 1 and h % 2 == 1:
    print("4 3")
    print("2 1")
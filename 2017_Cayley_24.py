"""
 @desc:
 @author: Richard
 @contact: 1955283190@gmail.com
 @site: www.Richard.com
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """
count = 0


def a(x, y, z):
    global count
    if x == y == z == 0:
        count += 1
        return
    if z > 0:
        a(x, y + 1, z - 1)
    if y > 0:
        a(x + 1, y - 1, z)
    if x > 0:
        a(x - 1, y, z)


a(0, 0, 3)
print(count)

"""
 @desc:
 @author: Richard
 @contact: 1955283190@gmail.com
 @site: www.Richard.com
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """

# Non-recursive solution
def wordsearch(target,map):
    direction = {"down":(1,0),"up":(-1,0),"right":(0,1),"left":(0,-1),"rightdown":(1,1),"rightup":(-1,1),"leftup":(-1,-1),"leftdown":(1,-1)}
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == target[0]:
                if len(target) == 1:
                    return [(row,col),'any_direction']
                for dir_name,dir_co in direction.items():
                    x = row+dir_co[0]
                    y = col+dir_co[1]
                    if 0 <= x < len(map) and 0 <= y < len(map[row]):
                        if map[x][y] == target[1]:
                            cur = target[0] + map[x][y]
                            count = 2
                            while True:
                                if cur == target:
                                    return [(row,col),dir_name]
                                x += dir_co[0]
                                y += dir_co[1]
                                if 0 <= x < len(map) and 0 <= y < len(map[row]):
                                    if map[x][y] == target[count]:
                                        cur += map[x][y]
                                        count += 1
                                    else:
                                        break
                                else:
                                    break


print(wordsearch("shore",["ebcda","mrvst","arolj","npihc","etsms"]))  # [(4, 4), 'leftup']

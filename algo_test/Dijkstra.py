"""
 @desc:
 @author: Richard
 @contact: 1955283190@gmail.com
 @site: www.Richard.com
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """

# how to use
# let user input the pathes and return the shortest path from node 0, [initital,end,cost]
# for example: one data [0,2,3] means it takes 3 unit to go from node 0 to node 2
# for the graph it's a directed graph


class Dij:
    # n: number of nodes, we'll asssume user's inputs are valid
    def __init__(self,n,origin,pathes):
        self.__n = n
        self.__pathes = pathes
        self.__origin = origin
        self.__set_up()

    # public methods
    def show_map(self):
        if self.__map:
            for i in self.__map:
                for j in i:
                    print(j,end= " ")
                print('\n')

    def show_distance(self):
        if self.__distance:
            for i in self.__distance:
                print(i,end= " ")

    def solve(self):
        # flag is true if every node can be reached, false otherwise
        flag = True
        while True:
            # every node has searched
            if not self.__not_been:
                break
            # find minimum from not_been set
            min_val,min_node = float("inf"),-1
            for i in self.__not_been:
                if min_val > self.__distance[i]:
                    min_val = self.__distance[i]
                    min_node = i
            # add to set
            if min_node == -1:
                # fail to find the minimum, some nodes cannot be reached
                flag = False
                break
            self.__not_been.remove(min_node)
            self.__been.add(min_node)
            # update distance list
            for i in range(self.__n):
                if not i == min_node:
                    if self.__distance[i] > min_val+self.__map[min_node][i]:
                        self.__distance[i] = min_val+self.__map[min_node][i]
                        self.__pre[i] = min_node
        self.__display(flag)
        return flag

    # private methods
    def __display(self,flag):
        for i in range(self.__n):
            if not self.__distance[i] == float("inf"):
                print("The shortest length to node {0}: {1}, with the previous node {2}".format(str(i),str(self.__distance[i]),str(self.__pre[i])))
            else:
                print("Sorry, we can't find a way to " + str(i))

    def __set_up(self):
        self.__map =  [[float('inf') for _ in range(self.__n)] for _ in range(self.__n)]
        for i in self.__pathes:
            self.__map[i[0]][i[1]] = i[2]
        # initiating distance array with respect to origin node
        self.__distance = [float("inf") for _ in range(self.__n)]
        self.__distance[self.__origin] = 0
        for u in range(self.__n):
            if not u == self.__origin:
                self.__distance[u] = self.__map[self.__origin][u]
        # initiating been and not_been set
        self.__been = {self.__origin}
        self.__not_been = set()
        for i in range(self.__n):
            if i != self.__origin:
                self.__not_been.add(i)
        # initiating pre list
        self.__pre = [self.__origin for _ in range(self.__n)]


if __name__ == "__main__":
    d = Dij(5,4,[[0,4,12],[4,0,8],[0,1,16],[1,0,29],[4,1,32],[1,3,13],[3,1,27],[0,2,15],[2,0,21],[2,3,7],[3,2,19]])
    d.show_map()
    print('------------------')
    d.solve()



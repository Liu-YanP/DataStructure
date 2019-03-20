#图的广度优先算法

graph = {
'A':['B','C'],
'B':['A','C','D'],
'C':['A','B','D','E'],
'D':['B','C','E','F'],
'E':['C','D'],
'F':['F']
}
#广度优先算法
def BFS(graph,start_node):
    '''
    算法思路：建立一个队列，首先将起始点放入队列。若队列不为空，每次
    取出队首的点，然后将取出点的相邻节点（不重复的）放入队列。直达队列
    为空 '''
    queue = []
    queue.append(start_node)
    seen = set()  #放入过队列的元素
    seen.add(start_node)
    while len(queue)>0:  #队列不为零
        vertex = queue.pop(0) #弹出先进去的元素
        node = graph[vertex]  
        for w in node:    #将弹出元素的相邻节点放入队尾
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


if __name__ == '__main__':
    BFS(graph,'E')

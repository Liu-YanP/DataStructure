graph = {
'A':['B','C'],
'B':['A','C','D'],
'C':['A','B','D','E'],
'D':['B','C','E','F'],
'E':['C','D'],
'F':['F']
}
#广度优先算法
def DFS(graph,start_node):
    '''
    算法思路：建立一个堆栈，首先将起始点放入堆栈。若堆栈不为空，每次
    取出栈顶的点，然后将取出点的相邻节点（不重复的）放入堆栈。直达堆栈
    为空 '''
    stack = []
    stack.append(start_node)
    seen = set()
    seen.add(start_node)
    parent = {#每个节点的父节点
    start_node:None,
    }
    while len(stack)>0:
        vertex = stack.pop()
        node = graph[vertex]
        for w in node:
            if w not in seen:
                stack.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent

if __name__ == '__main__':
    parent = DFS(graph,'E')
    for key,value in parent.items():
        print(key,value)

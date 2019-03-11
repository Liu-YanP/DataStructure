import heapq
import math
graph = {
'A':{'B':5,'C':1},
'B':{'A':5,'C':2,'D':1},
'C':{'A':1,'B':2,'D':4,'E':8},
'D':{'B':1,'C':4,'E':3,'F':6},
'E':{'C':8,'D':3},
'F':{'D':6}
}

def distance_init(graph,s):
    distance = {s:0}
    for w in graph:
        if w != s:
            distance[w] = math.inf
    return distance

def dijikstra(graph,s):
    pqueue = []
    heapq.heappush(pqueue,(0,s))
    seen = set()
    parent = {s:None}
    distance = distance_init(graph,s)

    while len(pqueue)>0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist+graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w] = vertex
                    distance[w] = dist+graph[vertex][w]
    return parent,distance

if __name__ == '__main__':
    parent,distance = dijikstra(graph,'A')
    print(parent)
    print(distance)
    #查找最短路径
    node = 'E'             #终点E
    while node != 'A':       #起点为B
        node = parent[node]
        print(node)   #输出最短路径（倒序）



from collections import deque

def bfs(graph, start):
    visit= set()  
    q= deque(start)  
    visit.add(start)

    while q:
        node = q.popleft()
        print(node, end=' ')  

        for x in graph[node]:
            if x not in visit:
                visit.add(x)
                q.append(x)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')



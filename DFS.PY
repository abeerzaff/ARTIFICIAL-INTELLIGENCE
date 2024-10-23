
def dfs(g, n, visit=None):
    if visit is None:
        visit = set()  

    visit.add(n)
    print(n, end=' ')  
    for x in g[n]:
        if x not in visit:
            dfs(g, x, visit)


g = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


dfs(g, 'A')

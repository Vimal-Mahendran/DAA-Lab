import sys

def tsp(graph, start):
    n = len(graph)
    all_points = set(range(n))
    memo = {(frozenset([start]), start): 0}
    
    def dp(visited, last):
        if len(visited) == n:
            return graph[last][start]
        
        if (frozenset(visited), last) in memo:
            return memo[(frozenset(visited), last)]
        
        res = sys.maxsize
        for point in all_points - set(visited):
            res = min(res, graph[last][point] + dp(visited + [point], point))
        
        memo[(frozenset(visited), last)] = res
        return res
    
    return dp([start], start)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_point = 0
print(tsp(graph, start_point))

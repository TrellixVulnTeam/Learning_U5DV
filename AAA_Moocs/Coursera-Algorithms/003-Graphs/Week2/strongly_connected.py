#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(nodes, node):
    node["visited"] = True
    for neighbour_index in node["neighbours"]:
        neighbour = nodes[neighbour_index]
        if not neighbour["visited"]:
            dfs(nodes, neighbour)

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    nodes = list(({ "visited": False, "neighbours": neighbours, "index": index } for index, neighbours in enumerate(adj)))
    for node in nodes:
        if not node["visited"]:
            result += 1
            dfs(nodes, node)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
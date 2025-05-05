from collections import deque
import heapq

def shortest_shortest_path(graph, source):
    result = {v: (float('inf'), float('inf')) for v in graph}
    result[source] = (0, 0)
    h = [(0, 0, source)]
    while h:
        weight, edges, node = heapq.heappop(h)
        for neighbor, w in graph[node]:
            new_weight = weight + w
            new_edges = edges + 1
            if (new_weight < result[neighbor][0] or
               (new_weight == result[neighbor][0] and new_edges < result[neighbor][1])):
                result[neighbor] = (new_weight, new_edges)
                heapq.heappush(h, (new_weight, new_edges, neighbor))
    return result


def bfs_path(graph, source):
    result = {}
    v = set([source])
    que = deque([source])
    while que:
        node = que.popleft()
        for neighbor in graph[node]:
            if neighbor not in v:
                v.add(neighbor)
                result[neighbor] = node
                que.append(neighbor)
    return result

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def get_path(parents, destination):
    p = []
    while destination in parents:
        p.append(parents[destination])
        destination = parents[destination]
    return ''.join(reversed(p))

print(get_path(bfs_path(get_sample_graph(), 's'), 'd'))


from typing import List, Tuple

def solve(cases: List):
    output = []
    for test_case in cases:
        n, e, t, _, passages = test_case
        inv_passages = inverse_adjacency(n, passages)
        min_distances = _dijkstra(n, e, inv_passages)
        num_mice = num_mice_exit(min_distances, t)
        output.append(f"{num_mice}")
    output = "\n\n".join(output)
    print(output)

def _dijkstra(n: int, e: int, edges: List[Tuple[int]]):
    done = [False]*(n+1)
    done[e] = True
    min_distances = [-1]*(n+1)
    min_distances[e] = 0
    curr_done = [e]
    for _ in range(n):
        min_weight = float("Inf")
        min_from_node = None
        min_to_node = None
        for from_node in curr_done:
            for to_node, weight in edges[from_node]:
                if done[to_node]:
                    continue
                if weight < min_weight:
                    min_weight = weight
                    min_from_node = from_node
                    min_to_node = to_node
        if min_to_node is None:
            break
        done[min_to_node] = True
        min_distances[min_to_node] = min_distances[min_from_node] + min_weight
        curr_done.append(min_to_node)
    return min_distances

def inverse_adjacency(num_nodes: int, edges: List[Tuple[int]]):
    inv_adj = [[] for _ in range(num_nodes+1)]
    for (from_node, to_node, weight) in edges:
        inv_adj[to_node].append((from_node, weight))
    return inv_adj

def num_mice_exit(min_distances, threshold):
    count = 0
    for dist in min_distances:
        if 0 <= dist <= threshold:
            count += 1
    return count
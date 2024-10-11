# Resources: 0.963s, 60.33 MB
# Maximum single-case runtime: 0.077s
# Final score: 140/140 (10.0/10 points)

from typing import List

def solve(n: int, m: int, translations: List[List[int]]):
    costs = [0 for _ in range(n+1)] # each node in a tree comes from only one edge 
        # (each language have one cost from only one language)

    # BFS
    visited = [False]*(n+1) # English
    visited[0] = True
    last_visited = set([0])
    while True:
        next_to_visit = set()
        for from_lang in last_visited:
            new_positions = translations[from_lang]
            for to_lang, cost in new_positions:
                add_position_and_cost(costs, visited, next_to_visit, to_lang, cost)
                                          
        if len(next_to_visit) == 0:
            break
        last_visited = next_to_visit
        for lang in last_visited:
            visited[lang] = True
    if all(visited):
        print(sum(costs))
    else:
        print("Impossible")

def add_position_and_cost(costs, visited, next_to_visit, to_lang, cost):
    if not visited[to_lang]:
        if to_lang not in next_to_visit:
            costs[to_lang] = cost
            next_to_visit.add(to_lang)                        
        else:
            if cost < costs[to_lang]:
                costs[to_lang] = cost
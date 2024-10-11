# Resources: 0.963s, 60.33 MB
# Maximum single-case runtime: 0.077s
# Final score: 140/140 (10.0/10 points)

from typing import Dict, List

def solve(n: int, m: int, translations: Dict[int, List[int]]):
    costs = [0 for _ in range(n+1)] # each node in a tree comes from only one edge 
        # (each language have one cost from only one language)

    # BFS
    visited = [False]*(n+1) # English
    visited[0] = True
    curr_visited = [0]
    while True:
        next_to_visit = []
        for from_lang in curr_visited:
            to_lang_list = translations[from_lang]
            for to_lang, cost in to_lang_list:
                if not visited[to_lang]:
                    if to_lang not in next_to_visit:
                        costs[to_lang] = cost
                        next_to_visit.append(to_lang)                        
                    else:
                        if cost < costs[to_lang]:
                            costs[to_lang] = cost
                                          
        if len(next_to_visit) == 0:
            break
        curr_visited = next_to_visit
        for lang in curr_visited:
            visited[lang] = True
    if all(visited):
        print(sum(costs))
    else:
        print("Impossible")
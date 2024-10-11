from typing import List

def solve(n: int, m: int, translations: List[List[int]]):
    costs = [0 for _ in range(n+1)] # each node in a tree comes from only one edge 
        # (each language have one cost from only one language)

    # BFS
    min_moves = [-1]*(n+1) # English
    min_moves[0] = 0
    curr_positions = set([0])
    while True:
        new_positions = set()
        for from_lang in curr_positions:
            new_positions = translations[from_lang]
            for to_lang, cost in new_positions:
                add_position_and_cost(costs, min_moves, new_positions, to_lang, cost)
                                          
        if len(new_positions) == 0:
            break
        curr_positions = new_positions
        for lang in curr_positions:
            min_moves[lang] = True
    if all(min_moves):
        print(sum(costs))
    else:
        print("Impossible")

def add_position_and_cost(costs, min_moves, next_to_visit, to_lang, cost):
    if min_moves[to_lang] == -1:
        if to_lang not in next_to_visit:
            min_moves[to_lang] = 1
            costs[to_lang] = cost
            next_to_visit.add(to_lang)                  
        else:
            if cost < costs[to_lang]:
                min_moves[to_lang] += 1
                costs[to_lang] = cost
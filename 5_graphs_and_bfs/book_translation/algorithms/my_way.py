from typing import Dict, List

def solve(n: int, m: int, translations: Dict[int, List[int]]):
    lang_cost_list = [0 for i in range(n+1)]
    acc_cost = 0

    # BFS
    visited = [0] # English
    curr_visited = [0]
    while True:
        next_to_visit = []
        for from_lang in curr_visited:
            to_lang_list = translations[from_lang]
            for to_lang, cost in to_lang_list:
                if to_lang not in visited:
                    if to_lang not in next_to_visit:
                        lang_cost_list[to_lang] =  lang_cost_list[from_lang] + cost
                        acc_cost += cost
                    else:
                        if lang_cost_list[from_lang] + cost < lang_cost_list[to_lang]:
                            new_cost = lang_cost_list[from_lang] + cost
                            acc_cost -= (lang_cost_list[to_lang] - new_cost)
                            lang_cost_list[to_lang] = new_cost
                        
                    next_to_visit.append(to_lang)
        if len(next_to_visit) == 0:
            break
        curr_visited = next_to_visit
        visited.extend(curr_visited)
    # print(lang_cost_list)
    # print(f"Accumulated cost: {acc_cost}")
    print(acc_cost)
    # print(f"Reached languages number: {len(visited)-1}") # WRONG!
    # print(visited)
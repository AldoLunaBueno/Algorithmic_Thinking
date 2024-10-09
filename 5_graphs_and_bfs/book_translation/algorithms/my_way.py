from typing import Dict, List

def solve(n: int, m: int, translations: Dict[int, List[int]]):
    visited = [0] # English
    curr_visited = [0]
    print(curr_visited)
    while True:
        next_to_visit = []
        for from_lang in curr_visited:
            to_lang_list = translations[from_lang]
            for to_lang, cost in to_lang_list:
                if to_lang not in visited and to_lang not in next_to_visit:
                    next_to_visit.append(to_lang)
        if len(next_to_visit) == 0:
            break
        curr_visited = next_to_visit
        visited.extend(curr_visited)
        print(curr_visited)
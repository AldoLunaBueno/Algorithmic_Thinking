from algorithms.my_way import solve
from collections import defaultdict
from typing import Dict, List



def main():
    n, m, translations = get_data()
    solve(n, m, translations)


def get_data():
    n, m = [int(x) for x in input().split(" ")]
    langs = ["English"] + input().split(" ")
    langs_to_int = {lang:i for i, lang in enumerate(langs)}

    # adjacency matrix
    translations: Dict[int, List[int]] = defaultdict(list)
    for _ in range(m):
        lang_1_str, lang_2_str, cost = input().split(" ")
        cost = int(cost)
        lang_1 = langs_to_int[lang_1_str]
        lang_2 = langs_to_int[lang_2_str]
        translations[lang_1].append((lang_2, cost))
        translations[lang_2].append((lang_1, cost))
    
    return n, m, translations

if __name__ == "__main__":
    main()
import random as rnd

with open("test_perf.txt", "w") as f:
    cases = []
    for i in range(1000):
        m = rnd.randint(0, 100)
        n = rnd.randint(0, 100)
        t = rnd.randint(0, 10000)
        one_case = f"{m} {n} {t}\n"
        f.write(one_case)

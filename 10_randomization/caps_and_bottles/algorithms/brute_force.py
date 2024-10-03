# Resources: ---, 59.13 MB
# Final score: 20/100 (4.0/20 points)

# time complexiy: O(n**2)
def solve(n: int):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"0 {i} {j}")
            evaluation = int(input().strip())
            if evaluation == 0:
                print(f"1 {i} {j}")
                break
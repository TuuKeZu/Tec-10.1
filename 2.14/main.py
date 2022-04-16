import time


def solve():
    x = 1
    while not (x % 12 == 0 and x % 34 == 0 and x % 56 == 0):
        x += 1
    print(f"{x}")



s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");


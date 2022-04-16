import time


def solve():
    x = 1
    n = 0
    while x < 9999:
        x *= 3
        n += 1
    
    print(f"n = {n} ({x})")



s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");

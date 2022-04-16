import time

# x**3 - 60x**2 + 60x = 59



def solve():
    x = 0;
    while x**3 - 60*x**2 + 60*x - 59 != 0:
        x += 1;
    
    print(f"{x} Solves the equation!");



s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");

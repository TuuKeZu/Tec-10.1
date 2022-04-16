import time

# a = 15n + 120, n = 1, 2, 3...

def solve_1():
    for n in range(10):
        a = 15*n + 120
        print(a)

def solve_2():
    a = 0
    n = 1
    while a <= 12456:
        a = 15*n + 120
        n += 1

        if(a == 12455):
            print(True)
            return
    
    print(False);

def solve_3():
    a = 0
    n = 1
    while a < 1000:
        a = 15*n + 120
        n += 1

    print(f"{n}, ({a})")
        




s = time.perf_counter()
solve_2()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");
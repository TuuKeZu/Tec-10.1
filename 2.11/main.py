import time


def solve():
    years = []
    for year in range(1800, 2200):
        if(year % 4 == 0):
            if(year % 100):
                if(year % 400):
                    years.append(year)
                    continue
            else:
                years.append(year)
                continue

    for year in years:
        print(year)



s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");
import random
import time
import math

# sqrt(a*b)

def solve_1():

    for a in range(2, 100):
        for b in range(2, 100):
            if math.sqrt(a * b).is_integer():
                break

    print(f"{a} and {b}'s geometric is an integer.")

def solve_2():
    iterations = 100000
    found = []

    for i in range(iterations):
        a = random.randint(0, 100)
        b = random.randint(0, 100)

        if math.sqrt(a * b).is_integer():
            found.append([a, b])
            continue

    print(f"From {iterations} randomly generated pairs, {len(found)} one's geometric average was an integer.")
    print(f"Random chance of guessing a pair is therefore {(len(found) / iterations) * 100}%")
    



s = time.perf_counter()
solve_2()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");

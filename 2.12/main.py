from re import A
import time


def solve():
    Aapo = 0
    Jaakko = Aapo + 1
    Kalle = Jaakko + 1
    
    while Aapo * Jaakko * Kalle != 42840:
        Aapo += 1
        Jaakko = Aapo + 1
        Kalle = Jaakko + 1
    print(f"Aapo: {Aapo}, Jaakko: {Jaakko}, Kalle: {Kalle}")
    
        


s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");
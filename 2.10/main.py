import time

ALKULUVUT = [29, 23, 19, 17, 13, 11, 7, 11, 7, 5, 3, 2]

# Main function
def solve():
    
    # CALCULATING

    x = 29282 # Value to be prime factorized
    m = [] # List of prime multiplications done to achieve that number
    d = [] # List of dublicate multiplications
    ans = "" # Final answer string

    # loop through every prime number to see if the value can be divided by it.
    for n in ALKULUVUT:
        while x % n == 0:
            x //= n
            m.append(n) # add the divider to multi.-list

    # Loop through each multiplication required to achieve target value.
    for o in m:
        c = m.count(o) # count how many times the same multiplication is performed

        if([o, c] not in d): # append the multiplication and the number of times its performed to the list.
            d.append([o, c])

    # FORMATTING

    ans += f"{x} prime factorized is: " # Intialize the answer string

    # Go through each multiplication
    for operation in d:
        num = operation[0] # The first value of the list within list is the multiplier
        pow = operation[1] # The second value of the list within list is the power which the multiplier should be in

        if(d.index(operation) > 0): # If the operation is the first one, don't add the multiplication symbol
            ans += " * "
        if(pow > 1): 
            ans += f"{num}^{pow}" # If the multiplier is added to the power of higher than 1, display it in the syntax of (num^pow).
        else:
            ans += f"{num}" # Else Display only the multiplier

    if(x > 1):
        ans += f" + {x}" # If there's still something left in value which cannot be factorized, add it.

    print(ans) # Finally print the answer





s = time.perf_counter()
solve()
e = time.perf_counter();

print(f"Solved in {(e - s) * 1000}ms");
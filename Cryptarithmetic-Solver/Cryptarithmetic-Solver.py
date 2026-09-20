import itertools

def solve_cryptarithmetic():
    for perm in itertools.permutations(range(10), 6):
        t, w, o, f, u, r = perm
        if t == 0 or f == 0:
            continue
        
        two = 100 * t + 10 * w + o
        four = 1000 * f + 100 * o + 10 * u + r
        
        if two + two == four:
            print(f"T={t}, W={w}, O={o}, F={f}, U={u}, R={r}\n")
            print(f"  {two}")
            print(f"+ {two}")
            print(" ----")
            print(f" {four}")

if __name__ == "__main__":
    solve_cryptarithmetic()
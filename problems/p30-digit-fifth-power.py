"""
[Problem Title]

[Problem Description]
"""

def run():
    power = 5
    limit = (9**power) * (power-1)
    res = 0
    for n in range(limit, 2, -1):
        digits = [ch for ch in str(n)]
        print(digits)
        if sum([int(d)**power for d in digits]) == n:
            
            res+=int("".join(digits))
      
    return res


if __name__ == "__main__":
    print(run())

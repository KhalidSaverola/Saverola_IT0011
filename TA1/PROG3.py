def pattern_a():
    n = 5
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        print()

pattern_a()

def pattern_b():
    i = 1
    while i <= 5:
        num = 2 * i - 1
        j = 1
        while j <= num:
            print(i, end="")
            j += 1
        print()
        i += 1

pattern_b()

# Collatz conjecture
# n -> n / 2 if n is even
# n -> 3n + 1 if n is odd
# All sequences converge to 1.
# Which starting value, under 1M, produces the longest sequence?

n = 1000000
max_count = -1
cache = {}
for i in range(1, n + 1):
    count = 0
    t = i
    while t > 1 and t not in cache:
        if t % 2 == 0:
            t = int(t / 2)
        else:
            t = 3 * t + 1

        count += 1
        # print(n, end=' ')

    cache[n] = count

    print(count, end=' ')
    if count > max_count:
        max_count = count

print(max_count)
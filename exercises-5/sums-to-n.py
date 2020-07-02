def sums_to_n(n):
    return [(i, j)
            for i in range(n+1)
            for j in range(n+1)[::-1]
            if i + j == n]

print(sums_to_n(5))


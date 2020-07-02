def fact(x):
    return 1 if x == 1 else x * fact(x-1)

nums = input().split()
print(sum([fact(int(x)) for x in nums]))


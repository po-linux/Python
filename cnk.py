def fuct(x):
    if x == 0 or x == 1:
        return 1
    return x * fuct(x-1)

n, k = map(int, input().split())
cnk = fuct(n) // fuct(k) // fuct(n-k)
print(cnk)
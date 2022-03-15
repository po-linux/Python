lst = [int(i) for i in input().split()]
res = list()

if len(lst) < 2:
    res = lst
else:
    for i in range(len(lst)):
        if i == len(lst) - 1:
            res.append(lst[i - 1] + lst[0])

        else:
            res.append(lst[i-1] + lst[i+1])

print(*res)
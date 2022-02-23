dna = input()
cnt = 1
res = dna[0]
for i in range(len(dna)-1):
    if dna[i] == dna[i+1]:
        cnt += 1
    else:
        res += str(cnt)
        res += dna[i+1]
        cnt = 1
res += str(cnt)
print(res)
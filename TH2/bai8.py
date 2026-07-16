import itertools 
t=int(input())
for _ in range(t):
    res = []
    xau = input()
    hv = list(xau) #chặt các char trong string ra "ABC"-> ["A","B","C"]
    cac_hv = itertools.permutations(hv)
    for s in cac_hv: 
        res.append("".join(s))
    print(*res)

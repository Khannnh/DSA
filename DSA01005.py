import itertools 
t=int(input())
for _ in range(t):
    n= int(input())
    res = []
    cac_hv = itertools.permutations(range(1,n+1))
    for hv in cac_hv: 
        s= ''.join(map(str ,hv))
        res.append(s)
    print(*res)

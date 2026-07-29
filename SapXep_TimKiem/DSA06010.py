t=int(input())
for _ in range(t):
    n=int(input())
    cac_so=input().split()
    chu_so = []
    for so in cac_so: 
        b = list(so)
        chu_so.extend(b)
    res=sorted(set(chu_so))
    print(*res)
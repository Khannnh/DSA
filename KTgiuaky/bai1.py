import itertools 
t=int(input())
for _ in range(t):
    n=int(input())
    res = []
    cac_xau = itertools.product(["A","B"] , repeat=n)
    for xau in cac_xau : #("A" ,"B")
        s="".join(map(str , xau))
        res.append(s)
    print(*res)
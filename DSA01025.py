import itertools 
t= int(input())
for _ in range(t): 
    n,k = list(map(int,input().split()))
    ds_chu = [chr(65+i) for i in range(n)]
    for tohop in itertools.combinations(ds_chu,k):
        th = "".join(tohop)
        print(th)
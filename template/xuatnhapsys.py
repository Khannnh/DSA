input_data = sys.stdin.read().split()
iterator = iter(input_data)
t=int(next(iterator))
for _ in range(t):
    n=int(next(iterator))
    k=int(next(iterator))
    a=[int(next(iterator)) for _ in range(n)]
    a.sort() #NHẤT ĐỊNH PHẢI SORT
    print(tong3sonhohonk(a,k))
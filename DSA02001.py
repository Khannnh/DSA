def dfs(a):
    print('[' + " ".join(map(str ,a)) + ']')
    #basecase 
    if len(a)==1 : 
        return 
    #xử lý 
    next_a=[]
    for i in range(0 , len(a)-1):
        sum_two = a[i] + a[i+1]
        next_a.append(sum_two)
    dfs(next_a)
t=int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int , input().split()))
    dfs(a)


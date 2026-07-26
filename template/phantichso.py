#phân tích số 2 
def solve(n):
    res = []
    def dfs(remain:int , last:int , path:list):
        #basecase
        if remain == 0 : 
            res.append('(' + " ".join(map(str,path)) + ')')
            return 
        #lựa chọn 
        for x in range(min(remain,last),0,-1):
            path.append(x)
            dfs(remain-x , x , path)
            path.pop()
    dfs(n,n,[]) 
    return res
t=int(input())
for _ in range(t):
    n=int(input())
    result = solve(n)
    print(len(result))
    print(*result)



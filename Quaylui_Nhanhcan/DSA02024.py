def solve(a:list):
    n=len(a)
    res = []
    def dfs(start_idx:int , path:list):
        #điều kiện in nghiệm , k phải basecase
        if len(path) >= 2 :
            res.append(" ".join(map(str,path)))
        for i in range(start_idx,n):
            #điều kiện chọn
            if path and a[i] <= path[-1]:
                continue
            path.append(a[i])
            dfs(i+1,path) #gọi path đang điền dở :))
            #hoàn tác
            path.pop()
    dfs(0,[])
    return res
n=int(input())
a=list(map(int,input().split()))
res = solve(a)
print("\n".join(sorted(res))) #đm sao sorted đc mà .sort() ko đc vì sửa mảng gốc hả??
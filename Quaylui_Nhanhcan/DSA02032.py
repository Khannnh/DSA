def solve(a, x):
    n = len(a)
    res = []
    a.sort()  #sort ngay vì lúc này là số nguyên ý 

    def dfs(remain, start, path):
        if remain == 0:
            res.append("{" + " ".join(map(str, path)) + "}")
            return

        for i in range(start, n):
            if a[i] > remain:
                break

            path.append(a[i])
            dfs(remain - a[i], i, path)
            path.pop()

    dfs(x, 0, [])
    return res
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    res = solve(a, x)

    if res:
        print(len(res), *res)
    else:
        print(-1)
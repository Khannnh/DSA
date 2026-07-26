t=int(input())
for _ in range(t):
    n,m = map(int ,input().split())
    a=list(map(int ,input().split()))
    b=list(map(int ,input().split()))

    a.sort()
    b.sort()
    result = a[-1]*b[0]
    print(result)
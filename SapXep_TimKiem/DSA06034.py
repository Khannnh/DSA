import itertools 
def captongbangk(a:list,k):
    n=len(a)
    cnt=0
    vitricap = itertools.combinations(range(n) , 2)
    for vitri in vitricap: #vị trí dạng tuple (0,1)
        tong = 0 
        for i in vitri : 
            tong += a[i]
        if tong == k : 
            cnt += 1 
    return cnt 
# Test
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(captongbangk(arr, k))

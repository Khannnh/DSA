def capsotongk(a,k):
    cnt = {}
    ans = 0 
    for x in a : 
        need = k-x 
        if cnt.get(need ,0) > 0 : 
            ans += cnt[need]
        cnt[x] = cnt.get(x,0) +1 #ko viết kiểu +=1 đc 
        #nhất định phải đánh dấu sau khi tìm need để tránh đếm thừa cặp x+x=k
    return ans
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(capsotongk(arr, k))
def capsotongk(arr,k):
    cnt = 0 
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n): # j từ i+1 chứ nếu để j từ 1 thì đếm trùng 
            if arr[i]+arr[j] == k : 
                cnt += 1 
    return cnt 
t=int(input())
for _ in range(t):
    n , k = list(map(int, input().split()))
    a=list(map(int, input().split()))
    print(capsotongk(a,k))
#bản chưa tối ưu của DSA06034
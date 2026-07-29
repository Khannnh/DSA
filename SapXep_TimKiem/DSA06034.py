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

def count_pairs(arr, k):
    arr.sort()
    n = len(arr)
    l = 0
    r = n - 1
    cnt = 0
    
    while l < r:
        tong = arr[l] + arr[r]
        
        if tong == k:
            # Xử lý trường hợp có nhiều giá trị trùng lặp
            
            # Nếu arr[l] == arr[r], tất cả phần tử từ l đến r đều giống nhau
            if arr[l] == arr[r]:
                # Số lượng phần tử trong đoạn
                num = r - l + 1
                # Số cặp = C(num, 2) = num * (num-1) // 2
                cnt += num * (num - 1) // 2
                break  # Không còn cặp nào khác
            
            # Đếm số lượng phần tử giống arr[l] bên trái
            left_val = arr[l]
            left_count = 0
            while l < n and arr[l] == left_val:
                left_count += 1
                l += 1
            
            # Đếm số lượng phần tử giống arr[r] bên phải
            right_val = arr[r]
            right_count = 0
            while r >= 0 and arr[r] == right_val:
                right_count += 1
                r -= 1
            
            # Số cặp = left_count * right_count
            cnt += left_count * right_count
            
        elif tong < k:
            l += 1
        else:  # tong > k
            r -= 1
    return cnt
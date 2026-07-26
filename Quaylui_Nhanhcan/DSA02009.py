# ------------------ Xử lý ------------------
def solve(n, k, a):
    total = sum(a)
    if total % k != 0:
        return 0
    target = total // k
    if max(a) > target:
        return 0
    bucket = [0] * k
    a.sort(reverse= True)  #sort lớn bé chạy nhanh hăn :)))
    # ------------------ Đệ quy ------------------
    def backtrack(i):
        # Base case
        if i == n:
            return True
        # Thử đưa a[i] vào từng bucket
        for j in range(k):
            # Cắt nhánh
            if bucket[j] + a[i] > target:
                continue
            # Chọn
            bucket[j] += a[i]
            # Đệ quy
            if backtrack(i + 1):
                return True
            # Hoàn tác
            bucket[j] -= a[i]
    if backtrack(0):
        return 1
    else: 
        return 0 
# ------------------ Main ------------------
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
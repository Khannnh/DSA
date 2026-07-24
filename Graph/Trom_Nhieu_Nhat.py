#cách để trộm đc nhiều đồ nhất :))) 
# Hàm 1: Logic Quy hoạch động tính tổng tài sản lớn nhất
#giải = quy hoạch động , na ná fibonacci 
def rob_max(n, a):
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    if n == 2:
        return max(a[0], a[1])
    # Khởi tạo mảng DP
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = max(a[0], a[1])
    # Điền mảng DP
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
    return dp[n - 1]
# Hàm 2: Xử lý Nhập / Xuất bình thường
def solve():
    # Nhập số lượng testcase T
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)
    for _ in range(t):
        # Nhập số ngôi nhà N
        n = int(input().strip())
        # Nhập N tài sản trên cùng 1 dòng
        a = list(map(int, input().split()))
        # Gọi hàm tính toán và in kết quả
        print(rob_max(n, a))
if __name__ == "__main__":
    solve()
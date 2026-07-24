# Hàm 1: Chuyên tính toán số cách di chuyển từ (n, m) về (0, 0)
def count_ways(n, m):
    # Khởi tạo bảng DP kích thước (n+1) x (m+1) toàn số 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Điểm xuất phát (n, m) có 1 cách
    dp[n][m] = 1

    # Duyệt lùi từ (n, m) về (0, 0)
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n and j == m:
                continue

            # Đi từ ô phía trên (i + 1, j) xuống
            if i + 1 <= n:
                dp[i][j] += dp[i + 1][j]

            # Đi từ ô bên phải (i, j + 1) sang
            if j + 1 <= m:
                dp[i][j] += dp[i][j + 1]

    # Trả về kết quả tại mốc (0, 0)
    return dp[0][0]
# Hàm 2: Chuyên xử lý Nhập / Xuất dữ liệu
def solve():
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        line = input().split()
        if not line:
            continue
        n, m = map(int, line)
        # Gọi hàm tính toán riêng
        ans = count_ways(n, m)
        # In kết quả
        print(ans)
if __name__ == "__main__":
    solve()
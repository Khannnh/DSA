def backtrack(r, c, n, matrix, path, res):
    # Nếu đến được ô đích (N-1, N-1) thì lưu chuỗi bước đi lại
    if r == n - 1 and c == n - 1:
        res.append(path)
        return

    # 1. Thử đi xuống Down ('D') trước (ưu tiên theo thứ tự từ điển)
    if r + 1 < n and matrix[r + 1][c] == 1:
        backtrack(r + 1, c, n, matrix, path + 'D', res)

    # 2. Thử đi sang phải Right ('R')
    if c + 1 < n and matrix[r][c + 1] == 1:
        backtrack(r, c + 1, n, matrix, path + 'R', res)

def solve():
    # Nhập số lượng testcase T
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        # Nhập kích thước ma trận N
        n = int(input().strip())

        # Nhập ma trận N x N
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)

        # Nếu ô đầu hoặc ô đích bị rào (bằng 0) thì chịu, in -1
        if matrix[0][0] == 0 or matrix[n - 1][n - 1] == 0:
            print(-1)
            continue

        res = []
        backtrack(0, 0, n, matrix, "", res)

        # Nếu res rỗng tức là không tìm thấy đường đi nào
        if not res:
            print(-1)
        else:
            print(*res)

if __name__ == "__main__":
    solve()
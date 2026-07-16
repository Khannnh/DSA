#đề cho len ko quá lớn nên chắc dùng đệ quy quay lui cắt nhánh 
def backtrack(s, k, i):
    global best

    # Hết lượt đổi hoặc đã xét hết chuỗi
    if k == 0 or i == len(s):
        cur = ''.join(s)
        if cur > best:
            best = cur
        return

    # Tìm chữ số lớn nhất từ vị trí i đến cuối
    max_digit = max(s[i:])

    # Nếu vị trí hiện tại đã là lớn nhất
    if s[i] == max_digit:
        backtrack(s, k, i + 1)
        return

    # Thử đổi với tất cả vị trí có max_digit
    for j in range(len(s) - 1, i, -1):
        if s[j] == max_digit:
            s[i], s[j] = s[j], s[i]      # swap
            backtrack(s, k - 1, i + 1)   # đệ quy
            s[i], s[j] = s[j], s[i]      # backtrack (undo)


T = int(input())

for _ in range(T):
    K = int(input())
    S = list(input())

    best = ''.join(S)

    backtrack(S, K, 0)

    print(best)
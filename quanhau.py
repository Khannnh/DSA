def solve():
    # 1. Nhập số lượng bộ test T
    t = int(input())
    
    # Khởi tạo các mảng đánh dấu toàn cục cho bàn cờ 8x8
    cols = [False] * 8
    diag1 = [False] * 16  # Đường chéo ngược (r + c)
    diag2 = [False] * 16  # Đường chéo xuôi (r - c + 8)
    
    for test_idx in range(1, t + 1):
        # 2. Đọc ma trận bàn cờ 8x8 bằng input() thông thường
        board = []
        for _ in range(8):
            # Đọc từng dòng, cắt theo khoảng trắng và chuyển thành số nguyên
            row = list(map(int, input().split()))
            board.append(row)
            
        max_score = 0
        
        # Hàm quay lui đặt hậu cho từng hàng r (từ 0 đến 7)
        def backtrack(r, current_score):
            nonlocal max_score
            
            # Nếu đã đặt xong cả 8 quân hậu (hàng 0 đến 7)
            if r == 8:
                max_score = max(max_score, current_score)
                return
            
            # Thử đặt hậu vào từng cột c ở hàng r
            for c in range(8):
                if not cols[c] and not diag1[r + c] and not diag2[r - c + 8]:
                    # Đặt quân hậu (Đánh dấu trạng thái)
                    cols[c] = diag1[r + c] = diag2[r - c + 8] = True
                    
                    # Gọi đệ quy sang hàng tiếp theo
                    backtrack(r + 1, current_score + board[r][c])
                    
                    # Bỏ quân hậu (Trả trạng thái / Quay lui)
                    cols[c] = diag1[r + c] = diag2[r - c + 8] = False

        # Chạy từ hàng 0 với điểm ban đầu bằng 0
        backtrack(0, 0)
        
        # 3. In ra theo đúng định dạng mẫu
        print(f"Test {test_idx}: {max_score}")

if __name__ == '__main__':
    solve()
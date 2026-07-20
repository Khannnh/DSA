# Mã Gray 2: Biến đổi xâu Gray thành xâu Nhị phân
t = int(input())
for _ in range(t):
    s = input()  # Nhập xâu ví dụ "0110"
    
    # Băm nhỏ từng ký tự và ép thành mảng số nguyên [0, 1, 1, 0] để dùng toán tử bitwise
    ma_gray = list(map(int, s)) 
    
    for i in range(1, len(ma_gray)):  # Bit đầu tiên (index 0) luôn giữ nguyên
        # CHỖ NÀY ĐỈNH NÈ: ma_gray[i-1] ở vòng lặp trước đã bị biến thành bit Nhị phân rồi.
        # Nên bản chất lệnh này là lấy: [Bit Gray hiện tại] XOR [Bit Nhị phân vừa tìm được].
        ma_gray[i] = ma_gray[i] ^ ma_gray[i-1]
        
    # Ép mảng số nguyên ngược về mảng chuỗi rồi nối lại in ra
    print("".join(map(str, ma_gray)))
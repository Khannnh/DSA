import sys

MOD = 10**9 + 7

# Hàm nhân 2 ma trận 2x2 và chia lấy dư cho MOD luôn
def multiply_matrix(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            total = 0
            for k in range(2):
                total = (total + A[i][k] * B[k][j]) % MOD
            C[i][j] = total
    return C

# Hàm tính ma trận A mũ n bằng lũy thừa nhị phân
def power_matrix(A, n):
    # Khởi tạo ma trận đơn vị (đóng vai trò như số 1 trong phép nhân thường)
    res = [[1, 0], [0, 1]]
    base = A
    
    while n > 0:
        if n % 2 == 1:
            res = multiply_matrix(res, base)
        base = multiply_matrix(base, base)
        n //= 2
    return res

def solve():
    # Đọc nhanh toàn bộ input để né TLE
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    
    out = []
    for i in range(1, T + 1):
        N = int(input_data[i])
        
        if N == 0:
            out.append("0")
            continue
        if N == 1:
            out.append("1")
            continue
            
        # Ma trận cơ sở Fibonacci
        A = [[1, 1], [1, 0]]
        
        # Tính A^(N-1)
        result_matrix = power_matrix(A, N - 1)
        
        # Phần tử tại vị trí [0][0] của ma trận kết quả chính là F_N
        out.append(str(result_matrix[0][0]))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
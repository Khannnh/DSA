def solve_test_case(A):
    # 1. Tận dụng syntax Python: dùng list comprehension + enumerate 
    # Biến [3, 1, 4] thành [(3, 0), (1, 1), (4, 2)]
    pairs = [(val, idx) for idx, val in enumerate(A)]
    
    # 2. Sắp xếp tăng dần theo giá trị (x[0]).
    # Nếu giá trị bằng nhau, thằng nào có index gốc LỚN HƠN (-x[1]) sẽ đứng trước.
    pairs.sort(key=lambda x: (x[0], -x[1]))
    
    max_diff = -1
    min_index = pairs[0][1] # Index gốc của phần tử nhỏ giá trị nhất
    
    # 3. Duyệt mảng đã sắp xếp để tìm khoảng cách lớn nhất
    for val, idx in pairs[1:]:
        # Điều kiện: Nếu index hiện tại lớn hơn min_index 
        # (Chắc chắn val > A[min_index] nhờ cách sort ưu tiên -x[1] ở bước 2)
        if idx > min_index:
            max_diff = max(max_diff, idx - min_index)
            
        # Luôn luôn cập nhật index gốc nhỏ nhất để làm "bàn đạp" i cho các số sau
        min_index = min(min_index, idx)
        
    return max_diff

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    print(solve_test_case(A))
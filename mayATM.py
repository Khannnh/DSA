import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    
    for _ in range(t):
        n = int(next(iterator))
        s = int(next(iterator))
        
        a = [int(next(iterator)) for _ in range(n)]
        
        # 1. SẮP XẾP GIẢM DẦN: Cực kỳ quan trọng để nhanh chóng tìm ra số tờ ít nhất
        a.sort(reverse=True)
        
        # Biến lưu số tờ ít nhất, ban đầu để một số vô cực
        min_notes = float('inf')
        
        def backtrack(index, current_sum, count):
            nonlocal min_notes
            
            # Nếu tìm được tổng S, cập nhật lại số tờ ít nhất
            if current_sum == s:
                min_notes = min(min_notes, count)
                return
            
            # 2. ĐIỀU KIỆN CẮT TỈA (PRUNING):
            # - Duyệt hết mảng
            # - Tổng hiện tại đã vượt S
            # - Số tờ đã chọn vượt quá kỉ lục min_notes tốt nhất hiện tại -> Dừng luôn
            if index == n or current_sum > s or count >= min_notes:
                return
            
            # Nhánh 1: CHỌN tờ tiền a[index]
            backtrack(index + 1, current_sum + a[index], count + 1)
            
            # Nhánh 2: KHÔNG CHỌN tờ tiền a[index]
            backtrack(index + 1, current_sum, count)

        # Bắt đầu quay lui từ tờ đầu tiên
        backtrack(0, 0, 0)
        
        # In kết quả
        if min_notes == float('inf'):
            print(-1)
        else:
            print(min_notes)

if __name__ == '__main__':
    solve()
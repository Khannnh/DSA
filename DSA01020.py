def xau_nhi_phan_truoc_v2(s):
    # Nếu xâu toàn số 0, xâu trước nó sẽ toàn số 1
    if '1' not in s:
        return '1' * len(s)
    
    # Tìm vị trí số '1' cuối cùng xuất hiện
    idx = s.rfind('1')
    
    # Biến số '1' đó thành '0', và toàn bộ số '0' phía sau thành '1'
    res = s[:idx] + '0' + '1' * (len(s) - 1 - idx)
    return res

t = int(input())
for _ in range(t):
    s = input().strip()
    print(xau_nhi_phan_truoc_v2(s))
import itertools

n, k = map(int, input().split())
ds = []
for _ in range(n):
    ds.append(input())

min_chenhlech = float('inf')

# Duyệt qua tất cả các hoán vị chỉ số từ 0 đến k - 1
for p in itertools.permutations(range(k)):
    ds_moi = []
    
    # Ứng với hoán vị p, biến đổi toàn bộ n xâu số
    for so in ds:
        chuoi_moi = ""
        for idx in p: 
            chuoi_moi += so[idx]
        so_moi = int(chuoi_moi)
        ds_moi.append(so_moi)
    
    # Tìm độ chênh lệch của hoán vị hiện tại
    hieu = max(ds_moi) - min(ds_moi)
    
    # Cập nhật độ chênh lệch nhỏ nhất
    if hieu < min_chenhlech:
        min_chenhlech = hieu

print(min_chenhlech)